import os
from flask import Flask


def create_app():
    # Criando e configurando uma app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    import db
    db.init_app(app)

    @app.route('/')
    def home():
        return 'Hello, world!'

    app.run(debug=True)

    # return app

if __name__ == '__main__':
    create_app()