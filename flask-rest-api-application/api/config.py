import os

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{PORT}/{DB_NAME}".format(DB_USER='root',DB_PASSWORD='sqlr00t',DB_HOST='127.0.0.1', PORT='3306',DB_NAME='messages')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
