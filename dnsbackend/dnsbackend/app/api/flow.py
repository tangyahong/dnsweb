from flask import jsonify, request, g

from . import api
from .. import common
import datetime
from .. import geo
# import json
import simplejson as json
from functools import wraps
# from IPy import IP
from app.api.decorator import *
from app.models import db
# from app.models.topn_models import *
# from app.models.industrial_internet_models import *
from app.models.flow_models import *
# from app.models.models import *
import datetime
import time

def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
db.Model.to_dict = to_dict


# 广东各地市访问21个地市情况
# agg_src_city_and_dst_city_and_dst_operator_daily
@api.route('/dns/visit-21-cities', methods=['GET', 'POST'])
def visit21Cities():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
		# date = datetime.date.today().strftime('%Y%m%d')
	query = db.session.query(AggSrcCityAndDstCityAndDstOperatorDaily.source_ip_city,
		db.func.sum(AggSrcCityAndDstCityAndDstOperatorDaily.resolved_number)).group_by(AggSrcCityAndDstCityAndDstOperatorDaily.source_ip_city)\
		.order_by(db.desc(db.func.sum(AggSrcCityAndDstCityAndDstOperatorDaily.resolved_number)))\
		.filter_by(resolved_ip_province='广东').filter_by(resolved_ip_operator='电信').filter_by(date=date)
	db.session.remove()
	result_list = []
	for index, item in enumerate(query):
		result_list.append({"rank": index+1, "source_ip_city": item[0], "resolved_number": int(item[1])})
	result = common.trueReturn(result_list, 'success')
	return jsonify(result)

# 广东各地市被21个地市访问的情况
# agg_src_city_and_dst_city_and_dst_operator_daily
@api.route('/dns/visited-by-21-cities', methods=['GET', 'POST'])
def visitedBy21Cities():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
	query = db.session.query(AggSrcCityAndDstCityAndDstOperatorDaily.resolved_ip_city,
		db.func.sum(AggSrcCityAndDstCityAndDstOperatorDaily.resolved_number)).group_by(AggSrcCityAndDstCityAndDstOperatorDaily.resolved_ip_city)\
		.order_by(db.desc(db.func.sum(AggSrcCityAndDstCityAndDstOperatorDaily.resolved_number)))\
		.filter_by(resolved_ip_province='广东').filter_by(resolved_ip_operator='电信').filter_by(date=date)
	db.session.remove()
	result_list = []
	for index, item in enumerate(query):
		result_list.append({"rank": index+1, "resolved_ip_city": item[0], "resolved_number": int(item[1])})
	result = common.trueReturn(result_list, 'success')
	return jsonify(result)

# 地市到地市之间访问情况前十
# agg_src_city_and_dst_city_and_dst_operator_daily
@api.route('/dns/flow-city-to-city', methods=['GET', 'POST'])
def flowCityToCity():
	if request.method == 'POST':
		date = request.get_json()['date']
	else:
		date = 20180318
	query = db.session.query(AggSrcCityAndDstCityAndDstOperatorDaily.source_ip_city,
		AggSrcCityAndDstCityAndDstOperatorDaily.resolved_ip_city,
		AggSrcCityAndDstCityAndDstOperatorDaily.resolved_number)\
		.order_by(db.desc(AggSrcCityAndDstCityAndDstOperatorDaily.resolved_number))\
		.filter_by(date=date).filter_by(resolved_ip_province='广东').filter_by(resolved_ip_operator='电信').limit(20)
	db.session.remove()
	result_list = []
	for index, item in enumerate(query):
		result_list.append({"rank": index+1, "city": item[0] + 'to' + item[1], "resolved_number": int(item[2])})
	result = common.trueReturn(result_list, 'success')
	return jsonify(result)