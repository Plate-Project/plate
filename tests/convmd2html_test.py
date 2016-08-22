# -*- coding:utf-8 -*-
import unittest

from plate.common.convmd2html import convert_md_to_html


class ConvMd2HtmlTestCase(unittest.TestCase):

    def test_convert_md_to_html(self):
        self.assertEqual(convert_md_to_html(md_text="#test#"), "<h1>test</h1>")
        self.assertEqual(convert_md_to_html(md_text="##test##"), "<h2>test</h2>")
        self.assertEqual(convert_md_to_html(md_text="###test###"), "<h3>test</h3>")

        with self.assertRaises(Exception):
            convert_md_to_html(md_text=2)
