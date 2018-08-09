from flask_sqlalchemy import SQLAlchemy
from IPy import IP


db = SQLAlchemy()

def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
db.Model.to_dict = to_dict

def session_commit():
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        reason = str(e)
        return reason

class IP_Table(db.Model):
    __tablename__ = 'ip_table'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50))
    ipAddress = db.Column(db.String(50))
    isOccupied = db.Column(db.Integer)
    type = db.Column(db.Integer)

    def __repr__(self):
        return "<Model ip `{}`>".format(self.ipAddress)

    def add(self, ipInfo):
        db.session.add(ipInfo)
        return session_commit()


class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    # email = db.Column(db.String(255))
    role = db.Column(db.Integer)
    name = db.Column(db.String(50))
    login_time = db.Column(db.DateTime())
    # mobile = db.Column(db.String(11))
    department = db.Column(db.String(20))

    # def __repr__(self):
    #     return "Users(login_time='%s')" % self.login_time

    def get(self, id):
        return self.query.filter_by(id=id).first()

    def getAll(self):
        return self.query.all()

    def getUser(self, username):
        return self.query.filter_by(username=username).all()

    def add(user):
        db.session.add(user)
        return session_commit()

    def delete(self, id):
        self.query.filter_by(id=id).delete()
        return session_commit()

    def update(self):
        return session_commit()


class Privilege(db.Model):
    __tablename__ = 'privilege'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    # privilege_name = db.Column(db.String(255))
    # path = db.Column(db.String(255))
    # component = db.Column(db.String(255))
    privilege_id = db.Column(db.Integer)

    def getPrivileges(self, userid):
        return self.query.filter_by(userid=userid).all()

    def getUser(self, userid):
        return self.query.filter_by(userid=userid).all()

    def add(privilege):
        db.session.add(privilege)
        return session_commit()

    def addAll(privilege):
        db.session.add_all(privilege)
        return session_commit()

    def delete(self, userid):
        self.query.filter_by(userid=userid).delete()
        return session_commit()


class Privilege_Map(db.Model):
    __tablename__ = 'privilege_map'
    id = db.Column(db.Integer, primary_key=True)
    privilege_name = db.Column(db.String(255))
    path = db.Column(db.String(255))
    component = db.Column(db.String(255))

    def getPrivilege(self, id):
        return self.query.filter_by(id=id).first()

# class Topn_Domain(db.Model):
#     __tablename__ = 'dns_top'
#     # id = db.Column(db.Integer, primary_key=True)
#     domain = db.Column(db.String(255))
#     resolved_ip = db.Column(db.String(255))
#     count = db.Column(db.Integer)
#     date = db.Column(db.String(255))
#     rank = db.Column(db.Integer)

#     def __repr__(self):
#         return "Topn_Domain(domain='%s')" % self.domain

#     def get(self, count):
#         return self.query.filter(self.rank <= count).all()


class FT_Domain_Top_Daily(db.Model):
    __tablename__ = 'ft_domain_top_daily'
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255))
    stld = db.Column(db.String(255))
    tld = db.Column(db.String(255))
    resolved_ip = db.Column(db.String(255))
    category_name = db.Column(db.String(255))
    service_name = db.Column(db.String(255))
    count = db.Column(db.BigInteger)
    rank = db.Column(db.Integer)
    category_rank = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.String(255))
    update_time = db.Column(db.DateTime())

    def __repr__(self):
        return "FT_Domain_Top_Daily(domain='%s')" % self.domain

    def get_rank(self, rank, date):
        return self.query.filter(self.rank <= rank).filter_by(date=date).order_by(self.rank).all()

    def get_date(self, date1, date2):
        return self.query.filter(and_(self.date >= date1, self.date <= date2)).all()

    def get_distinct_category(self):
        query = db.session.query(self.category_name).distinct().all()
        category_name = []
        for item in query:
            name = item[0]
            category_name.append(name)
        return category_name

    def get_category_rank(self, category_name, count, date):
        return self.query.filter_by(category_name=category_name).filter_by(date=date)\
            .filter(self.category_rank <= count).order_by(self.category_rank).all()

    '''
    根据category_name对service_name进行聚合，统计每个首页的总数
    '''
    def get_category_group(self, category_name, date, count):
        query = db.session.query(self.service_name, db.func.sum(self.count).label('count_all')).filter_by(date=date)\
            .filter_by(category_name=category_name).group_by(self.service_name).order_by(db.desc(db.func.sum(self.count))).limit(count)
        group_result = {}
        tmp1 = []
        tmp2 = []
        tmp3 = []
        for item in query:
            tmp = {}
            tmp1.append(item[0])
            tmp2.append(int(item[1]))
            tmp['name'] = item[0]
            tmp['value'] = int(item[1])
            tmp3.append(tmp)
        group_result['name'] = tmp1
        group_result['value'] = tmp2
        group_result['all'] = tmp3
        return group_result

    '''
    获取该域名的解析量数据
    '''
    def get_domain_count(self, domain):
        return self.query.filter_by(domain=domain).order_by(db.desc(self.date)).all()

    def get_domain_count_limit(self, domain, count):
        return self.query.filter_by(domain=domain).order_by(db.desc(self.date)).limit(count)

