from selenium import webdriver
import unittest
import time
from test.page.baidu_page import *


class Test_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../../drivers/chromedriver.exe")
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()

    def test_login(self):
        loginpage = LoginPage(self.driver)
        time.sleep(3)
        loginpage.click_login_button()  # 点击首页登陆按钮
        time.sleep(1)
        loginpage.click_UserName_Login_name()  # 点击选择用户名登陆按钮
        loginpage.input_UserName()  # 输入登录名
        loginpage.input_PassWord()  # 输入登录密码
        loginpage.click_LoginButton()  # 点击登录按钮
        time.sleep(5)
        self.driver.get("http://i.baidu.com/")
        s = loginpage.get_LoginName()
        print(s.text)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
