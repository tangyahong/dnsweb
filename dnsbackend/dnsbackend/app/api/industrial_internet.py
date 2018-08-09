from flask import jsonify, request, g
from app.models.models import *
from . import api
from .. import common
import datetime
from .. import geo
import json
from functools import wraps
from IPy import IP
from app.api.decorator import *
from app.models import db
from app.models.industrial_internet_models import *

# 企业指数详情-某日用户公有云访问量排名（10）
# agg_subscriber_name_and_resolved_ip_network_daily
@api.route('/dns/get-enterprise-index-detail-daily', methods=['POST'])
def getEnterpriseIndexDetailDaily():
	date = request.get_json()['date']
	query = db.session.query(AggSubscriberNameAndResolvedIpNetworkDaily.subscriber_name,
		AggSubscriberNameAndResolvedIpNetworkDaily.resolved_number).filter_by(date=date)\
		.order_by(db.desc(AggSubscriberNameAndResolvedIpNetworkDaily.resolved_number))\
		.filter_by(resolved_ip_network='公有云').limit(10)
	db.session.remove()
	subscriber_name = []
	resolved_number = []
	for item in query:
		subscriber_name.append(item[0])
		resolved_number.append(int(item[1]))
	result_dict = {"subscriber_name": subscriber_name, "resolved_number": resolved_number}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 企业指数详情-过去一周用户公有云访问量排名（10）
# agg_subscriber_name_and_resolved_ip_network_weekly
@api.route('/dns/get-enterprise-index-detail-weekly', methods=['GET'])
def getEnterpriseIndexDetailWeekly():
	year = 2018
	week = 12
	query = db.session.query(AggSubscriberNameAndResolvedIpNetworkWeekly.subscriber_name,
		AggSubscriberNameAndResolvedIpNetworkWeekly.resolved_number).filter_by(year=year).filter_by(week=week)\
		.order_by(db.desc(AggSubscriberNameAndResolvedIpNetworkWeekly.resolved_number))\
		.filter_by(resolved_ip_network='公有云').limit(10)
	db.session.remove()
	subscriber_name = []
	resolved_number = []
	for item in query:
		subscriber_name.append(item[0])
		resolved_number.append(int(item[1]))
	result_dict = {"year": year, "week": week, "subscriber_name": subscriber_name, "resolved_number": resolved_number}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 平台指数详情
# agg_user_type_and_resolved_ip_network_daily
@api.route('/dns/get-platform-index-detail-daily', methods=['POST'])
def getPlatformIndexDetailDaily():
	date = request.get_json()['date']
	query = db.session.query(AggUserTypeAndResolvedIpNetworkDaily.resolved_ip_network,
		AggUserTypeAndResolvedIpNetworkDaily.resolved_number).filter_by(user_type=0)\
		.filter_by(date=date).filter(AggUserTypeAndResolvedIpNetworkDaily.resolved_ip_network != '公有云').all()
	name_list = []
	value_list = []
	for item in query:
		name_list.append(item[0])
		value_list.append({"name": item[0], "value": int(item[1])})
	result_dict = {"name": name_list, "value": value_list}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 平台指数详情
# agg_user_type_and_resolved_ip_network_weekly
@api.route('/dns/get-platform-index-detail-weekly', methods=['GET'])
def getPlatformIndexDetailWeekly():
	year = 2018
	week = 12
	query = db.session.query(AggUserTypeAndResolvedIpNetworkWeekly.resolved_ip_network,
		AggUserTypeAndResolvedIpNetworkWeekly.resolved_number).filter_by(year=year).filter_by(week=week)\
		.filter_by(user_type=0).filter(AggUserTypeAndResolvedIpNetworkWeekly.resolved_ip_network != '公有云').all()
	db.session.remove()
	name_list = []
	value_list = []
	for item in query:
		name_list.append(item[0])
		value_list.append({"name": item[0], "value": int(item[1])})
	result_dict = {"year": year, "week": week, "name": name_list, "value": value_list}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 示范基地指数详情
# agg_subscriber_organization_and_resolved_ip_network_daily
@api.route('/dns/get-demonstration-bases-index-detail-daily', methods=['POST'])
def getDemonstrationBasesIndexDetailDaily():
	date = request.get_json()['date']
	query = db.session.query(AggSubscriberOrganizationAndResolvedIpNetworkDaily.subscriber_organization,
		AggSubscriberOrganizationAndResolvedIpNetworkDaily.resolved_number)\
		.filter_by(date=date).filter_by(resolved_ip_network='公有云').all()
	db.session.remove()
	name_list = []
	value_list = []
	for item in query:
		name_list.append(item[0])
		value_list.append({"name": item[0], "value": int(item[1])})
	result_dict = {"name": name_list, "value": value_list}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 示范基地指数详情