class FT_Domain_Top_Weelkly(db.Model):
    __tablename__ = 'ft_domain_top_weekly'
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255))
    stld = db.Column(db.String(255))
    tld = db.Column(db.String(255))
    resolved_ip = db.Column(db.String(255))
    category_name = db.Column(db.String(255))
    service_name = db.Column(db.String(255))
    count = db.Column(db.BigInteger)
    rank = db.Column(db.Integer)
    category_rank = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    week = db.Column(db.String(255))
    update_time = db.Column(db.DateTime())

    def __repr__(self):
        return "FT_Domain_Top_Weelkly(domain='%s')" % self.domain

    def get_rank(self, rank, week):
        return self.query.filter(self.rank <= rank).filter_by(week=week).order_by(self.rank).all()

    # def get_date(self, date1, date2):
    #     return self.query.filter(and_(self.date >= date1, self.date <= date2)).all()

    def get_distinct_category(self):
        query = db.session.query(self.category_name).distinct().all()
        category_name = []
        for item in query:
            name = item[0]
            category_name.append(name)
        return category_name

    def get_category_rank(self, category_name, count, week):
        return self.query.filter_by(category_name=category_name).filter_by(week=week)\
            .filter(self.category_rank <= count).order_by(self.category_rank).all()

    '''
    根据category_name对service_name进行聚合，统计每个首页的总数
    '''
    def get_category_group(self, category_name, count, week):
        query = db.session.query(self.service_name, db.func.sum(self.count).label('count_all')).filter_by(week=week)\
            .filter_by(category_name=category_name).group_by(self.service_name).order_by(db.desc(db.func.sum(self.count))).limit(count)
        print(query)
        group_result = {}
        tmp1 = []
        tmp2 = []
        tmp3 = []
        for item in query:
            tmp = {}
            tmp1.append(item[0])
            tmp2.append(int(item[1]))
            tmp['name'] = item[0]
            tmp['value'] = int(item[1])
            tmp3.append(tmp)
        print(tmp1)
        group_result['name'] = tmp1
        group_result['value'] = tmp2
        group_result['all'] = tmp3
        return group_result


class Domain_IP(db.Model):
    __tablename__ = 'domain_ip'
    id = db.Column(db.Integer, primary_key=True)
    subnet = db.Column(db.String(255))
    domain = db.Column(db.String(255))
    ip = db.Column(db.String(255))
    country = db.Column(db.String(255))
    province = db.Column(db.String(255))
    operator = db.Column(db.String(255))
    update_time = db.Column(db.DateTime())

    def __repr__(self):
        return "Domain_IP(ip='%s')" % self.domain

    def inverse_ip_query(self, ip):
        return self.query.filter_by(ip=ip).all()

    def inverse_ip_list_query(self, iplist):
        result_list = []
        for ip in iplist:
            query = self.query.filter_by(ip=ip).first()
            print(query)
            if query:
                d = {}
                d['resolved_ip'] = query.ip
                d['subnet'] = query.subnet
                d['country'] = query.country
                d['province'] = query.province
                d['operator'] = query.operator
                result_list.append(d)
        return result_list



