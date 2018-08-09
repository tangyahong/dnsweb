from flask import jsonify, request, g
from app.api.decorator import *
import requests
import json
from . import api
from .. import common


@api.route('/dns/icp_license_query', methods=['POST'])
def icp_licence_query():
	domain = request.get_json()['domain']
	url = 'http://123.207.17.166:3000/icp?domain=' + domain
	r = requests.get(url)
	content = json.loads(r.text)
	if content['success']:
		query_result = {}
		query_result['domain'] = content['domain']
		query_result['companyBeianCode'] = content['items']['companyBeianCode']
		query_result['name'] = content['items']['name']
		query_result['siteBeianCode'] = content['items']['siteBeianCode']
		result = common.trueReturn(query_result, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)
