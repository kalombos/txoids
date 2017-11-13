# -*- coding: utf-8 -*-
import binascii
from txoids.generic.processors import MultiOidMapProcessor
from txoids.igmp.oids import OIDS_MAP
from txoids.utils import FullDict, chunks
import re
from six import binary_type


class IGMPProcessor(MultiOidMapProcessor):

    oids_map = OIDS_MAP
    ip_regex = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"

    port_fields = ['GrpRouterPorts', 'GrpIncludeMemberPorts', 'GrpExcludeMemberPorts']
    ip_fields = ['ip', 'group', 'GrpGrpAddr']

    def decode_ip(self, value):
        if re.match(self.ip_regex, value):
            return value
        value = str(value)
        bin_str = binascii.b2a_hex(value)
        octets = []
        for chunk in chunks(bin_str, 2):
            octets.append(str(int(chunk, 16)))
        return '.'.join(octets)

    def decode_ports(self, value):
        value = binary_type(value)
        bin_str = binascii.b2a_hex(value)
        result = ''
        for chunk in chunks(bin_str, 2):
            result += bin(int(chunk, 16)).replace('0b', '').zfill(8)

        ports = []
        for num, port in enumerate(result, 1):
            if port == '1':
                ports.append(str(num))
        return ports

    def get_data(self, result):
        data = {}
        for field_name, field in self.oids_set.items():
            field_data = FullDict()
            oid = field['oid']
            values = result[oid]
            for group, value in values.items():
                group_id, group_name = group.replace(oid + '.', '').split('.', 1)
                column_name = field['columns'].get(group_id)
                if column_name:
                    field_data[group_name][column_name] = value

            field_data = field_data.to_dict()
            data[field_name] = list(field_data.values())

        for group, values in data.items():
            for value in values:
                for field in self.port_fields:
                    if field in value:
                        value[field] = self.decode_ports(value[field])
                for field in self.ip_fields:
                    if field in value:
                        value[field] = self.decode_ip(value[field])
        return data
