import os

# ref: https://stackoverflow.com/questions/27766794/switching-from-sqlite-to-mysql-with-flask-sqlalchemy
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{PORT}/{DB_NAME}".format(DB_USER='ryaan_hind', DB_PASSWORD='@ryaan#2016', DB_HOST=HOST, PORT='3306', DB_NAME='messages')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# pagination settings
PAGINATION_PAGE_SIZE = 5
PAGINATION_PAGE_ARGUMENT_NAME = 'page'
