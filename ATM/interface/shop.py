from db import db_handler
from lib import common

logger = common.get_logger('shop')

# 添加购物车接口
def add_shopping_cart_interface(name, shopping_cart):
    user_dic = db_handler.select(name)

    user_dic['shopping_cart'] = shopping_cart

    db_handler.save(user_dic)
    logger.info('添加商品成功!')
    return True, '添加商品成功!'

# 查看购物车接口
def show_shopping_cart_interface(name):

    user_dic = db_handler.select(name)

    return user_dic['shopping_cart']