class Dm_Domain_IP(db.Model):
    __tablename__ = 'dm_domain_ip'
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255))
    stld = db.Column(db.String(255))
    tld = db.Column(db.String(255))
    resolved_ip = db.Column(db.String(255))
    category_name = db.Column(db.String(255))
    service_name = db.Column(db.String(255))
    subnet = db.Column(db.String(255))
    country = db.Column(db.String(255))
    province = db.Column(db.String(255))
    operator = db.Column(db.String(255))
    update_time = db.Column(db.DateTime())

    def __repr__(self):
        return "Domain_IP(domain='%s')" % self.domain

    '''
    本省非电信ISP统计
    '''
    def isp_statistics_exp_telecom(self):
        query = db.session.query(self.operator, db.func.count(self.domain).label('count')).filter(self.province=='广东省').group_by(self.operator)
        result_list = []
        for item in query:
            if item[0] != '中国电信':
                tmp = {}
                tmp['name'] = item[0]
                tmp['value'] = item[1]
                result_list.append(tmp)
        return result_list

    '''
    IP列表查对对应的ISP信息
    '''
    def inverse_ip_list_query(self, iplist):
        result_list = []
        for ip in iplist:
            query = self.query.filter_by(resolved_ip=ip).first()
            print(query)
            if query:
                d = {}
                d['resolved_ip'] = query.resolved_ip
                d['subnet'] = query.subnet
                d['country'] = query.country
                d['province'] = query.province
                d['operator'] = query.operator
                result_list.append(d)
        return result_list


class Key_Domain(db.Model):
    __tablename__ = 'key_domain'
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255))
    legal_ip = db.Column(db.String(255))
    # update_time = db.Column(db.DateTime())

    def __repr__(self):
        return "Key_Domain(domain='%s')" % self.domain

    def add(self, Key_Domain):
        db.session.add(Key_Domain)
        return session_commit()

    def getAllDomain(self):
        return self.query.all()

    def getSingleDomain(self, domain):
        return self.query.filter_by(domain=domain).all()

    def getSingleDomainById(self, id):
        return self.query.filter_by(id=id).first()

    def deleteSelectDomain(self, id):
        self.query.filter_by(id=id).delete()
        return session_commit()

    def updateSelectDomain():
        return session_commit()


class Dm_Tld_ICP(db.Model):
    __tablename__ = 'dm_tld_icp'
    id = db.Column(db.Integer, primary_key=True)
    tld = db.Column(db.String(255))
    name = db.Column(db.String(255))
    siteBeianCode = db.Column(db.String(255))
    companyBeianCode = db.Column(db.String(255))

    def __repr__(self):
        return "Dm_Tld_ICP(tld='%s')" % self.tld

    def getICPInfo(self, tld):
        return self.query.filter_by(tld=tld).first()

    def getICPInfoBySiteBeianCode(self, siteBeianCode):
        return self.query.filter_by(siteBeianCode=siteBeianCode).all()

    def getICPInfoByCompanyBeianCode(self, companyBeianCode):
        return self.query.filter_by(companyBeianCode=companyBeianCode).all()

    def getICPInfoByBeianCode(self, beianCode):
        # query = db.session.query.filter(or_(self.companyBeianCode==beianCode, self.siteBeianCode==beianCode)).all()
        # return query
        # print(self.query.filter(self.companyBeianCode==beianCode | self.siteBeianCode==beianCode))
        return self.query.filter((self.companyBeianCode==beianCode) | (self.siteBeianCode==beianCode)).all()
        #return self.query.filter(db.func.or_(self.companyBeianCode==beianCode, self.siteBeianCode=='')).all()


class Dm_Tld_Whois(db.Model):
    __tablename__ = 'dm_tld_whois'
    id = db.Column(db.Integer, primary_key=True)
    tld = db.Column(db.String(255))
    domain_name = db.Column(db.String(255))
    registrar = db.Column(db.String(255))
    name = db.Column(db.String(255))
    emails = db.Column(db.String(255))
    address = db.Column(db.String(255))
    status = db.Column(db.Text())
    dnssec = db.Column(db.String(255))
    name_servers = db.Column(db.Text())
    referral_url = db.Column(db.String(255))
    whois_server = db.Column(db.String(255))
    org = db.Column(db.String(255))
    country = db.Column(db.String(255))
    state = db.Column(db.String(255))
    city = db.Column(db.String(255))
    zipcode = db.Column(db.String(255))
    text = db.Column(db.Text())
    updated_date = db.Column(db.String(255))
    creation_date = db.Column(db.String(255))
    expiration_date = db.Column(db.String(255))

    def getTldWhois(self, tld):
        return self.query.filter_by(tld=tld).first()


