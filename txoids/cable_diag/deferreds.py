# -*- coding: utf-8 -*-
from twisted.internet import defer
from twisted.python import log

from txoids.generic.deferreds import BaseAction
from txoids.cable_diag.processors import CableDiagProcessor, \
    StopDiagnostic

from txoids.utils import deferredSleep


class CableDiag(BaseAction):

    def __init__(self, parser, port):
        super(CableDiag, self).__init__(parser)
        self.port = port

    def get_deferred(self):
        return self.cable_diag()

    @defer.inlineCallbacks
    def cable_diag(self):
        processor = CableDiagProcessor(self.parser, self.port)

        oid = processor.get_oid('set')
        oids = [(oid, 'i', '1')]
        set_proxy = self.get_open_proxy(
            community=self.parser.community_write, tries=1
        )
        read_proxy = self.get_open_proxy()

        d = set_proxy.set(oids, **self.proxy_settings)
        try:
            result = yield d
            status = result.get(oid)
            processor.check_test_status(status)

            # Проверяем, что диагностики завершена
            for _ in xrange(20):
                yield deferredSleep(0.5)
                oids = [processor.get_oid('check')]
                result = yield read_proxy.get(oids, **self.proxy_settings)
                status = result.get(oids[0])
                if processor.diagnostic_is_finished(status):
                    break

            processor.check_errors(status)

            # Получаем результаты диагностики
            oids = processor.get_result_oids()
            result = yield read_proxy.get(oids.keys(), **self.proxy_settings)
            processor.process_result(result)
        except StopDiagnostic:
            pass
        except Exception as exc:
            log.err(exc)
        finally:
            read_proxy.close()
            set_proxy.close()
            defer.returnValue(processor.cable_diag)
