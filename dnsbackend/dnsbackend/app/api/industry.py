#----------------------------------------------------------
# 行业分析
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


# 各行业TOP10
# agg_user_type_and_website_name_top_daily
@api.route('/dns/category-top-10-websites-daily', methods=['POST'])
def categoryTop10WebsitesDaily():
	date = request.get_json()['date']
	category = request.get_json()['category']
	if date and category:
		query = AggUserTypeAndWebsiteNameTopDaily.query.filter_by(category=category).filter_by(date=date).filter_by(user_type=0).order_by(AggUserTypeAndWebsiteNameTopDaily.user_type_and_category_rank).limit(10)
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
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

# 各行业清单
# agg_user_type_and_website_name_top_daily
@api.route('/dns/category-websites-daily', methods=['POST'])
def categoryWebsitesDaily():
	date = request.get_json()['date']
	week = request.get_json()['week']
	category = request.get_json()['category']

	if not category:
		result = common.falseReturn('', 'failed')
	else:
		if date and not week:
			query = AggUserTypeAndWebsiteNameTopDaily.query.filter_by(category=category).filter_by(date=date).filter_by(user_type=0).order_by(AggUserTypeAndWebsiteNameTopDaily.user_type_and_category_rank)
			if query:
				result_list = json.loads(json.dumps([x.to_dict() for x in query]))
				for result in result_list:
					if result['success_rate'] == 1:
						result['success_rate'] = '100%'
					elif result['success_rate'] == 0:
						result['success_rate'] = '0%'
					else:
						result['success_rate'] = ("%.5f" %(result['success_rate'] * 100)) + '%'
						if result['success_rate'] == '100.00000%':
							result['success_rate'] = '100%'
				result = common.trueReturn(result_list, 'success')
			else:
				result = common.falseReturn('', 'failed')
		elif week and not date:
			pass
		else:
			result = common.falseReturn('', 'failed')
	return jsonify(result)

# 行业类型数组
# agg_user_type_and_domain_top_daily
@api.route('/dns/get-categories', methods=['GET'])
def getCategories():
	query = db.session.query(AggUserTypeAndDomainTopDaily.category).filter(AggUserTypeAndDomainTopDaily.category!='').distinct().all()
	result_list = []
	for item in query:
		name = item[0]
		result_list.append(name)
	result = common.trueReturn(result_list, 'success')
	return jsonify(result)

# 根据行业类型和日期查找清单
# agg_user_type_and_domain_top_daily
@api.route('/dns/get-industry-list', methods=['POST'])
def getIndustryList():
	date = request.get_json()['date']
	week = request.get_json()['week']
	category = request.get_json()['category']
	if not category:
		result = common.falseReturn('', 'failed')
	else:
		if date and not week:
			query = AggUserTypeAndDomainTopDaily.query.filter_by(date=date).filter_by(category=category).filter_by(user_type=0).order_by(AggUserTypeAndDomainTopDaily.user_type_and_category_rank).all()
			if query:
				result_list = json.loads(json.dumps([x.to_dict() for x in query]))
				for result in result_list:
					if result['success_rate'] == 1:
						result['success_rate'] = '100%'
					elif result['success_rate'] == 0:
						result['success_rate'] = '0%'
					else:
						result['success_rate'] = ("%.5f" %(result['success_rate'] * 100)) + '%'
						if result['success_rate'] == '100.00000%':
							result['success_rate'] = '100%'
				result = common.trueReturn(result_list, 'success')
			else:
				result = common.falseReturn('', 'failed')
		elif week and not date:
			pass
		else:
			result = common.falseReturn('', 'failed')
	return jsonify(result)

# TOPN域名清单
# agg_user_type_and_domain_top_daily
@api.route('/dns/get-domain-list', methods=['POST'])
def getDomainList():
	date = request.get_json()['date']
	week = request.get_json()['week']
	if date and not week:
		query = AggUserTypeAndDomainTopDaily.query.filter_by(date=date).filter_by(user_type=0).order_by(db.desc(AggUserTypeAndDomainTopDaily.resolved_number)).limit(200)
		if query:
			result_list = json.loads(json.dumps([x.to_dict() for x in query]))
			for result in result_list:
				if result['success_rate'] == 1:
					result['success_rate'] = '100%'
				elif result['success_rate'] == 0:
					result['success_rate'] = '0%'
				else:
					result['success_rate'] = ("%.5f" %(result['success_rate'] * 100)) + '%'
					if result['success_rate'] == '100.00000%':
						result['success_rate'] = '100%'
			result = common.trueReturn(result_list, 'success')
		else:
			result = common.falseReturn('', 'failed')
	elif week and not date:
		pass
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)