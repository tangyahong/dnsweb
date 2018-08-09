# -*- coding: utf-8 -*-
from flask import jsonify, request, g, make_response, send_file
from . import api
from .. import common
import datetime
import simplejson as json
from functools import wraps
from app.api.decorator import *
from app.models import db
from app.models.flow_models import *
from app.models.normal_models import *
import datetime
import time
import os

def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
db.Model.to_dict = to_dict

def session_commit():
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        reason = str(e)
        print(reason)
        return reason

# 域名清单表增删改查
# dim_focused_domain
@api.route('/dns/focus-domain/show', methods=['GET'])
def focusDomainShow():
	query = DimFocusedDomain.query.all()
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

@api.route('/dns/focus-domain/search', methods=['POST'])
def focusDomainSearch():
	content = request.get_json()['content']
	query = DimFocusedDomain.query.filter((DimFocusedDomain.domain.like('%' + content + '%')) | (DimFocusedDomain.tld_plus_two.like('%' + content + '%'))
		| (DimFocusedDomain.tld_plus_one.like('%' + content + '%'))
		| (DimFocusedDomain.like_pattern.like('%' + content + '%')) | (DimFocusedDomain.regexp_pattern.like('%' + content + '%'))
		| (DimFocusedDomain.is_focused.like('%' + content + '%')) | (DimFocusedDomain.category.like('%' + content + '%'))
		| (DimFocusedDomain.website_name.like('%' + content + '%')) | (DimFocusedDomain.comment.like('%' + content + '%'))).all()
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

@api.route('/dns/focus-domain/add', methods=['POST'])
def focusDomainAdd():
	domain = request.get_json()['domain']
	tld_plus_two = request.get_json()['tld_plus_two']
	tld_plus_one = request.get_json()['tld_plus_one']
	like_pattern = request.get_json()['like_pattern']
	regexp_pattern = request.get_json()['regexp_pattern']
	is_focused = request.get_json()['is_focused']
	category = request.get_json()['category']
	website_name = request.get_json()['website_name']
	comment = request.get_json()['comment']
	focusDomain = DimFocusedDomain(domain=domain, tld_plus_two=tld_plus_two, tld_plus_one=tld_plus_one, like_pattern=like_pattern,
		regexp_pattern=regexp_pattern, is_focused=is_focused, category=category, website_name=website_name, comment=comment)
	db.session.begin()
	db.session.add(focusDomain)
	result = session_commit()
	if result:
		result = common.falseReturn('', "failed")
	else:
		result = common.trueReturn('', 'success')
	return jsonify(result)

@api.route('/dns/focus-domain/delete', methods=['POST'])
def focusDomainDelete():
	id = request.get_json()['id']
	db.session.begin()
	query= DimFocusedDomain.query.filter_by(id=id).all()
	if query:
		DimFocusedDomain.query.filter_by(id=id).delete()
		result = session_commit()
		if result:
			result = common.falseReturn('', "failed")
		else:
			result = common.trueReturn('', 'success')
	else:
		result = common.falseReturn('', "failed")
	return jsonify(result)

@api.route('/dns/focus-domain/update/<id>', methods=['POST'])
def focusDomainUpdate(id):
	# id = request.get_json()['id']
	domain = request.get_json()['domain']
	tld_plus_two = request.get_json()['tld_plus_two']
	tld_plus_one = request.get_json()['tld_plus_one']
	like_pattern = request.get_json()['like_pattern']
	regexp_pattern = request.get_json()['regexp_pattern']
	is_focused = request.get_json()['is_focused']
	category = request.get_json()['category']
	website_name = request.get_json()['website_name']
	comment = request.get_json()['comment']
	query = DimFocusedDomain.query.filter_by(id=id).first()
	if query:
		db.session.begin()
		query.domain = domain
		query.tld_plus_two = tld_plus_two
		query.tld_plus_one = tld_plus_one
		query.like_pattern = like_pattern
		query.regexp_pattern = regexp_pattern
		query.is_focused = is_focused
		query.category = category
		query.website_name = website_name
		query.comment = comment
		result = session_commit()
		if result:
			result = common.falseReturn('', "failed")
		else:
			result = common.trueReturn('', 'success')
	else:
		result = common.falseReturn('', "failed")
	return jsonify(result)

@api.route('/dns/focus-domain/deleteSelected', methods=['POST'])
def focusDomainDeleteSelected():
	idList = request.get_json()['id']
	query = DimFocusedDomain.query.filter(DimFocusedDomain.id.in_(idList)).all()
	if query:
		db.session.begin()
		DimFocusedDomain.query.filter(DimFocusedDomain.id.in_(idList)).delete(synchronize_session=False)
		result = session_commit()
		if result:
			result = common.falseReturn('', "failed")
		else:
			result = common.trueReturn('', 'success')
	else:
		result = common.falseReturn('', "failed")
	return jsonify(result)

# 模板下载
@api.route('/dns/focus-domain/download-template', methods=['GET'])
def focusDomainDeleteDownloadTemplate():
	file = os.path.join(os.getcwd(), 'app/static/template.xlsx')
	response = make_response(send_file(file))
	response.headers["Content-Disposition"] = "attachment; filename={};".format('template.xlsx')
	return response
