# -*- coding:utf-8 -*-
import unittest

from plate.app import configure_app
from plate.app import configure_blueprints
from plate.app import start_test_server
from plate.app import start_service_server

import requests

class AppTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_configure_app(self):

        test_conf = {'KEY': 1234, 'db': 'localhost:3306//mc.dbo'}
        import json
        with open("./test.conf", 'w') as f:
            f.write(json.dumps(test_conf))

        from flask import Flask
        from plate.common.config import Config
        config = Config.load_conf('./test.conf')
        app = Flask(__name__, static_url_path="", static_folder="static")
        configure_app(app=app, config=config)

        self.assertNotEqual(app, None)
        self.assertEqual(app.config['KEY'], 1234)
        self.assertEqual(app.config['db'], 'localhost:3306//mc.dbo')

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

    def test_start_test_server(self):
        from flask import Flask
        app = Flask(__name__, static_url_path="", static_folder="static")

        start_test_server(app)
        r = requests.get('http://localhost:5000')
        self.assertEqual(r.status_code, 200)

    def test_start_service_server(self):
        from flask import Flask
        app = Flask(__name__, static_url_path="", static_folder="static")

        start_service_server(app)
        r = requests.get('http://localhost:8080')
        self.assertEqual(r.status_code, 200)

    def tearDown(self):
        from os.path import exists
        from os import remove

        if exists('./test.conf'):
            remove('./test.conf')
