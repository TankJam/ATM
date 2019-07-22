'''
    启动文件入口
'''

from core import src
import os
import sys

# 拿到项目的路径
path = os.path.dirname(__file__)

# 添加到环境变量中
sys.path.append(path)


if __name__ == '__main__':
    src.run()
