# -*- coding:utf-8 -*-
import unittest

from plate.watchdocs import DocumentTraceQueue
from plate.watchdocs import DocumentTraceHandler
from plate.watchdocs import APIDocumentObserver

class DocumentTraceQueueTestCase(unittest.TestCase):

    def setUp(self):
        self.docq = DocumentTraceQueue()

        if self.docq:
            self.docq.clear()
        self.docq.enqueue(event="Test", is_index_file=True)

    def test_is_empty(self):
        self.assertEqual(self.docq.is_empty(), False)
        self.docq.clear()
        self.assertEqual(self.docq.is_empty(), True)

    def count(self):
        self.assertEqual(self.docq.count(), 1)
        self.docq.enqueue(event="Test", is_index_file=False)
        self.assertEqual(self.docq.count(), 2)

    def test_clear(self):
        self.docq.clear()
        self.assertEqual(self.docq.count(), 0)

    def test_enqueue(self):
        self.docq.enqueue(event="Test3", is_index_file=False)
        self.assertEqual(self.docq.count(), 2)

        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", None))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", 1))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", "test"))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", True))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", []))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", {}))

    def test_dequeue(self):
        t = self.docq.dequeue()
        self.assertEqual(t[0], "Test")
        self.assertEqual(t[1], True)
        self.assertEqual(self.docq.count(), 0)


class DocumentTraceHandlerTestCase(unittest.TestCase):
    pass


class APIDocumentObserverTestCase(unittest.TestCase):
    pass
