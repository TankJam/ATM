
from db import db_handler
from lib import common

logger = common.get_logger('bank')


# 提现接口
def withdrwa_interface(name, money):
    user_dic = db_handler.select(name)
    # 判断用户余额是否大于提现金额 * 1.05
    money2 = money * 1.05
    money3 = money * 0.05
    if user_dic['balance'] >= money2:

        user_dic['balance'] -= money2


        info = '用户: [%s] 提现[%s￥]！手续费: [%s]' % (name, money, money3)

        # 记录提现流水
        user_dic['flow'].append(info)  # []

        db_handler.save(user_dic)

        logger.info(info)

        return True, info

    else:
        return False, '尊敬的用户，您的余额不足，请充值!'


# 转账接口
def transfer_interface(from_name, to_name, money):
    # 1、查询目标用户是否存在
    to_user_dic = db_handler.select(to_name)
    if not to_user_dic:
        return False, '目标用户不存在!'

    # 2、查询转账用户余额是否足够
    # 3、开始转账
    from_user_dic = db_handler.select(from_name)
    if from_user_dic['balance'] >= money:

        from_user_dic['balance'] -= money
        to_user_dic['balance'] += money

        # 更新用户信息
        db_handler.save(from_user_dic)
        db_handler.save(to_user_dic)

        return True, '用户[%s] 转账给 用户[%s] %s $!' % (from_name, to_name, money)
    else:
        return False, '尊敬的穷逼，您的余额不足，请充值!'


# 还款接口
def repay_interface(name, money):
    user_dic = db_handler.select(name)

    user_dic['balance'] += money

    db_handler.save(user_dic)

    return '还[%s]$款成功!' % money


# 查看流水接口
def check_flow_interface(name):
    user_dic = db_handler.select(name)
    # 把用户流水返回给用户层
    return user_dic['flow']


# bank，查看用户余额
def check_balance_interface(name):
    user_dic = db_handler.select(name)
    return user_dic['balance']

# 支付接口
def pay_interface(name, cost):

    user_dic = db_handler.select(name)

    if user_dic['balance'] >= cost:

        user_dic['balance'] -= cost

        user_dic['shopping_cart'] = {}

        db_handler.save(user_dic)

        return True, '支付成功!'

    else:
        return False, '消费失败!'


