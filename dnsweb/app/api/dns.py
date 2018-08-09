from flask import jsonify, request, g
from app.models.models import *
# from app.models.models import FT_Domain_Top_Daily, Domain_IP, Dm_Domain_IP, Ag_Statistics_Daily
# from app.models import FT_Domain_Top_Weelkly, Key_Domain, Dm_Tld_ICP, Dm_Tld_Whois
# from app.models import Dm_Domain_Route
# from app.models import FT_Customer_Csp_Hourly, FT_Customer_Info, FT_Customer_Cloud_Domain_Top_Hourly, FT_Customer_Not_Cloud_Domain_Top_Hourly
from . import api
from .. import common
import datetime
from .. import geo
import json
from functools import wraps
from IPy import IP
from app.api.decorator import *

# def login_required(f):
# 	@wraps(f)
# 	def decorated_function(*args, **kwargs):
# 		authResult = Auth.identify(Auth, request)
# 		if authResult['status'] and authResult['data']:
# 			return f(*args, **kwargs)
# 		else:
# 			return jsonify(authResult)
# 	return decorated_function


@api.route('/dns/test', methods=['GET'])
def test():
	result = common.trueReturn('success', 'success')
	return jsonify(result)

#获取TOPN域名的信息
@api.route('/dns/topn/<count>', methods=['GET'])
def getTopN(count):
	topn = FT_Domain_Top_Daily.get_rank(FT_Domain_Top_Daily, count)
	topn_list = []
	for item in topn:
		d = {}
		d['domain'] = item.domain
		d['tld'] = item.tld
		d['resolved_ip'] = item.resolved_ip
		d['service_name'] = item.service_name
		d['category_name'] = item.category_name
		d['count'] = item.count
		d['rank'] = item.rank
		topn_list.append(d)
	result = common.trueReturn(topn_list, '请求成功')
	return jsonify(result)


# *重写*获取TOPN域名信息的接口
@api.route('/dns/topn', methods=['POST'])
def getTopN_new():
	date = request.get_json()['date']
	week = request.get_json()['week']
	count = request.get_json()['count']
	if date and not week:
		topn = FT_Domain_Top_Daily.get_rank(FT_Domain_Top_Daily, count, date)
	elif week and not date:
		tmp = week.split('-')
		week = tmp[0] + str(datetime.date(int(tmp[0]), int(tmp[1]), int(tmp[2])).isocalendar()[1])
		topn = FT_Domain_Top_Weelkly.get_rank(FT_Domain_Top_Weelkly, count, week)
	else:
		result = common.falseReturn('', '请求失败')
		return jsonify(result)
	topn_list = []
	for item in topn:
		d = {}
		d['domain'] = item.domain
		d['tld'] = item.tld
		d['resolved_ip'] = item.resolved_ip
		d['service_name'] = item.service_name
		d['category_name'] = item.category_name
		d['count'] = item.count
		d['success_rate'] = "%.2f%%" % (item.success_rate*100)
		d['rank'] = item.rank
		topn_list.append(d)
	result = common.trueReturn(topn_list, '请求成功')
	return jsonify(result)

# 获取单个域名的解析量数据,用于折线图
@api.route('/dns/topn/singledomain', methods=['POST'])
def getTopnSingleDomain():
	domain = request.get_json()['domain']
	query = FT_Domain_Top_Daily.get_domain_count(FT_Domain_Top_Daily, domain)
	info_list = []
	for item in query:
		d = {}
		d['name'] = item.date
		d['value'] = item.count
		info_list.append(d)
	result = common.trueReturn(info_list, '请求成功')
	return jsonify(result)