class Ag_Statistics_Daily(db.Model):
    __tablename__ = 'ag_statistics_daily'
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.BigInteger)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)

    def getAgStatistics(self,count):
        return self.query.order_by(db.desc(self.date)).limit(count)


class Dm_Domain_Route(db.Model):
    __tablename__ = 'dm_domain_route'
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255))
    route = db.Column(db.Text())
    route_raw = db.Column(db.Text())

    def getRoute(self, domain):
        return self.query.filter_by(domain=domain).all()


class Map_Ems_IP(db.Model):
    __bind_key__ = 'auditsystem'
    __tablename__ = 'map_ems_ip'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(255))
    model = db.Column(db.String(255))
    OS = db.Column(db.String(255))
    node = db.Column(db.String(255))
    loopback = db.Column(db.String(255))
    property = db.Column(db.String(255))

    def getInfo(self, loopback, hostname, model=''):
        if model == '':
            return self.query.filter(self.loopback.like('%' + loopback + '%')).filter(self.hostname.like('%' + hostname + '%')).all()
        else:
            return self.query.filter(self.loopback.like('%' + loopback + '%')).filter(self.hostname.like('%' + hostname + '%')).filter_by(model=model).all()



    def getModel(self):
        query = db.session.query(self.model).distinct().all()
        model_name = []
        for item in query:
            name = item[0]
            model_name.append(name)
        return model_name


# class Interface_Info_Copy(db.Model):
#     __bind_key__ = 'auditsystem'
#     __tablename__ = 'interface_info_copy'
#     id = db.Column(db.Integer, primary_key=True)
#     hostname = db.Column(db.String(255))
#     loopback = db.Column(db.String(255))
#     interface = db.Column(db.String(255))
#     description = db.Column(db.String(255))
#     ipv4address = db.Column(db.String(255))
#     ipv6address = db.Column(db.String(255))
#     rate = db.Column(db.String(255))
#     date = db.Column(db.String(255))

#     def getInfo(self, loopback, hostname, date):
#         return self.query.filter(self.loopback.like('%' + loopback + '%')).filter(self.hostname.like('%' + hostname + '%')).filter_by(date=date).all()


class FT_Customer_Csp_Hourly(db.Model):
    # __bind_key__ = 'dns'
    __tablename__ = 'ft_customer_csp_hourly'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255))
    csp_name = db.Column(db.String(255))
    count = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.String(255))
    hour = db.Column(db.Integer)

    def getData(self, customer_name, date):
        return self.query.filter_by(customer_name=customer_name).filter_by(date=date).order_by(self.hour).all()

    def getCustomerName(self):
        query = db.session.query(self.customer_name).distinct().all()
        customer_name = [x[0] for x in query]
        return customer_name

    def getSumByHour(self, customer_name, date):
        return db.session.query(self.csp_name, db.func.sum(self.count).label('count')).filter(self.date==date).filter(self.csp_name != '非云').group_by(self.csp_name)

