# -*- coding: utf-8 -*-
from twisted.internet import reactor, defer
from txoids.engine import SnmpParser


@defer.inlineCallbacks
def fetch_data():
    parser = SnmpParser(
        '172.20.25.4', community='mymypub',
        community_write='mymypriv', model='D-Link DES-3200-28'
    )

    result = yield parser.fetch_arp()
    print(result)

    port = 1
    result = yield parser.cable_diag(port)
    print(result)

    result = yield parser.fetch_model()
    print(result)

    result = yield parser.fetch_serial_number()
    print(result)

    result = yield parser.fetch_hardware_version()
    print(result)

    result = yield parser.fetch_firwmare_version()
    print(result)

    result = yield parser.fetch_mac_address()
    print(result)


def main():
    d = fetch_data()
    d.addBoth(lambda x: reactor.stop())
    reactor.run()

if __name__ == '__main__':
    main()
