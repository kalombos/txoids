# -*- coding: utf-8 -*-

from txoids.utils import FullDict
from .oids import OIDS_MAP
from collections import OrderedDict
import re
import binascii
import logging
import six


class PortsProcessor(object):

    main_oids = {
        # ifOperStatus
        'oper': '.1.3.6.1.2.1.2.2.1.8',
        # ifType
        'type': '.1.3.6.1.2.1.2.2.1.3',
        # ifSpeed
        'speed': '.1.3.6.1.2.1.2.2.1.5',
        # ifName
        'name': '.1.3.6.1.2.1.31.1.1.1.1',
        # ifAlias
        'alias': '.1.3.6.1.2.1.31.1.1.1.18',
        # ifAdminStatus
        'admin': '.1.3.6.1.2.1.2.2.1.7',
    }

    lldp_oid = '.1.0.8802.1.1.2.1.3.7.1.3'

    port_fields = ('equipment', 'index', 'speed', 'name', 'alias', 'lldp', 'oper', 'admin',
                   "copper_admin_duplex", "copper_admin_speed", "copper_admin_state",
                   "copper_flow_control", "copper_mdix", "copper_oper_duplex",
                   "copper_oper_speed", "fiber_admin_duplex", "fiber_admin_speed",
                   "fiber_admin_state", "fiber_flow_control", "fiber_mdix", "fiber_oper_duplex",
                   "fiber_oper_speed")

    def __init__(self, parser):
        self.parser = parser
        self.medium_type_oids = OIDS_MAP.get(self.parser.model, {})

    def process_main_oids(self, result, ports):
        for field, oid in self.main_oids.items():
            for key, value in result[oid].items():
                port_index = key.split('.')[-1]
                ports[port_index][field] = value
                ports[port_index]['index'] = port_index
                ports[port_index]['medium_types'] = FullDict()
        return ports

    def get_port_index(self, ports, key):
        key = key.split('.')[-1]
        for port_index in ports.keys():
            if int(port_index) % 1000 == int(key):
                return port_index
        return key

    def process_lldp_oid(self, result, ports):
        field = 'lldp'
        for key, value in result[self.lldp_oid].items():
            port_index = self.get_port_index(ports, key)
            ports[port_index][field] = value

    def process_medium_types(self, result, ports):
        for field, description in self.medium_type_oids.items():
            oid = description['oid']
            for key, value in result[oid].items():
                port_index = key.split('.')[-2]
                medium_type_index = key.split('.')[-1]
                ports[port_index]['medium_types'][medium_type_index][field] = value
        for port_index in ports:
            ports[port_index]['medium_types'] = ports[port_index]['medium_types'].values()
        return ports

    def get_data(self, result):
        ports_result = FullDict()
        self.process_main_oids(result, ports_result)
        self.process_lldp_oid(result, ports_result)
        self.process_medium_types(result, ports_result)
        return self.process_ports(ports_result)

    @classmethod
    def convert_portname(cls, portname):
        """
        Метод конвертирует snmp-имя порта в удобочитаемое
        :param portname: str-объект, имя порта
        """

        try:
            split_symbol = re.search(r'[/:]', portname).group()
            module, begin = portname.split(split_symbol)
            module = int(module)
            begin = int(begin)
        except (ValueError, AttributeError):
            return portname

        while begin > 64:
            begin -= 64
            module += 1
        return "%d:%d" % (module, begin)

    def process_lldp(self, lldp):
        if lldp:
            return binascii.b2a_hex(lldp)

    def process_speed(self, port_speed):
        port_speed = int(port_speed)
        if port_speed > 1000000:
            port_speed = int(port_speed / 1000000)
            if port_speed == 4294:
                port_speed = 10000
        return port_speed

    def process_ports(self, ports_result):
        ports = []
        for port in ports_result.values():
            try:
                port['index'] = int(port['index'])
                port['type'] = int(port['type'])
            except TypeError:
                continue
            if port['type'] != 6 and port['type'] != 117:
                continue

            port['name'] = self.convert_portname(port['name'])

            if port['name'].startswith('ch') and port['index'] in range(301, 333):
                continue

            port['lldp'] = self.process_lldp(port['lldp'])
            port['speed'] = self.process_speed(port['speed'])
            if isinstance(port['alias'], six.binary_type):
                port['alias'] = port['alias'].decode()
            for medium_type in port['medium_types']:
                for field, value in medium_type.items():
                    value = str(value)
                    values = self.medium_type_oids[field]['values']
                    if values and value not in values:
                        logging.warning(
                            u"%s, %s has not string value "
                            u"for '%s' in field '%s'" %
                            (self.parser.ip, self.parser.model, value, field)
                        )
                    medium_type[field] = values.get(value, value)

                self.process_nway_state(medium_type)
                self.process_nway_status(medium_type)
                prefix = medium_type['medium_type']
                del medium_type['medium_type']
                for field, value in medium_type.items():
                    field = "%s_%s" % (prefix, field)
                    port[field] = value
            del port['medium_types']

            ordered_port = OrderedDict()
            for field in self.port_fields:
                ordered_port[field] = port.get(field, None)
            ports.append(ordered_port)
        return sorted(ports, key=lambda x: int(x['index']))

    def get_map_value(self, map_, value):
        for field, map_value in map_.items():
            if field.lower() in value.lower():
                return map_value
        return value

    def process_nway_state(self, medium_type):
        nway_state = medium_type['nway_state']
        speed_map = {
            "nway-enabled": "auto",
            "auto": "auto",
            "10Mbps": "10",
            "100Mbps": "100",
            "1Gigabps": "1000",
            "1000M": "1000",
            "100M": "100",
            "10M": "10"
        }

        medium_type['admin_speed'] = self.get_map_value(speed_map, nway_state)

        duplex_map = {
            "nway-enabled": "auto",
            "auto": "auto",
            "Full": "full",
            "Half": "half",
        }
        medium_type['admin_duplex'] = self.get_map_value(duplex_map, nway_state)
        del medium_type['nway_state']

    def process_nway_status(self, medium_type):
        nway_status = medium_type['nway_status']
        speed_map = {
            "link-down": "down",
            "auto": "down",
            "10Mbps": "10",
            "100Mbps": "100",
            "1Gigabps": "1000",
            "10G": "10000",
            "1000M": "1000",
            "100M": "100",
            "10M": "10"
        }
        medium_type['oper_speed'] = self.get_map_value(speed_map, nway_status)
        duplex_map = {
            "link-down": "down",
            "auto": "down",
            "Full": "full",
            "Half": "half",
        }
        medium_type['oper_duplex'] = self.get_map_value(duplex_map, nway_status)
        del medium_type['nway_status']

    def get_oids(self):
        medium_type_oids = [x['oid'] for x in self.medium_type_oids.values()]
        return list(self.main_oids.values()) + [self.lldp_oid] + medium_type_oids