# 获取单个域名的所有数据
@api.route('/dns/single-domain', methods=['POST'])
def getSingleDomain():
	domain = request.get_json()['domain']
	query = FT_Domain_Top_Daily.get_domain_count_limit(FT_Domain_Top_Daily, domain, 7)
	query2 = Key_Domain.getSingleDomain(Key_Domain, domain)
	legal_ip_list = []
	for item in query2:
		legal_ip_list.append(item.legal_ip)
		# ip_list = item.legal_ip.split(';')
		# for ip in ip_list:
			# legal_ip_list.append(ip)
	legal_ip_list = list(set(legal_ip_list))
	# print(legal_ip_list)
	if query:
		result_list = []
		for item in query:
			d = {}
			d['domain'] = item.domain
			d['stld'] = item.stld
			d['tld'] = item.tld
			d['resolved_ip'] = item.resolved_ip
			d['service_name'] = item.service_name
			d['category_name'] = item.category_name
			d['count'] = item.count
			d['rank'] = item.rank
			d['category_rank'] = item.category_rank
			d['success_rate'] = "%.2f%%" % (item.success_rate*100)
			d['date'] = item.date
			flag = 0
			for ip in item.resolved_ip.split(';'):
				if ip not in legal_ip_list:
					flag = 1
			if flag == 1:
				d['status'] = '异常'
			else:
				d['status'] = '正常'
			# print(d['status'])
			result_list.append(d)
		result = common.trueReturn(result_list, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)


# 查询IP的ISP信息
@api.route('/dns/ip-isp-query-list', methods=['POST'])
def getIpISPQueryList():
	iplist = request.get_json()['resolved_ip']
	if iplist:
		result_list = Dm_Domain_IP.inverse_ip_list_query(Dm_Domain_IP, iplist)
		result = common.trueReturn(result_list, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)

# 根据IP地址反查域名
@api.route('/dns/inverse-ip-query', methods=['POST'])
def getInverseIPQuery():
	ip = request.get_json()['ip'].strip()
	if ip:
		query = Domain_IP.inverse_ip_query(Domain_IP, ip)
		result_list = []
		for item in query:
			d = {}
			d['domain'] = item.domain
			d['ip'] = item.ip
			d['country'] = item.country
			d['province'] = item.province
			d['operator'] = item.operator
			result_list.append(d)
		result = common.trueReturn(result_list, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)


# 获取所有类别的名称
@api.route('/dns/get-category-name', methods=['GET'])
def getDisctinctCategory():
	query = FT_Domain_Top_Daily.get_distinct_category(FT_Domain_Top_Daily)
	result = common.trueReturn(query, '请求成功')
	return jsonify(result)

# 获取具体类别的当日排名情况
@api.route('/dns/get-category-date-topn', methods=['POST'])
def getCategoryDateTopn():
	date = request.get_json()['date']
	category_name = request.get_json()['category_name']
	count = request.get_json()['count']
	if date and category_name:
		query = FT_Domain_Top_Daily.get_category_rank(FT_Domain_Top_Daily, category_name, count, date)
		result_list = []
		for item in query:
			d = {}
			d['category_name'] = item.category_name
			d['category_rank'] = item.category_rank
			d['stld'] = item.stld
			d['tld'] = item.tld
			d['domain'] = item.domain
			d['resolved_ip'] = item.resolved_ip
			d['service_name'] = item.service_name
			d['count'] = item.count
			d['success_rate'] = "%.2f%%" % (item.success_rate*100)
			result_list.append(d)
		result = common.trueReturn(result_list, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)


#获取类别域名的聚合结果
@api.route('/dns/get-category-group', methods=['POST'])
def getCategoryGroup():
	date = request.get_json()['date']
	category_name = request.get_json()['category_name']
	count = request.get_json()['count']
	if date and category_name:
		query = FT_Domain_Top_Daily.get_category_group(FT_Domain_Top_Daily, category_name, date, count)
		result = common.trueReturn(query, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)


