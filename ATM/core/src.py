from interface import user, bank, shop
from lib import common

user_info = {
    'name': None
}

# 注册
# def register():
#     print('注册...')
#     while True:
#         name = input('请输入用户名: ').strip()
#         pwd = input('请输入密码: ').strip()
#         conf_pwd = input('请输入密码: ').strip()
#         if pwd == conf_pwd:
#             user_dic = {
#                 'name': name, 'pwd': pwd, 'flow': [], 'shopping_cart': {}
#             }
#             # BASE_PATH = os.path.dirname(os.path.dirname(__file__))
#             DB_PATH = settings.DB_PATH
#
#             # db_path/username.json
#             with open('%s/%s.json' % (DB_PATH, name), 'w', encoding='utf-8') as f:
#                 res = json.dumps(user_dic)
#                 f.write(res)
#                 f.flush()
#
#             print('注册成功!')
#             break


# 注册功能
def register():
    print('注册...')
    while True:
        name = input('请输入用户名: ').strip()
        pwd = input('请输入密码: ').strip()
        conf_pwd = input('请输入密码: ').strip()
        # 小的逻辑处理
        if pwd == conf_pwd:
            # res = user.register_interface(name, pwd)
            # flag = res[0]
            # msg = res[1]
            flag, msg = user.register_interface(name, pwd)

            # if True:
            #     print(注册成功)
            # eles:
            # print(用户已存在)
            if flag:
                print(msg)
                break

            else:
                print(msg)


# 登录
def login():
    # 如果已登录，结束login函数
    if user_info['name']:
        return

    while True:
        name = input('请输入用户名: ').strip()
        pwd = input('请输入密码: ').strip()
        flag, msg = user.login_interface(name, pwd)
        if flag:
            user_info['name'] = name
            print(msg)
            break

        else:
            print(msg)


# 查看余额
@common.auth
def check_balance():
    msg = user.check_balance_interface(user_info['name'])
    print(msg)


# 提现
@common.auth
def withdraw():
    while True:
        money = input('请输入提现金额: ').strip()
        if money.isdigit():
            money = int(money)
            flag, msg = bank.withdrwa_interface(user_info['name'], money)
            if flag:
                print(msg)
                break

            else:
                print(msg)
        else:
            print('请输入数字!')


# 转账
@common.auth
def transfer():
    while True:
        to_user = input('请输入转账目标用户: ').strip()
        money = input('请输入转账金额：').strip()
        money = int(money)
        flag, msg = bank.transfer_interface(user_info['name'], to_user, money)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 还款
@common.auth
def repay():
    while True:
        money = input('请输入还款金额: ').strip()
        money = int(money)

        msg = bank.repay_interface(user_info['name'], money)
        print(msg)
        break

# 查看流水
@common.auth
def check_flow():
    flow_s = bank.check_flow_interface(user_info['name'])
    # print(flow_s)
    for line in flow_s:
        print(line)


# 购物车功能
@common.auth
def shopping():
    '''
            购物车
            1 先循环打印出商品
            2 用户输入数字选择商品（判断是否是数字，判断输入的数字是否在范围内）
            3 取出商品名，商品价格
            4 判断用户余额是否大于商品价格
            5 余额大于商品价格时，判断此商品是否在购物车里
                5.1 在购物车里，个数加1
                5.1 不在购物车里，拼出字典放入（｛‘car’：｛‘price’：1000，‘count’：2｝,‘iphone’：｛‘price’：10，‘count’：1｝｝）
            6 用户余额减掉商品价格
            7 花费加上商品价格
            8 当输入 q时，购买商品
                8.1 消费为0 ，直接退出
                8.2 打印购物车
                8.3 接受用户输入，是否购买 当输入y，直接调购物接口实现购物
            9 商品列表
                goods_list = [
                    ['凤爪', 50],
                    ['T-shirt', 150],
                    ['macbook', 21800],
                    ['iphoneX', 7000]
                ]
            :return:
            '''
    goods_list = [
        ['凤爪', 50],
        ['T-shirt', 150],
        ['macbook', 21800],
        ['iphoneX', 7000]
    ]

    # 购物车
    shopping_cart = {}

    # 初始总额
    cost = 0

    # 获取用户余额
    user_balance = bank.check_balance_interface(user_info['name'])

    while True:
        for index, goods in enumerate(goods_list):
            print(index, goods)

        choice = input('请选择商品编号: ').strip()

        if choice.isdigit():
            choice = int(choice)

            if choice >= 0 and choice < len(goods_list):

                # 商品的名称和价格
                good_name, good_price = goods_list[choice]

                if user_balance >= good_price:

                    if good_name in shopping_cart:
                        shopping_cart[good_name] += 1

                    else:
                        shopping_cart[good_name] = 1

                    cost += good_price

                    flag, msg = shop.add_shopping_cart_interface(user_info['name'], shopping_cart)
                    if flag:
                        print(msg)
                        print(shopping_cart)
                else:
                    print('*穷*，请充值!')

        elif choice == 'q':
            if cost == 0: break

            confirm = input('确认购买输入 y/n 取消:').strip()

            # 输入y选择购买商品
            if confirm == 'y':
                flag, msg = bank.pay_interface(user_info['name'], cost)
                if flag:
                    print(msg)
                    break

                else:
                    print(msg)


            else:
                print('退出购买!')
                break
        else:
            print('输入有误!')


# 查看购物车
@common.auth
def check_shop():
    # 调用显示购物车接口
    shopping_cart = shop.show_shopping_cart_interface(user_info['name'])
    if shopping_cart:
        print(shopping_cart)

    else:
        print('购物车已被清空!')


# 注销用户
@common.auth
def logout():
    msg = user.logout_interface()
    print(msg)


func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': transfer,
    '6': repay,
    '7': check_flow,
    '8': shopping,
    '9': check_shop,
    '0': logout
}


# 主程序
def run():
    while True:
        print('''
        1、注册
        2、登录
        3、查看余额
        4、提现
        5、转账
        6、还款
        7、查看流水
        8、购物车
        9、查看购物车
        0、注销用户
        q、退出
        ''')

        choice = input('请选择功能编号: ').strip()

        quit = ['q', 'Q', 'quit']

        if choice in quit:
            break

        # 判断用户选择的编号是否在1-9的功能中
        if choice in func_dic:

            # 执行相应的功能
            func_dic[choice]()

        else:
            print('请输入正确的编号!')