'''
专线客户信息表
'''
class FT_Customer_Info(db.Model):
    # __bind_key__ = 'dns'
    # __tablename__ = 'ft_customer_info'
    __tablename__ = 'dm_customer'
    id = db.Column(db.Integer, primary_key=True)
    organization = db.Column(db.String(255))
    src_address = db.Column(db.String(255))
    dst_address = db.Column(db.String(255))
    src_address_int = db.Column(db.Integer)
    dst_address_int = db.Column(db.Integer)
    mode = db.Column(db.String(255))
    customer_name = db.Column(db.String(255))
    customer_address = db.Column(db.String(255))
    customer_type = db.Column(db.String(255))
    line_code = db.Column(db.String(255))
    # update_time = db.Column(db.String(255))

    # 获取客户的名称
    def getCustomerName(self):
        query = db.session.query(self.customer_name).distinct().all()
        customer_name = [x[0] for x in query]
        return customer_name

    # 精确搜索客户信息
    def getCustomerInfoAccurate(self, customer_name):
        return self.query.filter_by(customer_name=customer_name).all()

    # 根据ID查找客户
    def getCustomerInfoById(self, id):
        return self.query.filter_by(id=id).first()

    # 模糊搜索客户信息
    def getCustomerInfo(self, customer_name, ipaddress, line_code):
        if ipaddress:
            ipToInt = IP(ipaddress).int()
            return self.query.filter(self.customer_name.like('%' + customer_name + '%')).filter(self.line_code.like('%' + line_code + '%'))\
                .filter(self.src_address_int <= ipToInt).filter(self.dst_address_int >= ipToInt)
        else:
            return self.query.filter(self.customer_name.like('%' + customer_name + '%')).filter(self.line_code.like('%' + line_code + '%')).all()

    # 新增客户信息
    def addCustomerInfo(customer_info):
        db.session.add(customer_info)
        return session_commit()

    # 删除客户信息
    def deleteCustomerInfo(self, id):
        self.query.filter_by(id=id).delete()
        return session_commit()

    # 更新客户信息
    def updateCustomerInfo():
        return session_commit()

class FT_Customer_Cloud_Domain_Top_Hourly(db.Model):
    # __bind_key__ = 'dns'
    __tablename__ = 'ft_customer_cloud_domain_top_hourly'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255))
    domain = db.Column(db.String(255))
    stld = db.Column(db.String(255))
    tld = db.Column(db.String(255))
    resolved_ip = db.Column(db.String(255))
    category_name = db.Column(db.String(255))
    service_name = db.Column(db.String(255))
    count = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    ip_address_field = db.Column(db.String(255))
    csp_name = db.Column(db.String(255))
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    update_time = db.Column(db.String(255))

    def getTopTldByDate(self, customer_name, date, n):
        return db.session.query(self.customer_name, self.tld, db.func.sum(self.count).label('sum'), self.csp_name)\
            .filter_by(customer_name=customer_name).filter_by(date=date).group_by(self.tld).order_by(db.desc(db.func.sum(self.count))).limit(n)

    def getTopServiceName(self, customer_name, date, n):
        return db.session.query(self.customer_name, self.service_name, db.func.sum(self.count).label('sum'), self.csp_name).filter(self.service_name !='')\
            .filter_by(customer_name=customer_name).filter_by(date=date).group_by(self.service_name).order_by(db.desc(db.func.sum(self.count))).limit(n)

    def getTopDomainByDate(self, customer_name, date, n):
        return db.session.query(self.customer_name, self.domain, db.func.sum(self.count).label('sum'), self.csp_name)\
            .filter_by(customer_name=customer_name).filter_by(date=date).group_by(self.domain).order_by(db.desc(db.func.sum(self.count))).limit(n)

class FT_Customer_Not_Cloud_Domain_Top_Hourly(db.Model):
    # __bind_key__ = 'dns'
    __tablename__ = 'ft_customer_not_cloud_domain_top_hourly'
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255))
    domain = db.Column(db.String(255))
    stld = db.Column(db.String(255))
    tld = db.Column(db.String(255))
    resolved_ip = db.Column(db.String(255))
    category_name = db.Column(db.String(255))
    service_name = db.Column(db.String(255))
    count = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    ip_address_field = db.Column(db.String(255))
    csp_name = db.Column(db.String(255))
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    update_time = db.Column(db.String(255))

    def getTopTldByDate(self, customer_name, date, n):
        return db.session.query(self.customer_name, self.tld, db.func.sum(self.count).label('sum'))\
            .filter_by(customer_name=customer_name).filter_by(date=date).group_by(self.tld).order_by(db.desc(db.func.sum(self.count))).limit(n)

    def getTopDomainByDate(self, customer_name, date, n):
        return db.session.query(self.customer_name, self.domain, db.func.sum(self.count).label('sum'))\
            .filter_by(customer_name=customer_name).filter_by(date=date).group_by(self.domain).order_by(db.desc(db.func.sum(self.count))).limit(n)