# 重写类别域名聚合结果
@api.route('/dns/get-category-group-new/<count>', methods=['POST'])
def getCategoryGroupNew(count):
	date = request.get_json()['date']
	week = request.get_json()['week']
	category_name = request.get_json()['category_name']
	# count = request.get_json()['count']
	if date and not week:
		if category_name:
			query = FT_Domain_Top_Daily.get_category_group(FT_Domain_Top_Daily, category_name, date, count)
			result = common.trueReturn(query, '请求成功')
		else:
			result = common.falseReturn('', '请求失败')
	elif week and not date:
		if category_name:
			tmp = week.split('-')
			week = int(tmp[0] + str(datetime.date(int(tmp[0]), int(tmp[1]), int(tmp[2])).isocalendar()[1]))
			query = FT_Domain_Top_Weelkly.get_category_group(FT_Domain_Top_Weelkly, category_name, count, week)
			result = common.trueReturn(query, '请求成功')
		else:
			result = common.falseReturn('', '请求失败')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)

# 重写具体类别的排名情况
@api.route('/dns/get-category-topn/<count>', methods=['POST'])
def getCategoryTopn(count):
	date = request.get_json()['date']
	week = request.get_json()['week']
	# count = request.get_json()['count']
	category_name = request.get_json()['category_name']
	if date and not week:
		if category_name:
			query = FT_Domain_Top_Daily.get_category_rank(FT_Domain_Top_Daily, category_name, count, date)
			result_list = []
			for item in query:
				d = {}
				d['category_name'] = item.category_name
				d['category_rank'] = item.category_rank
				d['stld'] = item.stld
				d['tld'] = item.tld
				d['domain'] = item.domain
				d['resolved_ip'] = item.resolved_ip
				d['service_name'] = item.service_name
				d['count'] = item.count
				d['success_rate'] = "%.2f%%" % (item.success_rate*100)
				result_list.append(d)
			result = common.trueReturn(result_list, '请求成功')
		else:
			result = common.falseReturn('', '请求失败')
	elif week and not date:
		if category_name:
			tmp = week.split('-')
			week = int(tmp[0] + str(datetime.date(int(tmp[0]), int(tmp[1]), int(tmp[2])).isocalendar()[1]))
			query = FT_Domain_Top_Weelkly.get_category_rank(FT_Domain_Top_Weelkly, category_name, count, week)
			result_list = []
			for item in query:
				# print(item)
				d = {}
				d['category_name'] = item.category_name
				d['category_rank'] = item.category_rank
				d['stld'] = item.stld
				d['tld'] = item.tld
				d['domain'] = item.domain
				d['resolved_ip'] = item.resolved_ip
				d['service_name'] = item.service_name
				d['count'] = item.count
				d['success_rate'] = "%.2f%%" % (item.success_rate*100)
				result_list.append(d)
			result = common.trueReturn(result_list, '请求成功')
		else:
			result = common.falseReturn('', '请求失败')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)


# 获取具体类别的当周排名情况
@api.route('/dns/get-category-week-topn', methods=['POST'])
def getCategoryWeekTopn():
	date = request.get_json()['date']
	tmp = date.split('-')
	# print(tmp[0])
	# print(str(datetime.date(tmp[0], tmp[1], tmp[2]).isocalendar()[1]))
	week = tmp[0] + str(datetime.date(int(tmp[0]), int(tmp[1]), int(tmp[2])).isocalendar()[1])
	# week = datetime.date(int(tmp[0]), int(tmp[1]), int(tmp[2])).isocalendar()[1]
	# print(week)
	category_name = request.get_json()['category_name']
	count = request.get_json()['count']
	if date and category_name:
		query = FT_Domain_Top_Weelkly.get_category_rank(FT_Domain_Top_Weelkly, category_name, count, week)
		result_list = []
		for item in query:
			d = {}
			d['category_name'] = item.category_name
			d['category_rank'] = item.category_rank
			d['stld'] = item.stld
			d['tld'] = item.tld
			d['domain'] = item.domain
			d['resolved_ip'] = item.resolved_ip
			d['service_name'] = item.service_name
			d['count'] = item.count
			d['success_rate'] = "%.2f%%" % (item.success_rate*100)
			result_list.append(d)
		result = common.trueReturn(result_list, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)


