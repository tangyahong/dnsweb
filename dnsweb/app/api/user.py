from flask import jsonify, request, g
from flask import abort, make_response
from app.models.models import *
# from app.models import Users, Privilege, Privilege_Map,IP_Table1
from . import api
from .. import common
from app.auth.auth import Auth
import json
from functools import wraps, update_wrapper
# import redis
# import time
from app.api.decorator import *


dict_role = { 0:'管理员', 1:'用户' }
dict_role_rev = { '管理员':0, '用户':1 }

# 用户注册
@api.route('/register', methods=['POST'])
def register():
    pass

# 用户登陆
@api.route('/login', methods=['POST'])
def login():
    username = request.get_json()['username']
    password = request.get_json()['password']
    if (not username or not password):
        return jsonify(common.falseReturn('', '用户名和密码不能为空'))
    else:
        return Auth.authenticate(Auth, username, password)

# 获取用户信息
@api.route('/user', methods=['GET'])
def getUserInfo():
    result = Auth.identify(Auth, request)
    if result['status'] and result['data']:
        user = Users.get(Users, str(result['data']['userid']))
        returnUser = {
            'id': user.id,
            'username': user.username,
            'login_time': user.login_time,
            'department': user.department,
            'role': user.role,
            'name': user.name
        }
        result = common.trueReturn(returnUser, "success")
    else:
        result = common.falseReturn('', 'failed')
    return jsonify(result)

@api.route('/get-user', methods=['POST'])
@login_required
def getUser():
    username = request.get_json()['username']
    if username:
        query = Users.getUser(Users, username)
    else:
        query = Users.getAll(Users)
    if query:
        result_list = []
        for item in query:
            d = {}
            d['id'] = item.id
            d['username'] = item.username
            d['name'] = item.name
            d['role'] = dict_role[item.role]
            d['login_time'] = item.login_time
            d['department'] = item.department
            result_list.append(d)
        result = common.trueReturn(result_list, "success")
    else:
        result = common.falseReturn('', 'failed')
    return jsonify(result)

# 获取用户权限
@api.route('/get-privilege', methods=['POST'])
@login_required
def getPrivilege():
    id = request.get_json()['id']
    query = Users.get(Users, id)
    if query:
        userid = query.id
        query = Privilege.getPrivileges(Privilege, userid)
        result_list = []
        for item in query:
            result_list.append(Privilege_Map.getPrivilege(Privilege_Map, item.privilege_id).id)
        result = common.trueReturn(result_list, "success")
    else:
        result = common.falseReturn('', 'failed')
    return jsonify(result)


@api.route('/identify-menu', methods=['GET'])
@login_required
@ratelimit(limit=10, per=60 * 15)
def userIdentifyMenu():
    result = Auth.identify(Auth, request)
    if result['status'] and result['data']:
        user = Users.get(Users, str(result['data']['userid']))
        query = Privilege.getPrivileges(Privilege, user.id)
        result_list = []
        for item in query:
            result_list.append(Privilege_Map.getPrivilege(Privilege_Map, item.privilege_id).path)
        result = common.trueReturn(result_list, "success")
    else:
        result = common.falseReturn('', 'failed')
    return jsonify(result)

#新增用户(权限)
@api.route('/add-user', methods=['POST'])
@admin_required
def addUser():
    username = request.get_json()['username']
    password = request.get_json()['password']
    department = request.get_json()['department']
    name = request.get_json()['name']
    role = request.get_json()['role']
    role = dict_role_rev[role]
    privilege = request.get_json()['privilege']
    user = Users(username=username, password=password, department=department, name=name, role=role)
    result = Users.add(user)
    if result:
        result = common.falseReturn('', "failed")
    else:
        query = Users.getUser(Users, username)
        userid = query[0].id
        privilege_list = []
        for item in privilege:
            privilegeAdd = Privilege(userid=userid, privilege_id=item)
            privilege_list.append(privilegeAdd)
        result = Privilege.addAll(privilege_list)
        if result:
            result = common.falseReturn('', "failed")
        else:
            result = common.trueReturn('', "success")
    return jsonify(result)

# 编辑用户
@api.route('/edit-user/<id>', methods=['POST'])
@admin_required
def editUser(id):
    department = request.get_json()['department']
    name = request.get_json()['name']
    role = request.get_json()['role']
    role = dict_role_rev[role]
    privilege = request.get_json()['privilege']
    query = Users.get(Users, id)
    if query:
        query.department = department
        query.name = name
        query.role = role
        result = Users.update(query)
        if result:
            result = common.falseReturn('', "failed")
        else:
            userid = query.id
            result = Privilege.delete(Privilege, userid)
            if result:
                result = common.falseReturn('', "failed")
            else:
                privilege_list = []
                for item in privilege:
                    privilegeAdd = Privilege(userid=userid, privilege_id=item)
                    privilege_list.append(privilegeAdd)
                result = Privilege.addAll(privilege_list)
                if result:
                    result = common.falseReturn('', "failed")
                else:
                    result = common.trueReturn('', "success")
    else:
        result = common.falseReturn('', "failed")
    return jsonify(result)

@api.route('/del-user', methods=['POST'])
@login_required
def deleteUser():
    id = request.get_json()['id']
    query = Users.get(Users, id)
    userid = query.id
    if query:
        delUser = Users.delete(Users, id)
        if delUser:
            result = common.falseReturn('', "failed")
        else:
            delPrivilege = Privilege.delete(Privilege, userid)
            if delPrivilege:
                result = common.falseReturn('', "failed")
            else:
                result = common.trueReturn('', "success")
    else:
        result = common.falseReturn('', "failed")
    return jsonify(result)

@api.route('/change-password', methods=['POST'])
def changePassword():
    id = request.get_json()['id']
    oldPassword = request.get_json()['oldPassword']
    newPassword = request.get_json()['newPassword']
    confirmPassword = request.get_json()['confirmPassword']
    if newPassword != confirmPassword:
        result = common.falseReturn('新密码输入不一致', "failed")
    else:
        query = Users.get(Users, id)
        if query:
            storedPassword = query.password
            if storedPassword == oldPassword:
                query.password = newPassword
                result = Users.update(query)
                if result:
                    result = common.falseReturn('', "failed")
                else:
                    result = common.trueReturn('', "success")
            else:
                result = common.falseReturn('旧密码不正确！', "failed")
        else:
            result = common.falseReturn('', "failed")
    return jsonify(result)

# 重置密码
@api.route('/reset-password', methods=['POST'])
@admin_required
def resetPassword():
    id = request.get_json()['id']
    query = Users.get(Users, id)
    if query:
        query.password = '3086fd9a018a3e0f01a952e96669e603882a962d' # 12#$%abCDE
        result = Users.update(query)
        if result:
            result = common.falseReturn('', "failed")
        else:
            result = common.trueReturn('', "success")
    else:
        result = common.falseReturn('', "failed")
    return jsonify(result)