## txoids
There is a toold for parsing switches using SNMP protocol. 
It uses pynetsnmp library which works pretty fast with SNMP. See **example.py** for more information


```
# -*- coding: utf-8 -*-
from twisted.internet import reactor, defer
from txoids.engine import SnmpParser


@defer.inlineCallbacks
def fetch_data():
    parser = SnmpParser(
        '172.20.25.4', community='password',
        community_write='password', model='D-Link DES-3200-28'
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
    
>>>[{'ip': '172.20.25.1', 'mac': '00:04:96:82:51:bb'}, {'ip': '172.20.25.0', 'mac': 'ff:ff:ff:ff:ff:ff'}, {'ip': '172.20.25.255', 'mac': 'ff:ff:ff:ff:ff:ff'}, {'ip': '172.20.25.4', 'mac': '00:26:5a:8e:c4:20'}]
>>>{'test1': u'no-cable', 'test3': u'other', 'test2': u'no-cable', 'test4': u'other', 'port_type': u'fastEthernet', 'link_status': u'link-down', 'length3': 0, 'length2': 0, 'length1': 0, 'length4': 0, 'error': None, 'test_status': 1}
>>>D-Link DES-3200-28 Fast Ethernet Switch
>>>PVI41A4006567
>>>A1
>>>Build 1.88.B001
>>>00:26:5a:8e:c4:20

```

