import os
import shutil
import tempfile
import unittest

from blueberrypy.project import create_project

class CreateProjectTest(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def test_create_project(self):

        blueberrypy_config = {'author': 'Jimmy Wong',
                              'current_year': 2012,
                              'driver': 'pysqlite',
                              'path': self.tmpdir,
                              'email': 'abc@example.com',
                              'package': 'blueberrytest',
                              'project_name': 'blueberrytest',
                              'sqlalchemy_url': 'sqlite://',
                              'use_controller': True,
                              'use_jinja2': True,
                              'use_redis': True,
                              'use_rest_controller': True,
                              'use_sqlalchemy': True,
                              'use_webassets': True,
                              'version': '0.1'}

        create_project(blueberrypy_config)

        paths = ['',
                 '.cache',
                 'config',
                 'config/dev',
                 'config/dev/app.yml',
                 'config/dev/bundles.yml',
                 'config/dev/logging.yml',
                 'config/prod',
                 'config/prod/app.yml',
                 'config/prod/bundles.yml',
                 'config/prod/logging.yml',
                 'config/test',
                 'config/test/test.yml',
                 'log',
                 'setup.py',
                 'src',
                 'src/blueberrytest',
                 'src/blueberrytest/__init__.py',
                 'src/blueberrytest/api.py',
                 'src/blueberrytest/controller.py',
                 'src/blueberrytest/model.py',
                 'src/blueberrytest/rest_api.py',
                 'src/blueberrytest/rest_controller.py',
                 'src/blueberrytest/template',
                 'src/blueberrytest/template/404.html',
                 'src/blueberrytest/template/base.html',
                 'src/blueberrytest/template/index.html',
                 'src/tests',
                 'src/tests/__init__.py',
                 'src/tests/helper.py',
                 'src/tests/test_api.py',
                 'src/tests/test_controller.py',
                 'src/tests/test_model.py',
                 'src/tests/test_rest_api.py',
                 'src/tests/test_rest_controller.py',
                 'static',
                 'static/css',
                 'static/css/screen.css',
                 'static/favicon.ico',
                 'static/img',
                 'static/js']

        for path in paths:
            self.assertTrue(os.path.exists(os.path.join(self.tmpdir, path)))
