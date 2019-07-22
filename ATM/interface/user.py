'''
    用户接口层
'''


from db import db_handler
from lib import common

logger = common.get_logger('user')


# 注册接口
def register_interface(name, pwd, balance=15000):  # 默认额度15000

    # 调用数据处理层拿到用户信息
    user_dic = db_handler.select(name)

    # 判断用户信息是否存在
    if user_dic:  # user信息， False
        logger.info('用户: [%s] 已存在!' % name)
        return False, '用户已存在'

    # 加密用户输入的密码
    md5_pwd = common.get_md5(pwd)

    user_dic = {
        'name': name, 'pwd': md5_pwd, 'balance': balance,  'flow': [], 'shopping_cart': {}
    }

    db_handler.save(user_dic)

    logger.info('用户: [%s] 注册成功!' % name)

    return True, '注册成功!'  # (True, '注册成功!')


# 登录接口
def login_interface(name, pwd):
    # 用户信息 / None
    user_dic = db_handler.select(name)

    if not user_dic:

        return False, '用户不存在!'

    md5_pwd = common.get_md5(pwd)

    if md5_pwd == user_dic['pwd']:
        return True, '登录成功!'

    else:
        return False, '密码错误!'


# 查看用户余额接口
def check_balance_interface(name):
    # 用户信息 / None
    user_dic = db_handler.select(name)
    if not user_dic['balance']:
        return '穷逼..'

    return user_dic['balance']


# 注销接口
def logout_interface():
    from core import src
    src.user_info['name'] = None
    return '注销成功!'

