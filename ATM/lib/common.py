import logging.config
from conf import settings
import hashlib

# 用户认证装饰器
def auth(func):
    from core import src
    def inner(*args, **kwargs):
        # 调用被装饰函数前需要做的操作
        if src.user_info['name']:
            res = func(*args, **kwargs)
            # 调用被装饰函数后需要做的操作
            return res

        else:
            src.login()

    return inner


# 获取日志功能实例
def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(name)  # 创建log实例
    return logger


# 加密功能
def get_md5(pwd):
    # 加点料
    string = '天王盖地虎'

    # 创建加密工厂
    md5 = hashlib.md5()

    # 把密码传入加密工厂里加密
    md5.update(pwd.encode('utf8'))
    md5.update(string.encode('utf8'))

    # 把加密后的结果返回
    return md5.hexdigest()

# print(get_md5('123'))




