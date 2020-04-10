#coding=utf-8
from common.Base import Base
from test.page.baidu_locator import LoginPageLocators


class LoginPage(Base):
    """用户登陆页面"""

    def click_login_button(self):
        el = self.locate_element(LoginPageLocators().login_button)  # 点击首页登陆按钮
        el.click()

    def click_UserName_Login_name(self):
        el = self.locate_element(LoginPageLocators().UserName_Login_name)  # 点击选择用户名登陆按钮
        el.click()

    def click_UserName_Login_code(self):
        el = self.locate_element(LoginPageLocators().UserName_Login_code)  # 点击选择扫码登陆按钮
        el.click()

    def input_UserName(self):
        el = self.locate_element(LoginPageLocators().UserName)  # 输入登录名
        el.send_keys("xxxxxx")

    def input_PassWord(self):
        el = self.locate_element(LoginPageLocators().PassWord)  # 输入登录密码
        print(el)
        el.send_keys("xxxxxx")

    def click_LoginButton(self):
        el = self.locate_element(LoginPageLocators().LoginButton)  # 点击登录按钮
        el.click()

    def get_LoginName(self):
        el = self.locate_element(LoginPageLocators().LoginName)  # 获取登录后的名字
        return el.text
