import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir, 'app.db')