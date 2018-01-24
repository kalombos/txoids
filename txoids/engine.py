# -*- coding: utf-8 -*-

from twisted.internet import defer
from txoids.generic.deferreds import (
    FetchArp,
    FetchFdb,
    FetchModel,
    FetchSerialNumber,
    FetchHardwareVersion,
    FetchFirmwareVersion,
    FetchMacAddress,
    FetchUptime
)
from txoids.cable_diag.deferreds import CableDiag
from txoids.ports.deferreds import FetchPorts
from txoids.igmp.deferreds import FetchIgmp


class SnmpParser(object):
    def __init__(self, ip, community, community_write=None, model=None):
        self.ip = ip
        self.model = model
        self.community = community
        self.community_write = community_write

    def make_action(self, cls, *args, **kwargs):
        return cls(self, *args, **kwargs).get_deferred()

    def fetch_ports(self, **kwargs):
        return self.make_action(FetchPorts)

    def fetch_arp(self, **kwargs):
        return self.make_action(FetchArp)

    def fetch_fdb(self, **kwargs):
        return self.make_action(FetchFdb)

    def cable_diag(self, port):
        return self.make_action(CableDiag, port)

    def fetch_igmp(self):
        return self.make_action(FetchIgmp)

    def fetch_model(self):
        return self.make_action(FetchModel)

    def fetch_uptime(self):
        return self.make_action(FetchUptime)

    @defer.inlineCallbacks
    def detect_model(self):
        model = yield self.fetch_model()
        self.model = model
        defer.returnValue(model)

    def fetch_serial_number(self):
        return self.make_action(FetchSerialNumber)

    def fetch_hardware_version(self):
        return self.make_action(FetchHardwareVersion)

    def fetch_firwmare_version(self):
        return self.make_action(FetchFirmwareVersion)

    def fetch_mac_address(self):
        return self.make_action(FetchMacAddress)
