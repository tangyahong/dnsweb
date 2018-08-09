from functools import wraps, update_wrapper
from app.auth.auth import Auth
from flask import jsonify, request, g
from .. import common
import time
import redis

redis = redis.Redis(host='localhost', port=6379, db=0)

class RateLimit(object):
    expiration_window = 10  # 额外的延时，抵消提交到redis的网络延迟

    def __init__(self, key_prefix, limit, per, send_x_headers):
        self.reset = (int(time.time()) // per) * per + per
        self.key = key_prefix + str(self.reset)
        self.limit = limit
        self.per = per
        self.send_x_headers = send_x_headers

        """
        使用pipeline提交操作
        about redis.pipeline: https://redis.io/topics/pipelining
        """
        p = redis.pipeline()
        p.incr(self.key)
        p.expireat(self.key, self.reset + self.expiration_window)
        self.current = min(p.execute()[0], limit)

    remaining = property(lambda x: x.limit - x.current)   # 剩余查询次数
    over_limit = property(lambda x: x.current >= x.limit)  # 是否超过限制

# def get_view_rate_limit():
#     return getattr(g, '_view_rate_limit', None)

def on_over_limit(limit):
    result = common.falseReturn('Over the limit', 'failed')
    return jsonify(result), 400

def ratelimit(limit, per=300, send_x_headers=True, over_limit=on_over_limit,
              scope_func=lambda: g.username, key_func=lambda: request.endpoint):
    def decorator(f):
        def rate_limited(*args, **kwargs):
            key = 'rate-limit/%s/%s/' % (key_func(), scope_func())   # redis中的键名 默认使用路由端点和用户名
            rlimit = RateLimit(key, limit, per, send_x_headers)
            g._view_rate_limit = rlimit
            if over_limit is not None and rlimit.over_limit:
                return over_limit(rlimit)
            return f(*args, **kwargs)
        return update_wrapper(rate_limited, f)
    return decorator


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        authResult = Auth.identify(Auth, request)
        if authResult['status'] and authResult['data']:
            g.username = authResult['data']['username']
            return f(*args, **kwargs)
        else:
            return jsonify(authResult)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        authResult = Auth.identify(Auth, request)
        if authResult['status'] and authResult['data']['role'] == 0:
            return f(*args, **kwargs)
        else:
            result = common.falseReturn('Permission denied', 'failed')
            return jsonify(result)
    return decorated_function