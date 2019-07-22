'''
数据处理层
'''
from conf import settings
import json
import os


# 存数据
def save(user_dic):
    # BASE_PATH = os.path.dirname(os.path.dirname(__file__))
    # DB_PATH = settings.DB_PATH

    # db_path/username.json
    with open('%s/%s.json' % (settings.DB_PATH, user_dic['name']), 'w', encoding='utf-8') as f:
        res = json.dumps(user_dic)
        f.write(res)
        f.flush()


# 查取数据
def select(name):

    user_path = '%s/%s.json' % (settings.DB_PATH, name)

    if not os.path.exists(user_path):
        return

    with open(user_path, 'r', encoding='utf-8') as f:
        # res = f.read()
        # user_dic = json.loads(res)

        user_dic = json.load(f)
        return user_dic


