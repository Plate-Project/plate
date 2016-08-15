# -*- coding:utf-8 -*-
import unittest

from plate.common.config import Config


class ConfigTestCase(unittest.TestCase):

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

        default_json = {}
        with open("./default.json", 'w') as f:
            f.write(json.dumps(default_json))
        self.default_json_file_path = "./default.json"
        self.not_exist_json_file_path = "./t.json"

    def test_default_json_file(self):
        config = Config.load_conf(self.default_json_file_path)
        self.assertEqual(config.exist("test"), False)
        self.assertEqual(config.exist(1), False)
        self.assertEqual(config.exist(True), False)

    def test_not_exsit_json_file(self):
        self.assertRaises(Exception, Config.load_conf, (self.not_exist_json_file_path))

    def test_basic_json_file(self):
        config = Config.load_conf(self.basic_json_file_path)

        self.assertEqual(config.PORT, 7777)
        self.assertEqual(config.TITLE, "API Document")
        self.assertEqual(config.STATIC.DIR, "./plate_static")
        self.assertEqual(config.SUPPORT_LANG, ["shell", "python", "java"])

    def test_config_repr(self):
        config = Config.load_conf(self.basic_json_file_path)
        self.assertEqual( isinstance(config.__repr__(), str), True)

    def test_config_exist(self):
        config = Config.load_conf(self.basic_json_file_path)
        self.assertEqual(config.exist('TITLE'), True)
        self.assertEqual(config.exist('STATIC'), True)
        self.assertEqual(config.exist('SUPPORT_LANG'), True)

    def tearDown(self):
        import os

        if os.path.exists(self.default_json_file_path):
            os.remove(self.default_json_file_path)

        if os.path.exists(self.basic_json_file_path):
            os.remove(self.basic_json_file_path)

        if os.path.exists(self.not_exist_json_file_path):
            os.remove(self.not_exist_json_file_path)