# agg_subscriber_organization_and_resolved_ip_network_weekly
@api.route('/dns/get-demonstration-bases-index-detail-weekly', methods=['GET'])
def getDemonstrationBasesIndexDetailWeekly():
	year = 2018
	week = 12
	query = db.session.query(AggSubscriberOrganizationAndResolvedIpNetworkWeekly.subscriber_organization,
		AggSubscriberOrganizationAndResolvedIpNetworkWeekly.resolved_number)\
		.filter_by(year=year).filter_by(week=week).filter_by(resolved_ip_network='公有云').all()
	db.session.remove()
	name_list = []
	value_list = []
	for item in query:
		name_list.append(item[0])
		value_list.append({"name": item[0], "value": int(item[1])})
	result_dict = {"year": year, "week": week, "name": name_list, "value": value_list}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 应用服务指数详情
# agg_is_focused_domain_category_daily
@api.route('/dns/get-application-service-index-detail-daily', methods=['POST'])
def getApplicationServiceIndexDetailDaily():
	date = request.get_json()['date']
	query = db.session.query(AggIsFocusedDomainCategoryDaily.category,
		AggIsFocusedDomainCategoryDaily.resolved_number)\
		.filter_by(date=date).all()
	db.session.remove()
	name_list = []
	value_list = []
	for item in query:
		name_list.append(item[0])
		value_list.append({"name": item[0], "value": int(item[1])})
	result_dict = {"name": name_list, "value": value_list}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 应用服务指数详情
# agg_is_focused_domain_category_weekly
@api.route('/dns/get-application-service-index-detail-weekly', methods=['GET'])
def getAggIsFocusedDomainCategoryWeekly():
	year = 2018
	week = 12
	query = db.session.query(AggIsFocusedDomainCategoryWeekly.category,
		AggIsFocusedDomainCategoryWeekly.resolved_number).filter_by(year=year).filter_by(week=week).all()
	db.session.remove()
	name_list = []
	value_list = []
	for item in query:
		name_list.append(item[0])
		value_list.append({"name": item[0], "value": int(item[1])})
	result_dict = {"year": year, "week": week, "name": name_list, "value": value_list}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 金融服务指数详情
# agg_is_focused_domain_daily
# category = "供应链平台" and sum resolved_number
@api.route('/dns/get-financial-service-index-detail-daily', methods=['POST'])
def getFinancialServiceIndexDetailDaily():
	date = request.get_json()['date']
	query = db.session.query(AggIsFocusedDomainDaily.domain,
		AggIsFocusedDomainDaily.website_name,
		AggIsFocusedDomainDaily.resolved_number)\
		.filter_by(category="供应链平台")\
		.filter_by(date=date).all()
	db.session.remove()
	name_list = []
	value_list = []
	for item in query:
		name_list.append(item[1])
		value_list.append({"name": item[1], "value": int(item[2])})
	result_dict = {"name": name_list, "value": value_list}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)


# 金融服务指数详情
# agg_is_focused_domain_weekly
# category = "供应链平台" and sum resolved_number
@api.route('/dns/get-financial-service-index-detail-weekly', methods=['GET'])
def getFinancialServiceIndexDetailWeekly():
	year = 2018
	week = 12
	query = db.session.query(AggIsFocusedDomainWeekly.domain,
		AggIsFocusedDomainWeekly.website_name,
		AggIsFocusedDomainWeekly.resolved_number)\
		.filter_by(category="供应链平台")\
		.filter_by(year=year).filter_by(week=week).all()
	db.session.remove()
	name_list = []
	value_list = []
	for item in query:
		name_list.append(item[1])
		value_list.append({"name": item[1], "value": int(item[2])})
	result_dict = {"year": year, "week": week, "name": name_list, "value": value_list}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)


# 企业指数折线图
# agg_subscriber_name_and_resolved_ip_network_daily
# resolved_ip_network= "公有云" && sum resolved_number group by date
@api.route('/dns/get-enterprise-index', methods=['GET'])
def getEnterpriseIndex():
	query = db.session.query(AggSubscriberNameAndResolvedIpNetworkDaily.date,
		db.func.sum(AggSubscriberNameAndResolvedIpNetworkDaily.resolved_number)).filter_by(resolved_ip_network='公有云')\
		.group_by(AggSubscriberNameAndResolvedIpNetworkDaily.date).order_by(db.desc(AggSubscriberNameAndResolvedIpNetworkDaily.date)).limit(7)
	db.session.remove()
	date = []
	resolved_number = []
	for item in query:
		date.append(item[0])
		resolved_number.append(int(item[1]))
	date.reverse()
	resolved_number.reverse()
	result_dict = {"date": date, "resolved_number": resolved_number}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 平台指数折线图
