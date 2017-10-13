# -*- coding: utf-8 -*-


OIDS_MAP = {
    'default': {
        'snooping_hosts': {
            'oid': '.1.3.6.1.4.1.171.12.73.2.1.5.1',
            'columns': {
                '1': 'vlan', '2': 'group', '3': 'port', '4': 'ip'
            }
        },
        'snooping_groups': {
            'oid': '.1.3.6.1.4.1.171.12.73.2.1.2.1',
            'columns': {
                '1': 'GrpSrcAddr', '2': 'GrpGrpAddr', '3': 'GrpIncludeMemberPorts',
                '4': 'GrpExcludeMemberPorts', '5': 'GrpRouterPorts',
                '6': 'GrpUpTime', '7': 'GrpExpiryTime'
            }
        }
    }
}
