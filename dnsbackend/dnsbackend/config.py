class Config(object):
    """Base config class."""
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    DEBUG = True
    # MySQL connection
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://gdnoc:123456Qw!@127.0.0.1:3306/test_system'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456Qw!@127.0.0.1:33066/test_system'
    SQLALCHEMY_BINDS = {
        'dns':'mysql+pymysql://kfsyy:Kfsyy@2017@132.96.82.7:3306/dns',
        'dns_local': 'mysql+pymysql://gdnoc:123456Qw!@127.0.0.1:3306/dns',
        'dns_zx': 'mysql+pymysql://gdnoc:123456Qw!@127.0.0.1:3306/dns_zx',
        'dns_topn': 'mysql+pymysql://gdnoc:123456Qw!@127.0.0.1:3306/dns_topn'
    }
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gdnoc1@Dns@)!&@121.10.40.154:33066/test_system'
    # SQLALCHEMY_BINDS = {
    #     'dns_local':'mysql+pymysql://root:gdnoc1@Dns@)!&@121.10.40.154:33066/dns',
    #     'dns_zx':'mysql+pymysql://root:gdnoc1@Dns@)!&@121.10.40.154:33066/dns_zx1'
    # }
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SECRET_KEY = 'gdnoc'
    SQLALCHEMY_POOL_SIZE = 100
