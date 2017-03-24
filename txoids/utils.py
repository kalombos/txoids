# -*- coding: utf-8 -*-
from twisted.internet import reactor
from twisted.internet.task import deferLater


def pretty_mac(mac_string):
    return ':'.join('%02x' % ord(b) for b in mac_string)


def deferredSleep(howLong):
    return deferLater(reactor, howLong, lambda: None)