#获取类别域名的聚合结果
@api.route('/dns/get-category-group-week', methods=['POST'])
def getCategoryGroupWeek():
	date = request.get_json()['date']
	tmp = date.split('-')
	week = int(tmp[0] + str(datetime.date(int(tmp[0]), int(tmp[1]), int(tmp[2])).isocalendar()[1]))
	category_name = request.get_json()['category_name']
	count = request.get_json()['count']
	if date and category_name:
		query = FT_Domain_Top_Weelkly.get_category_group(FT_Domain_Top_Weelkly, category_name, count, week)
		result = common.trueReturn(query, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)

#获取非电信ISP的记录
@api.route('/dns/get-isp-statistics-exp-telecom', methods=['GET'])
def getISPStatisticsExpTelecom():
	query = Dm_Domain_IP.isp_statistics_exp_telecom(Dm_Domain_IP)
	# from IPython import embed;embed()
	result = common.trueReturn(query, '请求成功')
	return jsonify(result)

# 获取top100域名的ISP信息
# @api.route('/dns/get-top-100-isp-proportion', methods=['GET'])
# def getTop100ISPProportin():
# 	query = FT_Domain_Top_Weelkly.query.join(Domain_IP, FT_Domain_Top_Weelkly.domain == Domain_IP.domain)\
# 		.filter(FT_Domain_Top_Weelkly.rank <= 100).all()
# 	result_list = []
# 	for item in query:
# 		print(item.resolved_ip)
	# for item in query:

	#print(query)
	# result = common.trueReturn(query, '请求成功')
	# return jsonify(result)
	# query = FT_Domain_Top_Weelkly.get_rank(FT_Domain_Top_Weelkly, 100, '201747')
	# print(query)
	# iplist = []
	# for item in query:
	# 	tmplist = item.resolved_ip.split(';')
	# 	for i in tmplist:
	# 		iplist.append(i)
	# print(iplist)
	# query = Domain_IP.inverse_ip_list_query(Domain_IP, iplist)
	# result = common.trueReturn(query, '请求成功')
	# return jsonify(result)

# 获取所有的重点域名的清单
@api.route('/dns/get-key-domain-name', methods=['GET'])
def getKeyDomainName():
	query = Key_Domain.getAllDomain(Key_Domain)
	if query:
		result_list = []
		for item in query:
			result_list.append(item.domain)
		result_list = list(set(result_list))
		result = common.trueReturn(result_list, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)

# 获取所有重点域名的信息
@api.route('/dns/get-all-key-domain', methods=['GET'])
def getAllKeyDomain():
	query = Key_Domain.getAllDomain(Key_Domain)
	if query:
		result_list = []
		for item in query:
			d = {}
			d['id'] = item.id
			d['domain'] = item.domain
			d['legal_ip'] = item.legal_ip
			result_list.append(d)
		result = common.trueReturn(result_list, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)

# 获取单个重点域名的信息
@api.route('/dns/get-single-key-domain', methods=['POST'])
def getSingleKeyDomain():
	domain = request.get_json()['domain']
	query = Key_Domain.getSingleDomain(Key_Domain, domain)
	if query:
		result_list = []
		for item in query:
			d = {}
			d['id'] = item.id
			d['domain'] = item.domain
			d['legal_ip'] = item.legal_ip
			result_list.append(d)
		result = common.trueReturn(result_list, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)

# 删除重点域名
@api.route('/dns/delete-select-domain', methods=['POST'])
def deleteSelectDomain():
	id = request.get_json()['id']
	try:
		Key_Domain.deleteSelectDomain(Key_Domain, id)
		result = common.trueReturn('', '请求成功')
	except:
		result = common.falseReturn('', '请求失败')
	finally:
		return jsonify(result)