# class Dm_Customer(db.Model):
#     __bind_key__ = 'dns'
#     __tablename__ = 'dm_customer'
#     id = db.Column(db.Integer, primary_key=True)
#     organization = db.Column(db.String(255))
#     src_address = db.Column(db.String(255))
#     dst_address = db.Column(db.String(255))
#     mode = db.Column(db.String(255))
#     customer_name = db.Column(db.String(255))
#     customer_address = db.Column(db.String(255))
#     customer_type = db.Column(db.String(255))
#     line_code = db.Column(db.String(255))
#     update_time = db.Column(db.String(255))

#     def getCustomerInfo(self, ipaddress, customer_name, line_code):
#         if ipaddress:
#             ipToInt = IP(ipaddress).int()
#             return self.query.filter(self.customer_name.like('%' + customer_name + '%')).filter_by(line_code=line_code)\
#                 .filter(self.src_address <= ipToInt).filter(self.dst_address >= ipToInt)
#         else:
#             return self.query.filter(self.customer_name.like('%' + customer_name + '%')).filter_by(line_code=line_code).all()




class Agg_Subscriber_Csp_Hourly(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_subscriber_csp_hourly'
    id = db.Column(db.Integer, primary_key=True)
    subscriber_name = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    update_time = db.Column(db.String(255))


class Agg_Subscriber_Csp_Cloud_Daily(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_subscriber_csp_cloud_daily'
    id = db.Column(db.Integer, primary_key=True)
    subscriber_name = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)
    # update_time = db.Column(db.String(255))

    # 取出表中的所有日期，返回日期列表
    def getLast7Day(self):
        query = db.session.query(self.date).distinct().all()
        date_list = [x[0] for x in query]
        date_list.sort()
        date_list = date_list[-7:] if len(date_list) > 7 else date_list
        return date_list

    # 取出符合条件的某一天数据
    # 条件：resolved_ip_network，date，按照resolved_number进行降序, 取前十
    def getAggSubscriberCspCloudDaily(self, date, resolved_ip_network):
        return self.query.filter_by(resolved_ip_network=resolved_ip_network).filter_by(date=date).order_by(db.desc(self.resolved_number)).limit(10)

    # 取出符合条件的某个周期数据
    # 条件：resolved_ip_network，date，按照resolved_number进行降序, 取前十
    def getAggSubscriberCspCloudDaily_period(self, period):
        query = db.session.query(self.subscriber_name, self.resolved_ip_network, db.func.sum(self.resolved_number)).\
                filter(self.date >= period[0]).filter(self.date <= period[1]).\
                group_by(self.resolved_ip_network).group_by(self.subscriber_name).\
                order_by(db.desc(db.func.sum(self.resolved_number))).\
                all()
        return query

# 用户访问公有云情况每周汇总
class Agg_Subscriber_Csp_Cloud_Weekly(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_subscriber_csp_cloud_weekly'
    id = db.Column(db.Integer, primary_key=True)
    subscriber_name = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    # update_time = db.Column(db.String(255))

    # 取出符合条件的某个周期数据
    # 如果设定了resolved_ip_network，则取出该resolved_ip_network的前十，否则的话，取不带公有云的前十
    def getAggSubscriberCspCloudWeekly(self, date, resolved_ip_network=None):
        if resolved_ip_network:
            return self.query.filter_by(resolved_ip_network=resolved_ip_network).filter_by(date=date).filter(self.rank <= 10).all()
        else:
            return self.query.filter_by(date=date).filter(self.resolved_ip_network != '公有云').filter(self.rank <= 10).all()

class Agg_Csp_Hourly(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_csp_hourly'
    id = db.Column(db.Integer, primary_key=True)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    # update_time = db.Column(db.String(255))


class Agg_Csp_Daily(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_csp_daily'
    id = db.Column(db.Integer, primary_key=True)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)
    # update_time = db.Column(db.String(255))

    def getLast7Day(self):
        query = db.session.query(self.date).distinct().all()
        date_list = [x[0] for x in query]
        date_list.sort(reverse=True)
        return date_list

    def getAggCspDaily(self, date, resolved_ip_network=None):
        if resolved_ip_network:
            return self.query.filter_by(resolved_ip_network=resolved_ip_network).filter_by(date=date).all()
        else:
            return self.query.filter(self.resolved_ip_network != '公有云').filter_by(date=date).all()

class Agg_Csp_Weekly(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_csp_weekly'
    id = db.Column(db.Integer, primary_key=True)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)

    def getAggCspWeekly(self, date, resolved_ip_network=None):
        if resolved_ip_network:
            return self.query.filter_by(resolved_ip_network=resolved_ip_network).filter_by(date=date).all()
        else:
            return self.query.filter(self.resolved_ip_network != '公有云').filter_by(date=date).all()


class Agg_Subscriber_Organization_And_Resolved_Ip_Network_Hourly(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_subscriber_organization_and_resolved_ip_network_hourly'
    id = db.Column(db.Integer, primary_key=True)
    subscriber_organization = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)

class Agg_Subscriber_Organization_And_Resolved_Ip_Network_Daily(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_subscriber_organization_and_resolved_ip_network_daily'
    id = db.Column(db.Integer, primary_key=True)
    subscriber_organization = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)

    def getAggSubscriberOrganizationAndResolvedIpNetworkDaily(self, date, resolved_ip_network=None):
        if resolved_ip_network:
            return self.query.filter_by(date=date).filter_by(resolved_ip_network=resolved_ip_network).all()
        else:
            return self.query.filter_by(date=date).filter(self.resolved_ip_network != '公有云').filter(self.resolved_ip_network != '非云').all()


class Agg_Subscriber_Organization_And_Resolved_Ip_Network_Weekly(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_subscriber_organization_and_resolved_ip_network_weekly'
    id = db.Column(db.Integer, primary_key=True)
    subscriber_organization = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)

    def getAggSubscriberOrganizationAndResolvedIpNetworkWeekly(self, date, resolved_ip_network=None):
        if resolved_ip_network:
            return self.query.filter_by(date=date).filter_by(resolved_ip_network=resolved_ip_network).all()
        else:
            return self.query.filter_by(date=date).filter(self.resolved_ip_network != '公有云').filter(self.resolved_ip_network != '非云').all()


class Agg_Is_Focused_Domain_Category_Hourly(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_is_focused_domain_category_hourly'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)
    hour = db.Column(db.Integer)

class Agg_Is_Focused_Domain_Category_Daily(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_is_focused_domain_category_daily'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)

    def getAggIsFocusedDomainCategoryDaily(self, date):
        return self.query.filter_by(date=date).all()


class Agg_Is_Focused_Domain_Category_Weekly(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_is_focused_domain_category_weekly'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)

    def getAggIsFocusedDomainCategoryWeekly(self, date):
        return self.query.filter_by(date=date).all()

class Agg_Is_Focused_Domain_Daily(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_is_focused_domain_daily'
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.Text)
    category = db.Column(db.Text)
    website_name = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)

    def getAggIsFocusedDomainDaily(self, date, category=None):
        if category:
            return self.query.filter_by(category=category).filter_by(date=date).all()
        else:
            return self.query.filter_by(date=date).all()

class Agg_Is_Focused_Domain_Weekly(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_is_focused_domain_weekly'
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.Text)
    category = db.Column(db.Text)
    website_name = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)

    def getAggIsFocusedDomainWeekly(self, date, category=None):
        if category:
            return self.query.filter_by(category=category).filter_by(date=date).all()
        else:
            return self.query.filter_by(date=date).all()


class Agg_Subscriber_City_And_Resolved_Ip_Network_Daily(db.Model):
    __bind_key__ = 'dns_local'
    __tablename__ = 'agg_subscriber_city_and_resolved_ip_network_daily'
    id = db.Column(db.Integer, primary_key=True)
    subscriber_city = db.Column(db.Text)
    resolved_ip_network = db.Column(db.Text)
    resolved_number = db.Column(db.Integer)
    success_number = db.Column(db.Integer)
    success_rate = db.Column(db.Float)
    date = db.Column(db.Integer)

    def getAggSubscriberCityAndResolvedIpNetworkDaily(self, date, resolved_ip_network=None):
        if resolved_ip_network:
            return self.query.filter_by(resolved_ip_network=resolved_ip_network).filter_by(date=date).all()
        else:
            return self.query.filter_by(date=date).filter(self.resolved_ip_network != '非云').all()