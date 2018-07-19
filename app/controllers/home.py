from flask import render_template

def configure(app):
    @app.route('/')
    def index():
        return render_template('home/index.html')