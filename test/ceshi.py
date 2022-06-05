# sen_01 = input()
# list_01 = sen_01.split(" ")
# list_01.reverse()
# sen_02 = " ".join(list_01)
# print(sen_02)


from selenium import webdriver
import time
import unittest
import os

class TestUnit1(unittest.TestCase):
    # 获取浏览器的驱动
    def setUp(self):
        # 1、self 就是类的引用/实例
        # 2、全局变量的定义：self.变量名
        from selenium import webdriver

        # 指定 Chrome 的绝对路径
        # （如果Chrome不是默认安装，要么设置在环境变量中，要么就在这里指定你Chrome的绝对路径）
        # 如果是默认安装位置，或者设置环境变量中，这里可以不指定


        # -*- coding = utf-8 -*-
        # @Time : 2021/10/16 17:47
        # @Author : LIUYU
        # @File : test_selenium.py
        # @Software : PyCharm

        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service

        s = Service(r"/Users/fuyu/Desktop/logs/chromedriver")
        driver = webdriver.Chrome(service=s)
        driver.get('https://www.baidu.com')

        time.sleep(3)

        # 在百度中搜索信息
        # 测试用例的命名： test_

    def test_search1(self):
        self.driver.find_element_by_id("kw").send_keys("顾一野")
        self.driver.find_element_by_id("su").click()
        time.sleep(6)
    # 在百度中搜索英文
    def test_search2(self):
        self.driver.find_element_by_id("kw").send_keys("Lisa")
        self.driver.find_element_by_id("su").click()
        time.sleep(6)
        # 异常捕捉 再传参数时，没有传 self，实例也可以不用传。 在TestCase类下，只有test_ 才执行，其他的只有被调用才执行。
        try:
            self.assertEqual("肖战_百度搜索", self.driver.title, msg="和预期结果不一致")
        except:
            self.save_errorImage(self.driver, "error.png")

    def save_errorImage(self, driver,fileName):
        # "./" 表示当前路径
        if not os.path.exists("./image"):
            os.makedirs("./image")
        # 错误截图的名称要不一样
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file("./image/" + now + fileName)

    # 关闭浏览器
    def tearDowm(self):
        self.driver.quit()

    # 一个入口
    if __name__ == "__main__":
        unittest.main()

