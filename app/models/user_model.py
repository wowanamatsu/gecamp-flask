from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    passowrd = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    @property
    def is_authenticated(self): return True

    @property
    def is_activated(self): return True

    @property
    def is_anonymous(self): return False

    def get_id(self): return str(self.id)



    def __init__(self, user_name, password):
        self.username = user_name
        self.passowrd = password

    def __repr__(self):
        return 'Nome: {}'.format(self.username)