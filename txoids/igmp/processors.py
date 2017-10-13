# -*- coding: utf-8 -*-
import binascii
from txoids.generic.processors import MultiOidMapProcessor
from txoids.igmp.oids import OIDS_MAP
from txoids.utils import FullDict, chunks


class IGMPProcessor(MultiOidMapProcessor):

    oids_map = OIDS_MAP

    port_fields = ['GrpRouterPorts', 'GrpIncludeMemberPorts', 'GrpExcludeMemberPorts']

    def decode_ports(self, value):
        value = str(value)
        bin_str = binascii.b2a_hex(value)
        result = ''
        for chunk in chunks(bin_str, 2):
            result += bin(int(chunk, 16)).replace('0b', '').zfill(8)

        ports = []
        for num, port in enumerate(result, 1):
            if port == '1':
                ports.append(str(num))
        return ','.join(ports)

    def get_data(self, result):
        data = {}
        for field_name, field in self.oids_set.items():
            field_data = FullDict()
            oid = field['oid']
            values = result[oid]
            for group, value in values.items():
                group_id, group_name = group.replace(oid + '.', '').split('.', 1)
                column_name = field['columns'].get(group_id)
                field_data[group_name][column_name] = value
            data[field_name] = field_data.values()
        for value in data['snooping_groups']:
            for field in self.port_fields:
                value[field] = self.decode_ports(value[field])
        return data
