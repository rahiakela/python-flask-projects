import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#  basedir pointing to the directory the program is running in
basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance and give it the path to the swagger.yml file.
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance initialized by Connexion
app = connex_app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True  # echo SQL statements it executes to the console
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'people.db')  # use SQLite as the database, and a file named people.db in the current directory as the database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # turning off the SQLAlchemy event system, which is on by default

# Create the SQLAlchemy db instance by passing the app configuration information just set
db = SQLAlchemy(app)

# Initialize Marshmallow and allows it to introspect the SQLAlchemy components attached to the app
ma = Marshmallow(app)
