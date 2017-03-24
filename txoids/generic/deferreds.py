# -*- coding: utf-8 -*-
from pynetsnmp.twistedsnmp import AgentProxy
from pynetsnmp.tableretriever import TableRetriever
from txoids.utils import pretty_mac
import re

TABLE_SETTINGS = {'timeout': 15, 'maxRepetitions': 35, 'limit': 10000}


class BaseAction(object):
    oids = []
    proxy_settings = {
        'timeout': 1.0,
        'retryCount': 3
    }

    def __init__(self, parser):
        self.parser = parser

    def get_open_proxy(self, **kwargs):
        community = kwargs.pop('community', None) or self.parser.community
        ip = kwargs.pop('ip', None) or self.parser.ip
        proxy = AgentProxy(
            ip, snmpVersion='v2c', community=community, timeout=15, **kwargs)
        proxy.open()
        return proxy

    def get_oids(self):
        return self.oids

    def get(self, oids=None):
        oids = oids or self.get_oids()
        proxy = self.get_open_proxy()
        d = proxy.get(oids, **self.proxy_settings)
        d.addBoth(self.close_proxy, proxy)
        return d

    def walk(self, oids=None):
        oids = oids or self.get_oids()
        proxy = self.get_open_proxy()
        tr = TableRetriever(proxy, oids, **TABLE_SETTINGS)
        d = tr()
        d.addBoth(self.close_proxy, proxy)
        return d

    def parse_result(self, result):
        return result.values()[0]

    def get_deferred(self):
        d = self.get()
        d.addCallback(self.parse_result)
        return d

    def close_proxy(self, result, proxy):
        """
        Callback для закрытия snmp-agenta
        """
        proxy.close()
        return result


class FetchArp(BaseAction):
    oids = ['.1.3.6.1.2.1.4.22.1.2']

    def parse_result(self, result):
        arps = super(FetchArp, self).parse_result(result)
        results = []
        for key in arps:
            mac = pretty_mac(arps[key])
            ip = ".".join(key.split('.')[-4:])
            results.append({'mac': mac, 'ip': ip})
        return results

    def get_deferred(self):
        d = self.walk()
        d.addCallback(self.parse_result)
        return d


class FetchModel(BaseAction):
    oids = ['1.3.6.1.2.1.1.1.0']


class RegexAction(BaseAction):
    DEFAULT_OID = None
    OIDS_MAP = {}

    def get_oids(self):
        for pattern, oid in self.OIDS_MAP.iteritems():
            if re.match(pattern, self.parser.model):
                return [oid]
        return [self.DEFAULT_OID]


class FetchSerialNumber(RegexAction):
    DEFAULT_OID = '1.3.6.1.4.1.171.12.1.1.12.0'
    OIDS_MAP = {
        r'DGS-3100-\d+([A-z]+)?': '1.3.6.1.2.1.47.1.1.1.1.11.67108992',
        r'DGS-1210-12TS': '1.3.6.1.4.1.171.10.76.44.1.1.30.0',
        r'DGS-1210-10': '1.3.6.1.4.1.171.10.76.35.1.1.30.0',
        r'DGS-1210-20': '1.3.6.1.4.1.171.10.76.31.1.1.30.0',
        r'DGS-1210-28': '1.3.6.1.4.1.171.10.76.28.1.1.30.0'
    }


class FetchHardwareVersion(RegexAction):
    DEFAULT_OID = '1.3.6.1.2.1.16.19.3.0'
    OIDS_MAP = {
        r'DGS-3100-\d+([A-z]+)?': '1.3.6.1.2.1.47.1.1.1.1.8.67108992',
        r'DES-3028(G)?$': '1.3.6.1.2.1.47.1.1.1.1.8.1'
    }


class FetchFirmwareVersion(RegexAction):
    DEFAULT_OID = '1.3.6.1.2.1.16.19.2.0'
    OIDS_MAP = {
        r'DES-3010G$': '1.3.6.1.4.1.171.12.1.2.7.1.2.257',
        r'DGS-3100-\d+([A-z]+)?': '1.3.6.1.4.1.171.10.94.89.89.53.14.1.2.1'
    }


class FetchMacAddress(RegexAction):
    DEFAULT_OID = '1.3.6.1.2.1.2.2.1.6.5121'
    OIDS_MAP = {
        r'DGS-1210-28': '1.3.6.1.4.1.171.10.76.28.1.28.2.2.5.0',
        r'DGS-1210-20': '1.3.6.1.4.1.171.10.76.31.1.28.2.2.5.0',
        r'DGS-1210-10': '1.3.6.1.4.1.171.10.76.35.1.28.2.2.5.0',
        r'DGS-1210-12TS': '1.3.6.1.4.1.171.10.76.44.1.28.2.2.5.0',
        r'DGS-3100-\d+([A-z]+)?': '1.3.6.1.2.1.2.2.1.6.100000'
    }

    def parse_result(self, result):
        mac_string = super(FetchMacAddress, self).parse_result(result)
        return pretty_mac(mac_string)
