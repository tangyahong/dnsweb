# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, Text
from sqlalchemy.schema import FetchedValue
#  from flask_sqlalchemy import SQLAlchemy
from . import db


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    role = db.Column(db.Integer)
    name = db.Column(db.String(50))
    login_time = db.Column(db.DateTime())
    department = db.Column(db.String(20))

class Privilege(db.Model):
    __tablename__ = 'privilege'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    privilege_id = db.Column(db.Integer)

class Privilege_Map(db.Model):
    __tablename__ = 'privilege_map'
    id = db.Column(db.Integer, primary_key=True)
    privilege_name = db.Column(db.String(255))
    path = db.Column(db.String(255))
    component = db.Column(db.String(255))