# 更新重点域名信息
@api.route('/dns/edit-select-domain/<id>', methods=['POST'])
def editSelectDomain(id):
	# id = request.get_json()['id']
	domain = request.get_json()['domain']
	legal_ip = request.get_json()['legal_ip']
	query = Key_Domain.getSingleDomainById(Key_Domain,id)
	if query:
		try:
			query.domain = domain
			query.legal_ip = legal_ip
			Key_Domain.updateSelectDomain()
			result = common.trueReturn('', '请求成功')
		except:
			result = common.falseReturn('', '请求失败')
		finally:
			return jsonify(result)
	else:
		result = common.falseReturn('', '请求失败')
		return jsonify(result)

# 获取单个二级域名的ICP信息
@api.route('/dns/get-icp-info', methods=['POST'])
def getICPInfo():
	tld = request.get_json()['tld']
	query = Dm_Tld_ICP.getICPInfo(Dm_Tld_ICP, tld)
	if query:
		result_list = []
		d = {}
		d['tld'] = query.tld
		d['name']= query.name
		d['siteBeianCode'] = query.siteBeianCode
		d['companyBeianCode'] = query.companyBeianCode
		result_list.append(d)
		result = common.trueReturn(result_list, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)

# 根据网站备案号查单个二级域名的ICP信息
@api.route('/dns/get-icp-info-by-beiancode', methods=['POST'])
def getICPInfoByBeianCode():
	beianCode = request.get_json()['beianCode']
	query = Dm_Tld_ICP.getICPInfoByBeianCode(Dm_Tld_ICP, beianCode)
	# query2 = Dm_Tld_ICP.getICPInfoByCompanyBeianCode(Dm_Tld_ICP, beianCode)
	result_list = []
	if query:
		for item in query:
			d = {}
			d['tld'] = item.tld
			d['name']= item.name
			d['siteBeianCode'] = item.siteBeianCode
			d['companyBeianCode'] = item.companyBeianCode
			result_list.append(d)
	# if query1 or query2:
	# 	if query1:
	# 		for item in query1:
	# 			d = {}
	# 			d['tld'] = item.tld
	# 			d['name']= item.name
	# 			d['siteBeianCode'] = item.siteBeianCode
	# 			d['companyBeianCode'] = item.companyBeianCode
	# 			result_list.append(d)
	# 	if query2:
	# 		for item in query2:
	# 			d = {}
	# 			d['tld'] = item.tld
	# 			d['name']= item.name
	# 			d['siteBeianCode'] = item.siteBeianCode
	# 			d['companyBeianCode'] = item.companyBeianCode
	# 			result_list.append(d)
	# 	print(result_list)
	# 	result_list = list(set(result_list))
	# 	print(result_list)
		result = common.trueReturn(result_list, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)

