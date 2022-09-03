# -*- coding:UTF-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Base(object):
    # 新建对象就自动创建浏览器并且最大化窗口
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # 打开网页功能
    def open(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    # 关闭网页功能
    def close(self):
        time.sleep(3)
        self.driver.close()

    # 定位元素功能
    def locateElement(self, type, value):
        if type == "id":
            el=self.driver.find_element(By.ID,value)
        elif type == "name":
            el = self.driver.find_element(By.NAME,value)
        elif type == "class_name":
            el = self.driver.find_element(By.CLASS_NAME,value)
        elif type == "tag_name":
            el = self.driver.find_element(By.TAG_NAME,value)
        elif type == "link_text":
            el = self.driver.find_element(By.LINK_TEXT,value)
        elif type == "partial_link_text":
            el = self.driver.find_element(By.PARTIAL_LINK_TEXT,value)
        elif type == "xpath":
            el = self.driver.find_element(By.XPATH,value)
        elif type == "css_selector":
            el = self.driver.find_element(By.CSS_SELECTOR,value)

        return el

    # 点击元素功能
    def click(self, type, value):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 调用click()进行点击操作
        el.click()

    # 对定位到元素进行输入
    def input_data(self, type, value, data):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 调用send_keys进行输入
        el.send_keys(data)

    # 获取定位到的元素中的文本内容<a>text</a>
    def getText(self, type, value):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 返回文本内容
        return el.text

    # 获取定位到的元素中的标签值
    def getAttribute(self, type, value, name):
        # 调用locateElement定位元素
        el = self.locateElement(type, value)
        # 返回文本内容
        return el.get_attribute(name)

    # 删除对象时自动执行的方法
    def __del__(self):
        self.driver.close()
    def quit(self):
        '''
        退出浏览器
        :return:
        '''
        self.driver.quit()


# 如果是引用该类则不执行该方法
if __name__ == "__main__":
    test = Base()
    url = "https://www.baidu.com"
    test.open(url)
    test.input_data("id", "kw", "hiro")
    test.click("id", "su")
    time.sleep(5)