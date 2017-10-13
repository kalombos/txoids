# -*- coding: utf-8 -*-
from twisted.internet import reactor
from twisted.internet.task import deferLater


class FullDict(dict):

    def __getitem__(self, item):
        if item not in self:
            self[item] = FullDict()
        return super(FullDict, self).__getitem__(item)


def pretty_mac(mac_string):
    return ':'.join('%02x' % ord(b) for b in mac_string)


def deferredSleep(howLong):
    return deferLater(reactor, howLong, lambda: None)


def chunks(l, n):

    for i in xrange(0, len(l), n):
        yield l[i:i + n]
