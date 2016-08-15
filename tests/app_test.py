# -*- coding:utf-8 -*-
import unittest
import json

from os import remove
from os.path import exists

from flask import Flask

from plate.app import configure_app
from plate.app import configure_blueprints
from plate.app import create_app
from plate.common.config import Config


class AppTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_app(self):
        from flask import app
        app1 = create_app(config=None)
        self.assertEqual(app1.__class__, app.Flask)

    def test_configure_app(self):

        test_conf = {'KEY': 1234, 'DB': 'localhost:3306//mc.dbo'}

        with open("./test.conf", 'w') as f:
            f.write(json.dumps(test_conf))
        config = Config.load_conf('./test.conf')
        app = Flask(__name__, static_url_path="", static_folder="static")
        configure_app(app=app, config=config)

        self.assertNotEqual(app, None)
        self.assertEqual(app.config['KEY'], 1234)
        self.assertEqual(app.config['DB'], 'localhost:3306//mc.dbo')

    def test_configure_buleprints(self):
        from flask import Flask, Blueprint
        app = Flask(__name__, static_url_path="", static_folder="static")

        page1 = Blueprint('page1', __name__, template_folder='templates')
        page2 = Blueprint('page2', __name__, template_folder='templates')
        page3 = Blueprint('page3', __name__, template_folder='templates')

        configure_blueprints(app, [page1, page2, page3])
        self.assertEqual(len(app.blueprints), 3)
        self.assertEqual(app.blueprints['page1'], page1)
        self.assertEqual(app.blueprints['page2'], page2)
        self.assertEqual(app.blueprints['page3'], page3)

    def test_start_service_server(self):
        pass
        # TODO : TESTCASE, start server and requests call page

    def test_start_test_server(self):
        pass
        # TODO : TESTCASE, start server and requests call page

    def tearDown(self):

        if exists('./test.conf'):
            remove('./test.conf')
