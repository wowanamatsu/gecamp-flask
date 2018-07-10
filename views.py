
def show_urls(app):
    @app.route('/')
    def home():
        return 'Home'



def configure(app):
    pass