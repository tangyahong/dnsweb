import jwt
import datetime
from .. import DevConfig
from app.models.models import Users
from flask import jsonify
from .. import common


class Auth():
    @staticmethod
    def encode_auth_token(user_id, username, login_time, role):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=100),
                'iat': datetime.datetime.utcnow(),
                'iss': '%^6^@hIp',
                'data': {
                    'id': user_id,
                    'username': username,
                    'login_time': login_time,
                    'role': role
                }
            }
            return jwt.encode(payload, DevConfig.SECRET_KEY, algorithm='HS256')
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, DevConfig.SECRET_KEY, options={'verify_exp': False})
            if('data' in payload):
                return  payload
            else:
                raise jwt.InvalidTokenError
        except jwt.InvalidTokenError:
            return '无效token'

    # 用户登陆，成功返回token，失败返回失败原因
    def authenticate(self, username, password):
        userInfo = Users.query.filter_by(username=username).first()
        if(not userInfo):
            return jsonify(common.falseReturn('', '用户名或密码错误'))
        else:
            if(userInfo.password == password):
                # login_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                userInfo.login_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                Users.update(Users)
                token = self.encode_auth_token(userInfo.id, userInfo.username, str(userInfo.login_time), userInfo.role)
                return jsonify(common.trueReturn(token.decode(), '登录成功'))
            else:
                return jsonify(common.falseReturn('', '用户名或密码错误'))

    # 用户鉴权
    def identify(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_tokenArr = auth_header.split(' ')
            if (not auth_tokenArr or auth_tokenArr[0] != 'Bearer' or len(auth_tokenArr) != 2):
                result = common.falseReturn('', '请传递正确的验证头信息')
            else:
                auth_token = auth_tokenArr[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload, str):
                    user = Users.get(Users, payload['data']['id'])
                    if not user:
                        result = common.falseReturn('', '找不到该用户信息')
                    else:
                        if str(user.login_time) == payload['data']['login_time']:
                            result = {
                                'userid': user.id,
                                'role': user.role,
                                'username': user.username
                            }
                            result = common.trueReturn(result, '请求成功')
                        else:
                            result = common.falseReturn('', 'Token已更改')
                else:
                    result = common.falseReturn('', payload)
        else:
            result = common.falseReturn('', '没有提供认证token')
        return result