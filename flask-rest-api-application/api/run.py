from app import create_app

# set up a Flask app with this module as the configuration file
app = create_app('config')

# start the Flask application with the host, port and debug values read from the config module
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])