class DES3010GPortsProcessor(PortsProcessor):

    def get_medium_type(self, port_index):
        if int(port_index) == 10:
            medium_type_index = 2
            medium_type = 'fiber'
        else:
            medium_type_index = 1
            medium_type = 'copper'
        return medium_type, medium_type_index

    def process_medium_types(self, result, ports):
        for field, description in self.medium_type_oids.items():
            oid = description['oid']
            for key, value in result[oid].items():
                port_index = key.split('.')[-1]
                medium_type, medium_type_index = self.get_medium_type(port_index)
                ports[port_index]['medium_types'][medium_type_index][field] = value
                ports[port_index]['medium_types'][medium_type_index]['medium_type'] = medium_type
        for port_index in ports:
            ports[port_index]['medium_types'] = ports[port_index]['medium_types'].values()
        return ports

    def process_ports(self, ports_result):
        self.medium_type_oids = self.medium_type_oids.copy()
        self.medium_type_oids['medium_type'] = {'values': {'fiber': 'fiber', 'copper': 'copper'}}
        return super(DES3010GPortsProcessor, self).process_ports(ports_result)


class DGS3100PortsProcessor(DES3010GPortsProcessor):

    def convert_speed(self, speed):
        try:
            speed = int(speed)
        except (TypeError, ValueError):
            return speed
        if speed > 1000000:
            speed /= 1000000
        return str(speed)

    def get_medium_type(self, port_index):
        medium_type_index = 1
        medium_type = 'copper'
        return medium_type, medium_type_index

    def process_nway_state(self, medium_type):
        admin_speed = medium_type['nway_state_speed']
        if admin_speed == "0":
            admin_speed = "auto"
        medium_type['admin_speed'] = self.convert_speed(admin_speed)
        del medium_type['nway_state_speed']

        admin_duplex = medium_type['nway_state_duplex']
        if admin_duplex == "none":
            admin_duplex = "auto"
        medium_type['admin_duplex'] = admin_duplex
        del medium_type['nway_state_duplex']

    def process_nway_status(self, medium_type):
        oper_speed = medium_type['nway_status_speed']
        if oper_speed == "0":
            oper_speed = "down"
        medium_type['oper_speed'] = oper_speed
        del medium_type['nway_status_speed']

        oper_duplex = medium_type['nway_status_duplex']
        if oper_duplex == "unknown":
            oper_duplex = "down"
        medium_type['oper_duplex'] = oper_duplex
        del medium_type['nway_status_duplex']


class DGS3100TGPortsProcessor(DGS3100PortsProcessor):
    def get_medium_type(self, port_index):
        if int(port_index) > 8:
            medium_type_index = 2
            medium_type = 'fiber'
        else:
            medium_type_index = 1
            medium_type = 'copper'
        return medium_type, medium_type_index
