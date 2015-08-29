# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''

import sys
import time

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sys.path.append('../common')
except NameError:
    pass

from common import ALogger
from watchdog.observers import Observer
from .document_trace_handler import DocumentTraceHandler

g_observer = None


def start_watch(doc_path, doc_index_path, filter_docs):
    global g_observer
    event_handler = DocumentTraceHandler(doc_index_path, filter_docs)

    if g_observer:
        stop_watch()

    g_observer = Observer()
    g_observer.schedule(event_handler, doc_path, recursive=True)
    g_observer.start()
    ALogger.INFO("Start watchdocs..")


def stop_watch():
    global g_observer
    ALogger.INFO("Stop watchdocs..")
    g_observer.stop()
    g_observer.join()
    g_observer = None
