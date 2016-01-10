# -*- coding:utf-8 -*-

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sys.path.append('../common')
except NameError:
    pass

from common import logger
from watchdog.observers import Observer

_g_observer = None


def start_watch(doc_path, doc_index_path, filter_docs):
    """
    Start watch docs

    :param doc_path: API Document Directory path
    :param doc_index_path: API Document index path
    :param filter_docs: Document file list ``ORDER`` in ``index.json``

    """
    global _g_observer

    from .document_trace_handler import DocumentTraceHandler
    event_handler = DocumentTraceHandler(doc_index_path, filter_docs)

    if _g_observer:
        stop_watch()

    _g_observer = Observer()
    _g_observer.schedule(event_handler, doc_path, recursive=True)
    _g_observer.start()
    logger.info("Start watchdocs..")


def stop_watch():
    """
    Stop watch docs
    """
    global _g_observer
    _g_observer.stop()
    _g_observer.join()
    _g_observer = None
    logger.info("Stop watchdocs..")
