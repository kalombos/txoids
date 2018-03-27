# -*- coding: utf-8 -*-

from txoids.generic.deferreds import BaseAction
from txoids.ports import processors


class FetchPorts(BaseAction):

    method = 'walk'

    def get_processor(self):
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
