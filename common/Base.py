# coding=utf-8
"""
webdriver下载
https://sites.google.com/a/chromium.org/chromedriver/downloads
http://npm.taobao.org/mirrors/chromedriver/
"""
import os
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

current_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current_path))  # 项目路径
drivers_path = BASE_DIR + os.sep + "drivers"
chromedriver_path = os.path.join(drivers_path, "chromedriver.exe")


class Base():
    def __init__(self, driver="Chrome", driverpath=chromedriver_path):
        # 根据传入的参数创建对应的浏览器对象，前提是所有的浏览器驱动都已经正确安装
        if driver == 'Firefox':
            self.driver = webdriver.Firefox(driverpath)
        elif driver == 'Chrome':
            self.driver = webdriver.Chrome(driverpath)
        elif driver == 'PhantomJS':
            self.driver = webdriver.PhantomJS(driverpath)
        # 设置浏览器全屏
        self.driver.maximize_window()

    """
    元素定位方法
    """

    def locate_element(self, lo_type_value):
        """"显性等待定位元素，定位单个元素"""
        element = None
        wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.1)
        try:
            element = wait.until(lambda x: x.find_element(*lo_type_value))  # 查看源码：x就是self.driver
        except Exception as e:
            print("单个元素定位失败", e)
        if element is not None:
            return element

    def locate_elements(self, *lo_type_value):
        """显性等待定位元素，定位一组元素"""
        elements = None
        wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=0.1)
        try:
            elements = wait.until(
                lambda x: x.find_elements(*lo_type_value))  # 查看源码：x就是self.driver
        except Exception as e:
            print("一组元素定位失败", e)
        if elements is not None:
            return elements

    def delay(self):
        """隐式等待"""
        self.driver.implicitly_wait(5)

    def __del__(self):
        time.sleep(3)
        self.driver.quit()

    def get_url(self, url):
        self.driver.get(url)
        self.delay()

    """
    常用元素操作方法
    """

    def click(self, lo_type_value):
        # 调用定位方法进行元素定位
        element = self.locate_element(*lo_type_value)
        # 执行点击操作
        element.click()
        time.sleep(1)

    def input_data(self, lo_type_value, data):
        # 调用定位方法进行元素定位
        element = self.locate_element(*lo_type_value)
        element.clear()
        element.send_keys(data)

    def get_text(self, lo_type_value):
        # 调用定位方法进行元素定位
        el = self.locate_element(*lo_type_value)
        return el.text

    def get_attr(self, lo_type_value, data):
        # 调用定位方法进行元素定位
        el = self.locate_element(*lo_type_value)
        return el.get_attribute(data)


if __name__ == '__main__':
    print(chromedriver_path)
