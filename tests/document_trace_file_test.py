# -*- coding:utf-8 -*-
import unittest

from plate.watchdocs.document_trace_file import DocumentTraceFile


class DocumentTraceFileTestCase(unittest.TestCase):

    def test(self):
        with self.assertRaises(Exception):
            DocumentTraceFile(tracing_file_path=None)