# 获取单个二级域名的Whois信息
@api.route('/dns/get-whois-info', methods=['POST'])
def getWhoisInfo():
	tld = request.get_json()['tld']
	query = Dm_Tld_Whois.getTldWhois(Dm_Tld_Whois, tld)
	if query:
		result_list = []
		d = {}
		d['tld'] = query.tld
		d['domain_name'] = query.domain_name
		d['registrar'] = query.registrar
		d['name'] = query.name
		d['emails'] = query.emails
		d['address'] = query.address
		d['status'] = query.status
		d['dnssec'] = query.dnssec
		d['name_servers'] = query.name_servers
		d['referral_url'] = query.referral_url
		d['whois_server'] = query.whois_server
		d['org'] = query.org
		d['country'] = query.country
		d['state'] = query.state
		d['city'] = query.city
		d['zipcode'] = query.zipcode
		# d['text'] = query.text
		d['updated_date'] = query.updated_date
		d['creation_date'] = query.creation_date
		d['expiration_date'] = query.expiration_date

		e = {}
		e['name'] = '二级域名'
		e['value'] = query.tld
		result_list.append(e)
		e = {}
		e['name'] = '域名'
		e['value'] = query.domain_name
		result_list.append(e)
		e = {}
		e['name'] = '注册公司'
		e['value'] = query.registrar
		result_list.append(e)
		# e = {}
		# e['name'] = '注册者'
		# e['value'] = query.name
		# result_list.append(e)
		e = {}
		e['name'] = 'E-mail'
		e['value'] = query.emails
		result_list.append(e)
		e = {}
		e['name'] = '地址'
		e['value'] = query.address
		result_list.append(e)
		# e['name'] = '状态'
		# e['value'] = query.status
		# result_list.append(e)
		# e['name'] = '姓名'
		# e['value'] = query.dnssec
		# result_list.append(e)
		e = {}
		e['name'] = '域名NS'
		e['value'] = query.name_servers
		result_list.append(e)
		# e['name'] = '姓名'
		# e['value'] = query.referral_url
		# result_list.append(e)
		# e['name'] = '二级域名'
		# e['value'] = query.whois_server
		# result_list.append(e)
		# e['name'] = '姓名'
		# e['value'] = query.org
		# result_list.append(e)
		# e = {}
		# e['name'] = '国家'
		# e['value'] = query.country
		# result_list.append(e)
		# e = {}
		# e['name'] = '省份'
		# e['value'] = query.state
		# result_list.append(e)
		# e = {}
		# e['name'] = '地市'
		# e['value'] = query.city
		# result_list.append(e)
		# e = {}
		# e['name'] = '邮编'
		# e['value'] = query.zipcode
		# result_list.append(e)
		# e['name'] = '二级域名'
		# e['value'] = query.text
		# result_list.append(e)
		# e = {}
		# e['name'] = '最近更新时间'
		# e['value'] = query.updated_date
		# result_list.append(e)
		# e = {}
		# e['name'] = '申请时间'
		# e['value'] = query.creation_date
		# result_list.append(e)
		e = {}
		e['name'] = '域名过期时间'
		e['value'] = query.expiration_date
		result_list.append(e)
		e = {}
		e['name'] = '详情'
		e['value'] = query.text
		result_list.append(e)
		result = common.trueReturn(result_list, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)

# 获取总体情况
@api.route('/dns/get-dashboard-Info', methods=['GET'])
def getDashboardInfo():
	query = Ag_Statistics_Daily.getAgStatistics(Ag_Statistics_Daily, 10)
	if query:
		result_dict = {}
		count1 = query[0].count
		count2 = query[1].count
		rate1 = query[0].success_rate
		rate2 = query[1].success_rate
		if count1 > count2:
			dif_count = '+' + str("%.2f%%" %  ((count1 - count2) / count2 * 100))
		else:
			dif_count = "%.2f%%" %  ((count1 - count2) / count2 * 100)
		if rate1 > rate2:
			dif_rate = '+' + str("%.2f%%" %  ((rate1 - rate2) / rate2 * 100))
		else:
			dif_rate = "%.2f%%" %  ((rate1 - rate2) / rate2 * 100)
		d1 = {}
		d1['count_yesterday'] = count1
		d1['dif_count'] = dif_count
		d1['success_rate_yesterday'] = "%.3f%%" % (rate1 * 100)
		d1['dif_rate'] = dif_rate
		tmp = []
		count_sum = 0
		for item in query:
			count_sum += item.count
			d = {}
			d['count'] = item.count
			d['success_rate'] = item.success_rate * 100
			d['date'] = item.date
			tmp.append(d)
		d1['count_sum'] = count_sum
		d1['dif_count_sum'] = '+0.12%'
		result_dict['daily_statistics'] = d1
		result_dict['charts_statistics'] = tmp
		result = common.trueReturn(result_dict, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)

@api.route('/dns/get-cdn-route', methods=['POST'])
def getCDNRoute():
	domain = request.get_json()['domain']
	query = Dm_Domain_Route.getRoute(Dm_Domain_Route, domain)
	routeMap = []
	if query:
		for item in query:
			routeMap = routeMap + json.loads(item.route)
		result = common.trueReturn(routeMap, '请求成功')
	else:
		result = common.falseReturn('', '请求失败')
	return jsonify(result)

