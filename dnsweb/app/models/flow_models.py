# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, Text
from sqlalchemy.schema import FetchedValue
#  from flask_sqlalchemy import SQLAlchemy
from . import db

class AggSrcCityAndDstCityAndDstOperatorDaily(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_src_city_and_dst_city_and_dst_operator_daily'

    id = db.Column(db.Integer, primary_key=True)
    source_ip_city = db.Column(db.Text)
    resolved_ip_city = db.Column(db.Text)
    resolved_ip_operator = db.Column(db.Text)
    resolved_ip_province = db.Column(db.Text)
    resolved_ip_country = db.Column(db.Text)
    date = db.Column(db.BigInteger)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime)


class AggSrcCityAndDstCityAndDstOperatorHourly(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_src_city_and_dst_city_and_dst_operator_hourly'

    id = db.Column(db.Integer, primary_key=True)
    source_ip_city = db.Column(db.Text)
    resolved_ip_city = db.Column(db.Text)
    resolved_ip_operator = db.Column(db.Text)
    resolved_ip_country = db.Column(db.Text)
    resolved_ip_province = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())