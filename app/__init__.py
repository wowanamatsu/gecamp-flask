from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from .controllers import home

app = Flask(__name__, template_folder='views')
app.config.from_object('config')
db = SQLAlchemy(app)

def create_app(app):

    home.configure(app)

    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    # Instancias dos modelos de dados da aplicação
    from .models.user_model import User

    manager.run()
