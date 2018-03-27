# -*- coding: utf-8 -*-
from pynetsnmp.twistedsnmp import AgentProxy
from pynetsnmp.tableretriever import TableRetriever
from txoids.generic import processors

DEFAULT_TABLE_SETTINGS = {'timeout': 15, 'maxRepetitions': 10, 'limit': 10000}
DEFAULT_PROXY_TIMEOUT = 15


class BaseAction(object):
    proxy_settings = {
        'timeout': 1.0,
        'retryCount': 3
    }
    method = 'get'
    processor_class = None

    def __init__(self, parser, table_settings=DEFAULT_TABLE_SETTINGS):
        self.parser = parser
        self.table_settings = table_settings
        self.processor = self.get_processor()

    def get_open_proxy(self, timeout=DEFAULT_PROXY_TIMEOUT, **kwargs):
        community = kwargs.pop('community', None) or self.parser.community
        proxy = AgentProxy(
            self.parser.ip, snmpVersion='v2c', community=community,
            timeout=timeout, **kwargs
        )
        proxy.open()
        return proxy

    def get_processor(self):
        return self.processor_class(self.parser)

    def get_oids(self):
        raise NotImplementedError

    def get(self, oids):
        proxy = self.get_open_proxy()
        d = proxy.get(oids, **self.proxy_settings)
        d.addBoth(self.close_proxy, proxy)
        return d

    def walk(self, oids):
        proxy = self.get_open_proxy()
        tr = TableRetriever(proxy, oids, **self.table_settings)
        d = tr()
        d.addBoth(self.close_proxy, proxy)
        return d

    def get_deferred(self):
        oids = self.processor.get_oids()
        if self.method == 'get':
            d = self.get(oids)
        elif self.method == 'walk':
            d = self.walk(oids)
        else:
            raise AttributeError('Unknown method %s' % self.method)
        d.addCallback(self.processor.get_data)
        return d

    def close_proxy(self, result, proxy):
        """
        Callback для закрытия snmp-agenta
        """
        proxy.close()
        return result


class FetchArp(BaseAction):
    processor_class = processors.FetchArpProcessor
    method = 'walk'


class FetchFdb(BaseAction):
    processor_class = processors.FetchFdbProcessor
    method = 'walk'


class FetchModel(BaseAction):
    processor_class = processors.FetchModelProccessor


class FetchSerialNumber(BaseAction):
    processor_class = processors.FetchSerialNumberProccessor


class FetchHardwareVersion(BaseAction):
    processor_class = processors.FetchHardwareVersionProccessor


class FetchFirmwareVersion(BaseAction):
    processor_class = processors.FetchFirmwareVersionProccessor


class FetchMacAddress(BaseAction):
    processor_class = processors.FetchMacAddressProccessor


class FetchUptime(BaseAction):
    processor_class = processors.FetchUptimeProccessor
