# -*- coding: utf-8 -*-

from txoids.generic.deferreds import BaseAction
from txoids.ports import processors


class FetchPorts(BaseAction):

    def get_ports_proccessor(self):
        model = self.parser.model
        if model == "D-Link DES-3010G":
            cls = processors.DES3010GPortsProcessor
        elif model == "D-Link DGS-3100-24":
            cls = processors.DGS3100PortsProcessor
        elif model == "D-Link DGS-3100-24TG":
            cls = processors.DGS3100TGPortsProcessor
        else:
            cls = processors.PortsProcessor
        return cls(self.parser)

    def get_deferred(self):
        processor = self.get_ports_proccessor()
        d = self.walk(processor.get_oids())
        d.addCallback(processor.get_ports)
        return d
