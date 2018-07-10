import views

from flask import Flask


def create_app():
    app = Flask(__name__)

    views.show_urls(app)

    app.run(debug=True)




if __name__ == '__main__':
    create_app()
