# -*- coding:utf-8 -*-
import unittest

from watchdog.events import FileModifiedEvent

from plate.watchdocs.document_trace_queue import DocumentTraceQueue


class DocumentTraceQueueTestCase(unittest.TestCase):

    def setUp(self):
        self.docq = DocumentTraceQueue()

        if self.docq:
            self.docq.clear()

        event = FileModifiedEvent("./")
        self.docq.enqueue(event=event, is_index_file=True)

    def test_is_empty(self):
        self.assertEqual(self.docq.is_empty(), False)
        self.docq.clear()
        self.assertEqual(self.docq.is_empty(), True)

    def count(self):
        self.assertEqual(self.docq.count(), 1)
        event = FileModifiedEvent("./")
        self.docq.enqueue(event=event, is_index_file=False)
        self.assertEqual(self.docq.count(), 2)

    def test_clear(self):
        self.docq.clear()
        self.assertEqual(self.docq.count(), 0)

    def test_enqueue(self):
        event = FileModifiedEvent("./")
        self.docq.enqueue(event=event, is_index_file=False)
        self.assertEqual(self.docq.count(), 2)

        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", None))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", 1))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", "test"))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", True))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", []))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", {}))

        with self.assertRaises(TypeError):
            self.docq.enqueue(event="TEST", is_index_file=True)

    def test_dequeue(self):
        t = self.docq.dequeue()
        self.assertEqual(isinstance(t[0], FileModifiedEvent), True)
        self.assertEqual(t[1], True)
        self.assertEqual(self.docq.count(), 0)
        self.assertEqual(self.docq.dequeue(), None)

