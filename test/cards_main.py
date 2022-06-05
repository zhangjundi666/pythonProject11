import cards_tools
from bs4 import BeautifulSoup
import xlwt
import urllib
import sqlite3
import re

while True:
    # TODO(小张同学) 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作：")

    print("您选择的操作是【%s】" % action_str)

    if action_str in ["1","2","3"]:

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()
    elif action_str == "0":

        print("欢迎您再次使用【名片管理系统】！")
        break
        # pass 表示占位符，程序运行不会受到任何影响，保证代码结构正确！
        # pass
    else:
        print("您输入的不正确，请重新选择！")
