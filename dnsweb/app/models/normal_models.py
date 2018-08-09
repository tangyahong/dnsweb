# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, Text
from sqlalchemy.schema import FetchedValue
from . import db

class DimFocusedDomain(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'dim_focused_domain'

    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255))
    tld_plus_two = db.Column(db.String(255))
    tld_plus_one = db.Column(db.String(255))
    like_pattern = db.Column(db.String(255))
    regexp_pattern = db.Column(db.String(255))
    is_focused = db.Column(db.SmallInteger)
    category = db.Column(db.String(255))
    website_name = db.Column(db.String(255))
    comment = db.Column(db.String(255))