@api.route('/dns/get-customer-csp-hourly', methods=['POST'])
# @login_required
def getCustomerCspHourly():
	customer_name = request.get_json()['customer_name']
	date = request.get_json()['date']
	query = FT_Customer_Csp_Hourly.getData(FT_Customer_Csp_Hourly,customer_name, date)
	if query:
		result_list = json.dumps(query)
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

'''
获取专线客户信息
GET：获取所有专线客户名称
POST：获取单个专线客户详细信息
'''
@api.route('/dns/get-customer-info', methods=['GET', 'POST'])
def getCustomerInfo():
	if request.method == 'GET':
		query = FT_Customer_Info.getCustomerName(FT_Customer_Info)
		result = common.trueReturn(query, 'success') if query else common.falseReturn('', 'failed')
		return jsonify(result)
	else:
		customer_name = request.get_json()['customer_name']
		ipaddress = request.get_json()['ipaddress']
		line_code = request.get_json()['line_code']
		query = FT_Customer_Info.getCustomerInfo(FT_Customer_Info, customer_name, ipaddress, line_code)
		if query:
			result_list = json.loads(json.dumps([x.to_dict() for x in query]))
			result = common.trueReturn(result_list, 'success')
		else:
			result = common.falseReturn('', 'failed')
		return jsonify(result)

'''
删除专线客户信息
'''
@api.route('/dns/delete-customer-info', methods=['POST'])
def DeleteCustomerInfo():
	id = request.get_json()['id']
	query = FT_Customer_Info.deleteCustomerInfo(FT_Customer_Info, id)
	result = common.trueReturn('', 'failed') if query else common.falseReturn('', 'success')
	return jsonify(result)

'''
编辑专线客户信息
'''
@api.route('/dns/customer-info/edit/<id>', methods=['POST'])
def CustomerInfoEdit(id):
	organization = request.get_json()['organization']
	customer_name = request.get_json()['customer_name']
	src_address = request.get_json()['src_address']
	dst_address = request.get_json()['dst_address']
	customer_name = request.get_json()['customer_name']
	customer_address = request.get_json()['customer_address']
	customer_type = request.get_json()['customer_type']
	line_code = request.get_json()['line_code']
	query = FT_Customer_Info.getCustomerInfoById(FT_Customer_Info, id)
	if query:
		query.organization = organization
		query.customer_name = customer_name
		query.src_address = src_address
		query.dst_address = dst_address
		query.src_address_int = IP(src_address).int()
		query.dst_address_int = IP(dst_address).int()
		query.customer_address = customer_address
		query.customer_type = customer_type
		query.line_code = line_code
		result = FT_Customer_Info.updateCustomerInfo()
		result = common.trueReturn('', 'failed') if result else common.falseReturn('', 'success')
		return jsonify(result)
	else:
		result = common.falseReturn('', '请求失败')
		return jsonify(result)

'''
新增专线客户信息
'''
@api.route('/dns/customer-info/add', methods=['POST'])
def CustomerInfoAdd():
	organization = request.get_json()['organization']
	customer_name = request.get_json()['customer_name']
	src_address = request.get_json()['src_address']
	dst_address = request.get_json()['dst_address']
	customer_address = request.get_json()['customer_address']
	customer_type = request.get_json()['customer_type']
	line_code = request.get_json()['line_code']
	src_address_int = IP(src_address).int()
	dst_address_int = IP(dst_address).int()
	print(src_address_int)
	customer_info = FT_Customer_Info(organization=organization, src_address=src_address,
		dst_address=dst_address, src_address_int=src_address_int, dst_address_int=dst_address_int,
		customer_name=customer_name, customer_address=customer_address, customer_type=customer_type, line_code=line_code)
	result = FT_Customer_Info.addCustomerInfo(customer_info)
	print(result)
	result = common.trueReturn('', 'failed') if result else common.falseReturn('', 'success')
	return jsonify(result)


