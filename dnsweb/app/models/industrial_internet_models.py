# from flask_sqlalchemy import SQLAlchemy
# from IPy import IP

# db = SQLAlchemy()

# # from app.models import db

# def to_dict(self):
#     return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
# db.Model.to_dict = to_dict

# def session_commit():
#     try:
#         db.session.commit()
#     except Exception as e:
#         db.session.rollback()
#         reason = str(e)
#         return reason

# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, Integer, Text
from sqlalchemy.schema import FetchedValue
#  from flask_sqlalchemy import SQLAlchemy
from . import db

# db = SQLAlchemy()

# def to_dict(self):
#     return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
# db.Model.to_dict = to_dict



class AggIsFocusedDomainCategoryDaily(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_is_focused_domain_category_daily'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    category = db.Column(db.Text)
    date = db.Column(db.BigInteger)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime)


class AggIsFocusedDomainCategoryHourly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_is_focused_domain_category_hourly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    category = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class AggIsFocusedDomainCategoryMonthly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_is_focused_domain_category_monthly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    category = db.Column(db.Text)
    date = db.Column(db.BigInteger)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    update_time = db.Column(db.DateTime)
    year = db.Column(db.BigInteger)
    month = db.Column(db.BigInteger)


class AggIsFocusedDomainCategoryWeekly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_is_focused_domain_category_weekly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    category = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    year = db.Column(db.BigInteger)
    week = db.Column(db.BigInteger)
    # update_time = db.Column(db.DateTime)


class AggIsFocusedDomainDaily(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_is_focused_domain_daily'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    domain = db.Column(db.Text)
    category = db.Column(db.Text)
    website_name = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    category_rank = db.Column(db.Integer)
    date = db.Column(db.BigInteger)
    # update_time = db.Column(db.DateTime)


class AggIsFocusedDomainHourly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_is_focused_domain_hourly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    domain = db.Column(db.Text)
    category = db.Column(db.Text)
    website_name = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class AggIsFocusedDomainMonthly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_is_focused_domain_monthly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    domain = db.Column(db.Text)
    category = db.Column(db.Text)
    date = db.Column(db.BigInteger)
    website_name = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    category_rank = db.Column(db.Integer)
    update_time = db.Column(db.DateTime)
    year = db.Column(db.BigInteger)
    month = db.Column(db.BigInteger)


class AggIsFocusedDomainWeekly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_is_focused_domain_weekly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    domain = db.Column(db.Text)
    category = db.Column(db.Text)
    website_name = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    category_rank = db.Column(db.Integer)
    year = db.Column(db.BigInteger)
    week = db.Column(db.BigInteger)
    # update_time = db.Column(db.DateTime)


class AggSubscriberCityAndResolvedIpNetworkDaily(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_subscriber_city_and_resolved_ip_network_daily'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subscriber_city = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    date = db.Column(db.BigInteger)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    resolved_ip_network_rank = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime)


class AggSubscriberCityAndResolvedIpNetworkHourly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_subscriber_city_and_resolved_ip_network_hourly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subscriber_city = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class AggSubscriberCityAndResolvedIpNetworkMonthly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_subscriber_city_and_resolved_ip_network_monthly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subscriber_city = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    date = db.Column(db.BigInteger)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    resolved_ip_network_rank = db.Column(db.Integer)
    update_time = db.Column(db.DateTime)
    year = db.Column(db.BigInteger)
    month = db.Column(db.BigInteger)


class AggSubscriberCityAndResolvedIpNetworkWeekly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_subscriber_city_and_resolved_ip_network_weekly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subscriber_city = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    resolved_ip_network_rank = db.Column(db.Integer)
    year = db.Column(db.BigInteger)
    week = db.Column(db.BigInteger)
    # update_time = db.Column(db.DateTime)


class AggSubscriberNameAndResolvedIpNetworkDaily(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_subscriber_name_and_resolved_ip_network_daily'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subscriber_name = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    subscriber_organization = db.Column(db.Text)
    subscriber_city = db.Column(db.Text)
    date = db.Column(db.BigInteger)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    resolved_ip_network_rank = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime)


class AggSubscriberNameAndResolvedIpNetworkHourly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_subscriber_name_and_resolved_ip_network_hourly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subscriber_name = db.Column(db.Text)
    subscriber_city = db.Column(db.Text)
    subscriber_organization = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class AggSubscriberNameAndResolvedIpNetworkMonthly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_subscriber_name_and_resolved_ip_network_monthly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subscriber_name = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    date = db.Column(db.BigInteger)
    subscriber_city = db.Column(db.Text)
    subscriber_organization = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    resolved_ip_network_rank = db.Column(db.Integer)
    update_time = db.Column(db.DateTime)
    year = db.Column(db.BigInteger)
    month = db.Column(db.BigInteger)


class AggSubscriberNameAndResolvedIpNetworkWeekly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_subscriber_name_and_resolved_ip_network_weekly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subscriber_name = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    subscriber_organization = db.Column(db.Text)
    subscriber_city = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    resolved_ip_network_rank = db.Column(db.Integer)
    year = db.Column(db.BigInteger)
    week = db.Column(db.BigInteger)
    # update_time = db.Column(db.DateTime)


class AggSubscriberOrganizationAndResolvedIpNetworkDaily(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_subscriber_organization_and_resolved_ip_network_daily'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subscriber_organization = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    date = db.Column(db.BigInteger)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    resolved_ip_network_rank = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime)


class AggSubscriberOrganizationAndResolvedIpNetworkHourly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_subscriber_organization_and_resolved_ip_network_hourly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subscriber_organization = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class AggSubscriberOrganizationAndResolvedIpNetworkMonthly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_subscriber_organization_and_resolved_ip_network_monthly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subscriber_organization = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    date = db.Column(db.BigInteger)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    resolved_ip_network_rank = db.Column(db.Integer)
    update_time = db.Column(db.DateTime)
    year = db.Column(db.BigInteger)
    month = db.Column(db.BigInteger)


class AggSubscriberOrganizationAndResolvedIpNetworkWeekly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_subscriber_organization_and_resolved_ip_network_weekly'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    subscriber_organization = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    resolved_ip_network_rank = db.Column(db.Integer)
    year = db.Column(db.BigInteger)
    week = db.Column(db.BigInteger)
    # update_time = db.Column(db.DateTime)


class AggUserTypeAndResolvedIpNetworkDaily(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_user_type_and_resolved_ip_network_daily'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.BigInteger)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    user_type_rank = db.Column(db.Integer)
    update_time = db.Column(db.DateTime)
    date = db.Column(db.BigInteger)


class AggUserTypeAndResolvedIpNetworkHourly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_user_type_and_resolved_ip_network_hourly'

    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.Integer)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())

class AggUserTypeAndResolvedIpNetworkWeekly(db.Model):
    __bind_key__ = 'dns_zx'
    __tablename__ = 'agg_user_type_and_resolved_ip_network_weekly'

    id = db.Column(db.BigInteger, primary_key=True)
    user_type = db.Column(db.BigInteger)
    resolved_ip_network = db.Column(db.Text)
    user_type_rank = db.Column(db.Integer)
    resolved_number = db.Column(db.BigInteger)
    success_number = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float(asdecimal=True))
    rank = db.Column(db.Integer)
    update_time = db.Column(db.DateTime)
    year = db.Column(db.BigInteger)
    week = db.Column(db.BigInteger)
