# -*- coding: utf-8 -*-

from txoids.generic.deferreds import BaseAction
import datetime
import binascii

# TODO: Not implemented yet


def chunks(l, n):
    """
    Метод разбивает список l на списки по n элементов
    """

    for i in xrange(0, len(l), n):
        yield l[i:i + n]


class FetchIgmp(BaseAction):
    oids = ['.1.3.6.1.4.1.171.12.73.2.1.5.1',
            '.1.3.6.1.4.1.171.12.73.2.1.2.1']

    def get_deferred(self):
        d = self.walk(self.oids)
        d.addCallback(self.parse_result)
        return d

    def group_table(self, oid, table_map, igmp_result):
        values = igmp_result[oid]
        result = {}
        for key in values:
            column_id, group_name = key.replace(oid + '.', '').split('.', 1)
            if group_name not in result:
                result[group_name] = {table_map.get(column_id): values[key]}
            else:
                result[group_name][table_map.get(column_id)] = values[key]
        return result.values()

    def decode_ports(self, value):
        bin_str = binascii.b2a_hex(value)
        result = ''
        for chunk in chunks(bin_str, 2):
            result += bin(int(chunk, 16)).replace('0b', '').zfill(8)

        ports = []
        for num, port in enumerate(result, 1):
            if port == '1':
                ports.append(str(num))
        return ','.join(ports)

    def parse_result(self, result):
        table_map = {'1': 'vlan', '2': 'group', '3': 'port', '4': 'ip'}
        first_values = self.group_table('.1.3.6.1.4.1.171.12.73.2.1.5.1', table_map, result)

        table_map = {'1': 'GrpSrcAddr', '2': 'GrpGrpAddr', '3': 'GrpIncludeMemberPorts',
                     '4': 'GrpExcludeMemberPorts', '5': 'GrpRouterPorts',
                     '6': 'GrpUpTime', '7': 'GrpExpiryTime'}
        second_values = self.group_table('.1.3.6.1.4.1.171.12.73.2.1.2.1', table_map, result)
        # # собираем все ip-шники для запроса
        # ips = [row['group'] for row in first_values]
        # ips.extend([row['GrpGrpAddr'] for row in second_values])
        # # выбираем только уникальные
        # multicasts = {}
        # for value in first_values:
        #     value['group'] += " - %s" % multicasts.get(value['group'], u'Неизвестная группа')
        # for value in second_values:
        #     value['GrpRouterPorts'] = self.decode_ports(value['GrpRouterPorts'])
        #     value['GrpIncludeMemberPorts'] = self.decode_ports(value['GrpIncludeMemberPorts'])
        #     value['GrpExcludeMemberPorts'] = self.decode_ports(value['GrpExcludeMemberPorts'])
        #     value['GrpUpTime'] = str(datetime.timedelta(seconds=value['GrpUpTime']))
        #     value['GrpExpiryTime'] = str(datetime.timedelta(seconds=value['GrpExpiryTime']))
        #     value['GrpGrpAddr'] += " - %s" % multicasts.get(
        #         value['GrpGrpAddr'], u'Неизвестная группа'
        #     )
        return first_values, second_values
