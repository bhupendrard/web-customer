from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import db, login, app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
"""

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    phone = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    zipcode= db.Column(db.String(64))
    state = db.Column(db.String(64))
    activity = db.Column(db.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'],expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s=Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    phone = db.Column(db.String(10), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    fname = db.Column(db.String(64), index=True, unique=False)
    lname = db.Column(db.String(64), index=True, unique=False)
    gender = db.Column(db.Integer)
    address = db.Column(db.String(64))
    state = db.Column(db.String(2))
    city = db.Column(db.String(64))
    zip = db.Column(db.String(5))
    score = db.Column(db.Integer, index=True, unique=False)

    def __repr__(self):
        return '<Customer {}>'.format(self.username)
