from flask import Flask


def create_app(config_filename):
    # creates the main entry point for the Flask application named app
    app = Flask(__name__)
    # set ups a Flask app with this configuration file, and returns the app object
    app.config.from_object(config_filename)

    # initilize the flask_sqlalchemy.SQLAlchemy instance created in the models module named db
    # and link the created Flask app with the SQLAlchemy instance
    from models import db
    db.init_app(app)

    # Registering the blueprint created in the views module, named api_bp
    from views import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
