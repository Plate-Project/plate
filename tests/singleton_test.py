# -*- coding:utf-8 -*-

import unittest

from plate.api_document import APIDocument
from plate.watchdocs.api_document_observer import APIDocumentObserver
from plate.watchdocs.document_trace_queue import DocumentTraceQueue


class SingletonClassTestCase(unittest.TestCase):

    def test_api_document_observer_singleton(self):
        observer1 = APIDocumentObserver(doc_path="./")
        observer2 = APIDocumentObserver(doc_path="./")
        self.assertEqual(hex(id(observer1)), hex(id(observer2)))

    def test_document_trace_queue_singleton(self):
        queue1 = DocumentTraceQueue()
        queue2 = DocumentTraceQueue()
        self.assertEqual(hex(id(queue1)), hex(id(queue2)))

