from flask_restful import Resource, reqparse
from flask import jsonify, request
from flask import abort, make_response
from app.models import Users
from . import api
from .. import common
from app.auth.auth import Auth


dict_role = {0: '超级管理员', 1: '管理员', 2:'用户'}

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

# 修改用户信息
@api.route('/changeInfo', methods=['PATCH'])
def changeInfo():
    pass

# 获取用户信息
@api.route('/user', methods=['GET'])
def getUserInfo():
    """
    获取用户信息
    :return: JSON
    """
    result = Auth.identify(Auth, request)
    if result['status'] and result['data']:
        user = Users.get(Users, str(result['data']))
        returnUser = {
            'id': user.id,
            'username': user.username,
            'login_time': user.login_time,
            # 'email': user.email,
            'mobile': user.mobile,
            'role': user.role,
            'name': user.name
        }
        result = common.trueReturn(returnUser, "请求成功")
    return jsonify(result)

@api.route('/alluser', methods=['GET'])
def getAllUserInfo():
    '''
    获取所有用户信息
    :return:JSON
    '''
    result = Auth.identify(Auth, request)
    if result['status']:
        allUser = Users.getAll(Users)
        userList = []
        for user in allUser:
            userDict = {}
            userDict['username'] = user.username
            userDict['login_time'] = user.login_time
            # userDict['email'] = user.email
            userDict['department'] =  user.department
            # userDict['role'] = user.role
            userDict['name'] = user.name
            userDict['mobile'] = user.mobile
            if user.role in dict_role.keys():
                userDict['role'] = dict_role[user.role]
            userList.append(userDict)
        result = common.trueReturn(userList, "请求成功")
    return jsonify(result)



@api.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({'error': 'Unauthorized'}), 401)