@api.route('/dns/get-customer-cloud-count', methods=['POST'])
def getCustomerCloudCount():
	customer_name = request.get_json()['customer_name']
	date = request.get_json()['date']
	query = FT_Customer_Csp_Hourly.getData(FT_Customer_Csp_Hourly, customer_name, date)
	if query:
		result_list = json.loads(json.dumps([x.to_dict() for x in query]))
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

@api.route('/dns/get-customer-cloud-count-chart', methods=['POST'])
def getCustomerCloudCountChart():
	customer_name = request.get_json()['customer_name']
	date = request.get_json()['date']
	query = FT_Customer_Csp_Hourly.getData(FT_Customer_Csp_Hourly, customer_name, date)
	if query:
		query = json.loads(json.dumps([x.to_dict() for x in query]))
		result_dict = {}
		for item in query:
			result_dict.setdefault(item['csp_name'], [0]*24)[item['hour']] = item['count']
		result = common.trueReturn(result_dict, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

@api.route('/dns/get-customer-cloud-count-total', methods=['POST'])
def getCustomerCloudCountTotal():
	customer_name = request.get_json()['customer_name']
	date = request.get_json()['date']
	query = FT_Customer_Csp_Hourly.getSumByHour(FT_Customer_Csp_Hourly, customer_name, date)
	# from IPython import embed;embed()
	if query:
		result_list = [{'csp_name':x[0], 'count': int(x[1])} for x in query]
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

@api.route('/dns/get-customer-top-cloud-tld', methods=['POST'])
def getCustomerTopCloudTld():
	customer_name = request.get_json()['customer_name']
	date = request.get_json()['date']
	query = FT_Customer_Cloud_Domain_Top_Hourly.getTopTldByDate(FT_Customer_Cloud_Domain_Top_Hourly, customer_name, date, 5)
	if query:
		result_list = [{'customer_name':x[0], 'tld':x[1], 'count': int(x[2]), 'csp_name': x[3]} for x in query]
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

@api.route('/dns/get-customer-top-cloud-service-name', methods=['POST'])
def getCustomerTopCloudServiceName():
	customer_name = request.get_json()['customer_name']
	date = request.get_json()['date']
	query = FT_Customer_Cloud_Domain_Top_Hourly.getTopServiceName(FT_Customer_Cloud_Domain_Top_Hourly, customer_name, date, 5)
	if query:
		result_list = [{'customer_name':x[0], 'service_name':x[1], 'count': int(x[2]), 'csp_name': x[3]} for x in query]
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)

@api.route('/dns/get-customer-top-not-cloud-tld', methods=['POST'])
def getCustomerTopNotCloudTld():
	customer_name = request.get_json()['customer_name']
	date = request.get_json()['date']
	query = FT_Customer_Not_Cloud_Domain_Top_Hourly.getTopTldByDate(FT_Customer_Not_Cloud_Domain_Top_Hourly, customer_name, date, 5)
	if query:
		result_list = [{'customer_name':x[0], 'tld':x[1], 'count': int(x[2])} for x in query]
		result = common.trueReturn(result_list, 'success')
	else:
		result = common.falseReturn('', 'failed')
	return jsonify(result)


# @api.route('/dns/get-customer-info-detail', methods=['POST'])
# def getCustomerInfoDetail():
# 	customer_name = request.get_json()['customer_name']
# 	ipaddress = request.get_json()['ipaddress']
# 	line_code = request.get_json()['line_code']
# 	query = Dm_Customer.getCustomerInfo(Dm_Customer, ipaddress, customer_name, line_code)
# 	if query:
# 		result_list = json.dumps(query)
# 		# result_list = [{'organization':x[0], 'src_address':x[1], 'dst_address': x[2], 'mode': x[3], 'customer_name': x[4],
# 		# 	'customer_address': x[5], 'customer_type': x[6], 'line_code': x[7]} for x in query]
# 		# result_list = json.loads(json.dumps([x.to_dict() for x in query]))
# 		result = common.trueReturn(result_list, 'success')
# 	else:
# 		result = common.falseReturn('', 'failed')
# 	return jsonify(result)