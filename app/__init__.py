from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from .controllers import home

app = Flask(__name__, template_folder='views')

def create_app(app):
    app.config.from_object('config')
    database = SQLAlchemy(app)

    home.configure(app)

    migrate = Migrate(app, database)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    manager.run()
