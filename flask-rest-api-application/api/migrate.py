from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db
from run import app

# creates an instance of flask_migrate.Migrate with the Flask app using app and db module
migrate = Migrate(app, db)
# creates a flask_script.Manager class with the Flask app as an argument
manager = Manager(app)
# calls the add_command method with 'db' and MigrateCommand as arguments
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    # calls the run method for the Manager instance
    manager.run()
