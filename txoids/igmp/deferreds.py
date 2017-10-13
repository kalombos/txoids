# -*- coding: utf-8 -*-

from txoids.generic.deferreds import BaseAction
from txoids.igmp.processors import IGMPProcessor


class FetchIgmp(BaseAction):
    processor_class = IGMPProcessor
    method = 'walk'
