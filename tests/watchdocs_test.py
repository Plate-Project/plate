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

    def setUp(self):

        self.tracing_files = []

        for i in range(0, 10):
            file_path = "./" + str(i) + "_test.txt"
            with open(file_path, "w") as f:
                f.write(str(i))
                self.tracing_files.append(file_path)

        self.document_handler = DocumentTraceHandler(tracing_files=self.tracing_files)

    def test_on_modified(self):
        print "test"

    def test_is_index_file(self):
        pass

    def tearDown(self):
        from os import remove
        from os.path import exists
        for f in self.tracing_files:
            if exists(f):
                remove(f)


class APIDocumentObserverTestCase(unittest.TestCase):
    pass
