from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, Session
from config import mysql

engine = create_engine('mysql://{user}:{password}@{host}:{port}/{db}'.format(**mysql))
Base = declarative_base()


class Customer(Base):
    # __tablename__ = 'customer'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    customer_id = Column(String(255), nullable=False, index=True)
    username = Column(String(255), index=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    customer = relationship('Identify', backref='customer', lazy='dynamic')

    def __repr__(self):
        return '<Customer %s>' % self.username

    @classmethod
    def get_by_username(cls, username):
        query = Customer(username=username)
        if len(query) > 0:
            return query[0]
        return None


# class Identify(Base):
#     id = Column(Integer, autoincrement=True, primary_key=True, index=True)
#     birthday = Column(String(255))
#     gender = Column(String(255))
#     address = Column(String(255))
#     identify = ForeignKey(Integer, Customer.id)
#
#     def __repr__(self):
#         return '<Identify %s>' % self.birthday


Base.metadata.create_all(engine)
session = Session(bind=engine)
