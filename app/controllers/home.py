from flask import render_template

def configure(app):
    @app.route('/')
    def index():
        return render_template('home/index.html')

    @app.route('/sobre')
    def sobre():
    	return render_template('home/sobre.html')