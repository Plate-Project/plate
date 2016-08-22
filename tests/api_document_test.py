# -*- coding:utf-8 -*-
try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
except NameError:
    pass

import unittest

from plate.api_document import APIDocument
from plate.common.config import Config


class ApiDocumentTestCase(unittest.TestCase):

    def setUp(self):
        basic_json = {
            "PORT": 7777,
            "TITLE": "API Document",
            "LOGO_IMG": "logo.png",
            "SEARCH_ON": True,
            "SUPPORT_LANG": ["shell", "python", "java"],
            "API_DOC_PATH": "./document",
            "API_DOC_INDEX_PATH": "index.json",
            "COPYRIGHT": "© 2015 plate",
            "FAVICON": "favicon.ico",
            "CLIPBOARD": True,
            "STATIC": {
                "DIR": "./plate_static",
                "HTML": "index.html"
            }
        }

        import json
        with open("./basic.json", 'w') as f:
            f.write(json.dumps(basic_json))
        self.basic_json_file_path = "./basic.json"

    def test_api_document_create(self):
        config = Config.load_conf(self.basic_json_file_path)

        api_document = APIDocument(config=config)
        self.assertEqual(isinstance(api_document, APIDocument), True)

        api_document.total_reload_docs()

        from collections import OrderedDict
        self.assertEqual(isinstance(api_document.toc, OrderedDict), True)

    def test_reordering(self):
        pass

    def tearDown(self):
        import os

        if os.path.exists(self.basic_json_file_path):
            os.remove(self.basic_json_file_path)