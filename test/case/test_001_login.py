#coding=utf-8
import unittest
from test.page.baidu_page import *


class Test_Login(unittest.TestCase):

    def test_login(self):
        loginpage = LoginPage()
        loginpage.get_url("http://www.baidu.com")
        loginpage.click_login_button()  # 点击首页登陆按钮
        loginpage.click_UserName_Login_name()  # 点击选择用户名登陆按钮
        loginpage.input_UserName()  # 输入登录名
        loginpage.input_PassWord()  # 输入登录密码
        loginpage.click_LoginButton()  # 点击登录按钮
        loginpage.get_url("http://i.baidu.com")
        del loginpage


if __name__ == '__main__':
    unittest.main()
