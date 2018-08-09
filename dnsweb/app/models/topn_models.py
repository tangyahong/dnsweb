# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, Text
from sqlalchemy.schema import FetchedValue
#  from flask_sqlalchemy import SQLAlchemy
from . import db

class AggSrcCityHourly(db.Model):
    __bind_key__ = 'dns_topn'
    __tablename__ = 'agg_src_city_hourly'

    id = db.Column(db.Integer, primary_key=True)
    source_ip_city = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

class AggSrcCityDaily(db.Model):
    __bind_key__ = 'dns_topn'
    __tablename__ = 'agg_src_city_daily'

    id = db.Column(db.Integer, primary_key=True)
    source_ip_city = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    date = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

class AggUserTypeAndCategoryHourly(db.Model):
    __bind_key__ = 'dns_topn'
    __tablename__ = 'agg_user_type_and_category_hourly'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer)
    category = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

class AggUserTypeAndCategoryDaily(db.Model):
    __bind_key__ = 'dns_topn'
    __tablename__ = 'agg_user_type_and_category_daily'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.BigInteger)
    category = db.Column(db.Text)
    date = db.Column(db.BigInteger)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    user_type_rank = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime)


class AggUserTypeAndDomainTopDaily(db.Model):
    __bind_key__ = 'dns_topn'
    __tablename__ = 'agg_user_type_and_domain_top_daily'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer)
    domain = db.Column(db.Text)
    category = db.Column(db.Text)
    website_name = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    user_type_rank = db.Column(db.Integer)
    user_type_and_category_rank = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    date = db.Column(db.Integer)


class AggUserTypeAndDomainTopHourly(db.Model):
    __bind_key__ = 'dns_topn'
    __tablename__ = 'agg_user_type_and_domain_top_hourly'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer)
    domain = db.Column(db.Text)
    category = db.Column(db.Text)
    website_name = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    category_and_user_type_rank = db.Column(db.Integer)
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class AggUserTypeAndDomainTopWeekly(db.Model):
    __bind_key__ = 'dns_topn'
    __tablename__ = 'agg_user_type_and_domain_top_weekly'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer)
    domain = db.Column(db.Text)
    category = db.Column(db.Text)
    website_name = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    category_and_user_type_rank = db.Column(db.Integer)
    year = db.Column(db.Integer)
    week = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class AggUserTypeAndWebsiteNameTopDaily(db.Model):
    __bind_key__ = 'dns_topn'
    __tablename__ = 'agg_user_type_and_website_name_top_daily'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer)
    category = db.Column(db.Text)
    website_name = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    user_type_rank = db.Column(db.Integer)
    user_type_and_category_rank = db.Column(db.Integer)
    date = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class AggUserTypeAndWebsiteNameTopHourly(db.Model):
    __bind_key__ = 'dns_topn'
    __tablename__ = 'agg_user_type_and_website_name_top_hourly'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer)
    category = db.Column(db.Text)
    website_name = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    category_rank = db.Column(db.Integer)
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class AggUserTypeAndWebsiteNameTopWeekly(db.Model):
    __bind_key__ = 'dns_topn'
    __tablename__ = 'agg_user_type_and_website_name_top_weekly'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer)
    category = db.Column(db.Text)
    website_name = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    category_rank = db.Column(db.Integer)
    year = db.Column(db.Integer)
    week = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

class AggUserTypeHourly(db.Model):
    __bind_key__ = 'dns_topn'
    __tablename__ = 'agg_user_type_hourly'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

class AggUserTypeDaily(db.Model):
    __bind_key__ = 'dns_topn'
    __tablename__ = 'agg_user_type_daily'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    date = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
