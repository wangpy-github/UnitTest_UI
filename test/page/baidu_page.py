from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    """用户登陆页面"""

    def click_login_button(self):
        login_button = (By.XPATH, '//*[@id="u1"]/a[8]')  # 首页登陆按钮
        el = self.driver.find_element(*login_button)
        el.click()

    def click_UserName_Login_name(self):
        UserName_Login_name = (By.ID, 'TANGRAM__PSP_10__footerULoginBtn')  # 选择用户名登陆按钮
        el = self.driver.find_element(*UserName_Login_name)
        el.click()

    def click_UserName_Login_code(self):
        UserName_Login_code = (By.ID, 'TANGRAM__PSP_10__footerQrcodeBtn')  # 选择扫码登陆按钮
        el = self.driver.find_element(*UserName_Login_code)
        el.click()

    def input_UserName(self):
        UserName = (By.ID, 'TANGRAM__PSP_10__userName')  # 登录名
        el = self.driver.find_element(*UserName)
        el.send_keys("掩沙")

    def input_PassWord(self):
        PassWord = (By.ID, 'TANGRAM__PSP_10__password')  # 登录密码
        el = self.driver.find_element(*PassWord)
        print(el)
        el.send_keys("wpy620606")

    def click_LoginButton(self):
        LoginButton = (By.ID, 'TANGRAM__PSP_10__submit')  # 登录按钮
        el = self.driver.find_element(*LoginButton)
        el.click()

    def get_LoginName(self):
        LoginName = (By.XPATH, '//*[@id="ibx-uc"]/div/div[2]/a')  # 登录后的名字
        el = self.driver.find_element(*LoginName)
        return el
