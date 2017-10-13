# -*- coding: utf-8 -*-
from txoids.cable_diag.oids import OIDS_MAP
from txoids.generic.processors import MultiOidMapProcessor


class StopDiagnostic(Exception):
    pass


class CableDiagProcessor(MultiOidMapProcessor):
    oids_map = OIDS_MAP

    def __init__(self, parser, port):
        super(CableDiagProcessor, self).__init__(parser, port)
        self.port = port
        self.statuses = self.oids_set['statuses']
        self.oids = self.oids_set['oids']
        self.cable_diag = {
            'port_type': None, 'link_status': None, 'test1': None,
            'test2': None, 'test3': None, 'test4': None, 'length1': None,
            'length2': None, 'length3': None, 'length4': None,
            'error': None, 'test_status': 0
        }

    def get_oids(self):
        return self.get_oids_set()['oids']

    def get_oid(self, oid_name):
        return "%s.%s" % (self.oids[oid_name], self.port)

    def check_test_status(self, status):
        if status != 1:
            self.cable_diag['error'] = u'Диагностика не поддерживается'
            raise StopDiagnostic

    def diagnostic_is_finished(self, status):
        return status != 2

    def check_errors(self, status):
        if status != 3:
            statuses = {1: u'not-run', 2: u'processing',
                        3: u'last-test-ok', 4: u'last-test-failed'}
            status_error = statuses.get(status, u'не распознан')
            self.cable_diag['error'] = u'Результат неизвестен. ' \
                                       u'Статус: %s' % status_error
            raise StopDiagnostic

    def get_result_oids(self):
        return {self.get_oid(key): key for key in
                ('port_type', 'port_status', 'test1', 'test2', 'test3',
                 'test4', 'length1', 'length2', 'length3', 'length4')}

    def process_result(self, result):

        oids = self.get_result_oids()

        table = {oids[key]: value for key, value in result.items()}
        self.cable_diag['port_type'] = {0: u'fastEthernet',
                                        1: u'gigaEthernet',
                                        2: u'other'}.get(table['port_type'])
        self.cable_diag['link_status'] = {0: u'link-down',
                                          1: u'link-up',
                                          2: u'other'}.get(table['port_status'])
        for key in ('test1', 'test2', 'test3', 'test4'):
            value = self.statuses['pair_statuses'].get(table[key])
            self.cable_diag[key] = value
        for key in ('length1', 'length2', 'length3', 'length4'):
            value = table[key]
            self.cable_diag[key] = value
        self.cable_diag['test_status'] = 1
