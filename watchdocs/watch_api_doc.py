# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sys.path.append('../common')
except NameError:
    pass

from common import ALogger
from watchdog.observers import Observer


_g_observer = None

# todo : CONVERT TO CLASS


def start_watch(doc_path, doc_index_path, filter_docs):
    global _g_observer

    from .document_trace_handler import DocumentTraceHandler
    event_handler = DocumentTraceHandler(doc_index_path, filter_docs)

    if _g_observer:
        stop_watch()

    _g_observer = Observer()
    _g_observer.schedule(event_handler, doc_path, recursive=True)
    _g_observer.start()
    ALogger.INFO("Start watchdocs..")


def stop_watch():
    global _g_observer
    _g_observer.INFO("Stop watchdocs..")
    _g_observer.stop()
    _g_observer.join()
    _g_observer = None
