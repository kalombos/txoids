# -*- coding: utf-8 -*-
from txoids.utils import pretty_mac
import re


class AbstractProccessor(object):

    def __init__(self, parser, *args, **kwargs):
        self.parser = parser
        self.oids = self.get_oids()

    def get_oids(self):
        return []

    def get_data(self, result):
        return list(result.values())[0]


class OidProcessor(AbstractProccessor):
    oid = None

    def get_oids(self):
        return [self.oid]


class MultiOidMapProcessor(AbstractProccessor):
    oids_map = {}

    def __init__(self, *args, **kwargs):
        super(MultiOidMapProcessor, self).__init__(*args, **kwargs)
        self.oids_set = self.get_oids_set()

    def get_oids_set(self):
        oids_map = self.oids_map.copy()
        default_oid_set = oids_map.pop('default', None)
        for pattern, oid_set in oids_map.items():
            if re.search(pattern, self.parser.model):
                return oid_set
        return default_oid_set

    def get_oids(self):
        return [v['oid'] for v in self.get_oids_set().values()]


class OidMapProcessor(MultiOidMapProcessor):

    def get_oids(self):
        return [self.get_oids_set()]


class FetchArpProcessor(OidProcessor):

    oid = '.1.3.6.1.2.1.4.22.1.2'

    def get_data(self, result):
        arps = super(FetchArpProcessor, self).get_data(result)
        results = []
        for key in arps:
            mac = pretty_mac(arps[key])
            ip = ".".join(key.split('.')[-4:])
            results.append({'mac': mac, 'ip': ip})
        return results


class FetchFdbProcessor(OidProcessor):

    oid = '.1.3.6.1.2.1.17.7.1.2.2.1.2'

    def get_data(self, result):
        fdbs = super(FetchFdbProcessor, self).get_data(result)
        results = []
        for key in fdbs:
            tmp = list(map(int, key.split(".")[1:]))
            vlan = tmp[-7]
            mac = "%02x:%02x:%02x:%02x:%02x:%02x" % tuple(i for i in tmp[-6:])
            port = int(fdbs[key])
            results.append({'mac': mac, 'vlan': vlan, 'port': port})
        return results


class FetchModelProccessor(OidProcessor):
    oid = '1.3.6.1.2.1.1.1.0'


class FetchSerialNumberProccessor(OidMapProcessor):
    oids_map = {
        'default': '1.3.6.1.4.1.171.12.1.1.12.0',
        r'DGS-3100-\d+([A-z]+)?': '1.3.6.1.2.1.47.1.1.1.1.11.67108992',
        r'DGS-1210-12TS': '1.3.6.1.4.1.171.10.76.44.1.1.30.0',
        r'DGS-1210-10': '1.3.6.1.4.1.171.10.76.35.1.1.30.0',
        r'DGS-1210-20': '1.3.6.1.4.1.171.10.76.31.1.1.30.0',
        r'DGS-1210-28': '1.3.6.1.4.1.171.10.76.28.1.1.30.0'
    }


class FetchHardwareVersionProccessor(OidMapProcessor):
    oids_map = {
        'default': '1.3.6.1.2.1.16.19.3.0',
        r'DGS-3100-\d+([A-z]+)?': '1.3.6.1.2.1.47.1.1.1.1.8.67108992',
        r'DES-3028(G)?$': '1.3.6.1.2.1.47.1.1.1.1.8.1'
    }


class FetchFirmwareVersionProccessor(OidMapProcessor):
    oids_map = {
        'default': '1.3.6.1.2.1.16.19.2.0',
        r'DES-3010G$': '1.3.6.1.4.1.171.12.1.2.7.1.2.257',
        r'DGS-3100-\d+([A-z]+)?': '1.3.6.1.4.1.171.10.94.89.89.53.14.1.2.1'
    }


class FetchMacAddressProccessor(OidMapProcessor):
    oids_map = {
        'default': '1.3.6.1.2.1.2.2.1.6.5121',
        r'DGS-1210-28': '1.3.6.1.4.1.171.10.76.28.1.28.2.2.5.0',
        r'DGS-1210-20': '1.3.6.1.4.1.171.10.76.31.1.28.2.2.5.0',
        r'DGS-1210-10': '1.3.6.1.4.1.171.10.76.35.1.28.2.2.5.0',
        r'DGS-1210-12TS': '1.3.6.1.4.1.171.10.76.44.1.28.2.2.5.0',
        r'DGS-3100-\d+([A-z]+)?': '1.3.6.1.2.1.2.2.1.6.100000'
    }

    def get_data(self, result):
        mac_string = list(result.values())[0]
        return pretty_mac(mac_string)


class FetchUptimeProccessor(OidProcessor):
    oid = '1.3.6.1.2.1.1.3.0'
