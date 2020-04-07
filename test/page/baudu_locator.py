from selenium.webdriver.common.by import By


class LoginPageLocators():
    '''
    用户登录页面
    '''
    login_button = (By.XPATH, '//*[@id="u1"]/a[8]')  # 首页登陆按钮
    UserName_Login_name = (By.ID, 'TANGRAM__PSP_10__footerULoginBtn')  # 选择用户名登陆按钮
    UserName_Login_code = (By.ID, 'TANGRAM__PSP_10__footerQrcodeBtn')  # 选择扫码登陆按钮
    UserName = (By.ID, 'TANGRAM__PSP_10__userName')  # 登录名
    PassWord = (By.ID, 'TANGRAM__PSP_10__password')  # 登录密码
    LoginButton = (By.ID, 'TANGRAM__PSP_10__submit')  # 登录按钮
    LoginName = (By.XPATH, '//*[@id="ibx-uc"]/div/div[2]/a')  # 登录后的名字