# agg_user_type_and_resolved_ip_network_daily
# user_type = 0 and resolved_ip_network = "公有云"
@api.route('/dns/get-platform-index', methods=['GET'])
def getPlatformIndex():
	query = db.session.query(AggUserTypeAndResolvedIpNetworkDaily.date, AggUserTypeAndResolvedIpNetworkDaily.resolved_number)\
		.filter_by(user_type=0).filter_by(resolved_ip_network='公有云').order_by(db.desc(AggUserTypeAndResolvedIpNetworkDaily.date)).limit(7)
	db.session.remove()
	date = []
	resolved_number = []
	for item in query:
		date.append(item[0])
		resolved_number.append(int(item[1]))
	date.reverse()
	resolved_number.reverse()
	result_dict = {"date": date, "resolved_number": resolved_number}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 示范基地指数折线图
# agg_subscriber_organization_and_resolved_ip_network_daily
# resolved_ip_network = "公有云" and sum resolved_number group by date
@api.route('/dns/get-demonstration-bases-index', methods=['GET'])
def getDemonstrationBasesIndex():
	query = db.session.query(AggSubscriberOrganizationAndResolvedIpNetworkDaily.date,
		db.func.sum(AggSubscriberOrganizationAndResolvedIpNetworkDaily.resolved_number))\
		.filter_by(resolved_ip_network='公有云')\
		.group_by(AggSubscriberOrganizationAndResolvedIpNetworkDaily.date)\
		.order_by(db.desc(AggSubscriberOrganizationAndResolvedIpNetworkDaily.date)).limit(7)
	db.session.remove()
	date = []
	resolved_number = []
	for item in query:
		date.append(item[0])
		resolved_number.append(int(item[1]))
	date.reverse()
	resolved_number.reverse()
	result_dict = {"date": date, "resolved_number": resolved_number}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 应用服务指数折线图
# agg_is_focused_domain_category_daily
# sum resolved_number group by date
@api.route('/dns/get-application-service-index', methods=['GET'])
def getApplicationServiceIndex():
	query = db.session.query(AggIsFocusedDomainCategoryDaily.date,
		db.func.sum(AggIsFocusedDomainCategoryDaily.resolved_number))\
		.group_by(AggIsFocusedDomainCategoryDaily.date)\
		.order_by(db.desc(AggIsFocusedDomainCategoryDaily.date)).limit(7)
	db.session.remove()
	date = []
	resolved_number = []
	for item in query:
		date.append(item[0])
		resolved_number.append(int(item[1]))
	date.reverse()
	resolved_number.reverse()
	result_dict = {"date": date, "resolved_number": resolved_number}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 金融服务指数折线图
# agg_is_focused_domain_daily
# category = "供应链平台" and sum resolved_number group by date
@api.route('/dns/get-financial-service-index', methods=['GET'])
def getFinancialServiceIndex():
	query = db.session.query(AggIsFocusedDomainDaily.date,
		db.func.sum(AggIsFocusedDomainDaily.resolved_number))\
		.filter_by(category="供应链平台")\
		.group_by(AggIsFocusedDomainDaily.date)\
		.order_by(db.desc(AggIsFocusedDomainDaily.date)).limit(7)
	db.session.remove()
	date = []
	resolved_number = []
	for item in query:
		date.append(item[0])
		resolved_number.append(int(item[1]))
	date.reverse()
	resolved_number.reverse()
	result_dict = {"date": date, "resolved_number": resolved_number}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 全省发展指数折线图
# agg_subscriber_city_and_resolved_ip_network_daily
# resolved_ip_network = "公有云" and sum resolved_number group by date
@api.route('/dns/get-development-index', methods=['GET'])
def getDevelopmentIndex():
	query = db.session.query(AggSubscriberCityAndResolvedIpNetworkDaily.date,
		db.func.sum(AggSubscriberCityAndResolvedIpNetworkDaily.resolved_number))\
		.filter_by(resolved_ip_network='公有云')\
		.group_by(AggSubscriberCityAndResolvedIpNetworkDaily.date)\
		.order_by(db.desc(AggSubscriberCityAndResolvedIpNetworkDaily.date)).limit(7)
	db.session.remove()
	date = []
	resolved_number = []
	for item in query:
		date.append(item[0])
		resolved_number.append(int(item[1]))
	date.reverse()
	resolved_number.reverse()
	result_dict = {"date": date, "resolved_number": resolved_number}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)

# 地图
# agg_subscriber_city_and_resolved_ip_network_weekly
@api.route('/dns/get-development-index-weekly', methods=['GET'])
def getDevelopmentIndexWeekly():
	year = 2018
	week = 12
	query = db.session.query(AggSubscriberCityAndResolvedIpNetworkWeekly.subscriber_city, AggSubscriberCityAndResolvedIpNetworkWeekly.resolved_number)\
			.filter_by(resolved_ip_network='公有云').filter_by(year=year).filter_by(week=week).all()
	db.session.remove()
	subscriber_city = []
	resolved_number = []
	for item in query:
		subscriber_city.append(item[0])
		resolved_number.append(int(item[1]))
	result_dict = {"year": year, "week": week, "subscriber_city": subscriber_city, "resolved_number": resolved_number}
	result = common.trueReturn(result_dict, 'success')
	return jsonify(result)