from config import mysql
from portal import app
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{user}:{password}@{host}:{port}/{db}'.format(**mysql)
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 5
db = SQLAlchemy(app)


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, index=True)
    customer_id = db.Column(db.String(255), nullable=False, index=True)
    username = db.Column(db.String(255), index=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    customer = db.relationship('Identify', backref='customer', lazy='dynamic')

    def __repr__(self):
        return '<Customer %s>' % self.username

    @classmethod
    def get_by_username(cls, username):
        query = Customer(username=username)
        if len(query) > 0:
            return query[0]
        return None


class Identify(db.Model):
    __tablename__ = 'identify'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, index=True)
    birthday = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    address = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __repr__(self):
        return '<Identify %s>' % self.birthday


db.create_all()
