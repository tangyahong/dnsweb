#----------------------------------------------------------
# 域名解析智能看板
# 域名访问量排名，TOP N域名及其他
#-----------------------------------------------------------

from flask import jsonify, request, g
from . import api
from .. import common
import datetime
from .. import geo
import simplejson as json
from functools import wraps
from app.api.decorator import *
from app.models import db
from app.models.topn_models import *
from app.models.industrial_internet_models import *
import datetime
import time

def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
db.Model.to_dict = to_dict

# 广东各地市所发起的请求量-日
# agg_src_city_daily
@api.route('/dns/resolved-number-from-city-daily', methods=['GET', 'POST'])
def resolvedNumberFromCityDaily():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
		# date = datetime.date.today().strftime('%Y%m%d')
	query = AggSrcCityDaily.query.filter_by(date=date).all()
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

# 每种用户类型所发起的访问量-日(user_type !=0 && user_type < 1000)
# agg_user_type_daily
@api.route('/dns/user-type-each-daily', methods=['GET', 'POST'])
def userTypeEachDaily():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
		# date = datetime.date.today().strftime('%Y%m%d')
	query = AggUserTypeDaily.query.filter_by(date=date).filter(AggUserTypeDaily.user_type != 0).filter(AggUserTypeDaily.user_type < 1000).all()
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

# 所有用户所发起的访问量趋势-日(user_type = 0)
# agg_user_type_hourly
@api.route('/dns/user-type-all-hourly', methods=['GET', 'POST'])
def userTypeAllHourly():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
	query = AggUserTypeHourly.query.filter_by(date=date).filter_by(user_type=0).all()
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

# 所有用户所发起的访问量趋势-周(user_type = 0)
# agg_user_type_daily
@api.route('/dns/user-type-all-daily', methods=['GET', 'POST'])
def userTypeAllDaily():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
	start = datetime.datetime.strptime(str(date),'%Y%m%d') + datetime.timedelta(days=-7)
	query = AggUserTypeDaily.query.filter(AggUserTypeDaily.date <= date).filter(AggUserTypeDaily.date >= start).all()
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

# 所有用户请求的TOP10网站及其访问量-日
# agg_user_type_and_website_name_top_daily
@api.route('/dns/top-10-website-daily', methods=['GET', 'POST'])
def top10WebsiteDaily():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
	query = AggUserTypeAndWebsiteNameTopDaily.query.filter_by(date=date).filter_by(user_type=0).filter(AggUserTypeAndWebsiteNameTopDaily.user_type_rank <= 10).order_by(AggUserTypeAndWebsiteNameTopDaily.user_type_rank).all()
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

# 所有用户请求的TOP10域名及其访问量-日
# agg_user_type_and_domain_top_daily
@api.route('/dns/top-10-domain-daily', methods=['GET', 'POST'])
def top10DomainDaily():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
	query = AggUserTypeAndDomainTopDaily.query.filter_by(date=date).filter_by(user_type=0).filter(AggUserTypeAndDomainTopDaily.user_type_rank<=10).order_by(AggUserTypeAndDomainTopDaily.user_type_rank).all()
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

# 所有用户域名分类访问情况-日
# agg_user_type_and_category_daily
@api.route('/dns/top-category-daily', methods=['GET', 'POST'])
def top10CategoryDaily():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
	query = AggUserTypeAndCategoryDaily.query.filter_by(date=date).filter_by(user_type=0).filter(AggUserTypeAndCategoryDaily.user_type_rank<=5).order_by(AggUserTypeAndCategoryDaily.user_type_rank).all()
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

# 移动用户访问趋势-小时
# agg_user_type_hourly
@api.route('/dns/resolved-number-mobile-hourly/<user_type>', methods=['GET', 'POST'])
def resolvedNumberMobileHourly(user_type):
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
	query = AggUserTypeHourly.query.filter_by(date=date).filter_by(user_type=user_type).order_by(AggUserTypeHourly.hour).all()
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

# 用户访问类型占比-日
# agg_user_type_daily
@api.route('/dns/resolved-number-user-type-daily', methods=['GET', 'POST'])
def resolvedNumberUserTypeDaily():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
	query = AggUserTypeDaily.query.filter_by(date=date).filter(AggUserTypeDaily.user_type>0).all()
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		for result in result_list:
			if result['user_type'] == 0:
				result['user_type'] = '所有用户'
			elif result['user_type'] == 1:
				result['user_type'] = '移动用户'
			elif result['user_type'] == 2:
				result['user_type'] = '固网用户'
			elif result['user_type'] == 3:
				result['user_type'] = '专线用户'
			else:
				pass
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

# 地市访问量-日
# agg_src_city_daily
@api.route('/dns/resolved-number-city-daily', methods=['GET', 'POST'])
def resolvedNumberCityDaily():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
	query = AggSrcCityDaily.query.filter_by(date=date).order_by(AggSrcCityDaily.resolved_number).all()
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

# 重点关注域名
# agg_is_focused_domain_daily
@api.route('/dns/key-domain-daily', methods=['GET', 'POST'])
def keyDomainDaily():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
	query = AggIsFocusedDomainDaily.query.filter_by(date=date).order_by(db.desc(AggIsFocusedDomainDaily.resolved_number)).limit(5)
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		for result in result_list:
			if result['success_rate'] == 1:
				result['success_rate'] = '100%'
			elif result['success_rate'] == 0:
				result['success_rate'] = '0%'
			else:
				result['success_rate'] = ("%.5f" %(result['success_rate'] * 100)) + '%'
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

# 网站对应子域名详情
# agg_user_type_and_domain_top_daily
@api.route('/dns/websites-domains-daily', methods=['POST'])
def websitesDomainsDaily():
	date = request.get_json()['date']
	website_name = request.get_json()['website_name']
	if date and website_name:
		query = AggUserTypeAndDomainTopDaily.query.filter_by(website_name=website_name).filter_by(date=date).filter_by(user_type=0).order_by(db.desc(AggUserTypeAndDomainTopDaily.resolved_number)).all()
		if query:
			result_list = json.loads(json.dumps([x.to_dict() for x in query]))
			for index, result in enumerate(result_list):
				result['user_type_and_website_rank'] = index + 1
				if result['success_rate'] == 1:
					result['success_rate'] = '100%'
				elif result['success_rate'] == 0:
					result['success_rate'] = '0%'
				else:
					result['success_rate'] = ("%.5f" %(result['success_rate'] * 100)) + '%'
			result = common.trueReturn(result_list, 'success')
		else:
			result = common.falseReturn('', 'failed')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)
