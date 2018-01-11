# coding=utf-8

import unittest
import HTMLTestReportCN
import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# desired_caps = {
#     'platformName': 'Android',
#     'plafromVersion': '8.0.0',  # 系统版本号，需要对应修改不然会报错
#     'deviceName': 'emulator-5554',  # 设备名
#     'appPackage': 'com.fudaojun.app.teacher',  # 包名 可通过uiautomatorviewer获取，也可以直接问开发
#     'appActivity': '.activity.loading.LoadingActivity',
#     'unicodeKeyboard': True,
#     'resetKeyboard': True
# }

CONNECT = {
    'platformName': 'Android',
    'platformVersion': '8.0',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.fudaojun.app.teacher',
    'appActivity': '.activity.loading.LoadingActivity',
    "baseUrl": "http://localhost:4723/wd/hub",
    'unicodeKeyboard': True,
    'resetKeyboard': True
}


# python 连接 appium
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


class Login(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': CONNECT['platformName'],
            'platformVersion': CONNECT['platformVersion'],
            'deviceName': CONNECT['deviceName'],
            'appPackage': CONNECT['appPackage'],
            'appActivity': CONNECT['appActivity'],
            'unicodeKeyboard': CONNECT['unicodeKeyboard'],
            'resetKeyboard': CONNECT['resetKeyboard']
        }
        self.driver = webdriver.Remote(CONNECT['baseUrl'], desired_caps)

    def tearDown(self):
        print("Login tearDown")

        self.driver.close_app()
        self.driver.quit()

    def test_login_case1(self):
        u"""已有账号正常登录"""

        # 跳过引导页
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/tv_skip_guide_activity")).click()

        # 清空原有的账号

        # 填写已有的账号
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_login_account")).send_keys(
            "13777748550")
        # 填写正确的密码
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_login_password")).send_keys(
            "666666")

        # 点击登录按钮
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/rlv_button_login")).click()


class Register(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': CONNECT['platformName'],
            'platformVersion': CONNECT['platformVersion'],
            'deviceName': CONNECT['deviceName'],
            'appPackage': CONNECT['appPackage'],
            'appActivity': CONNECT['appActivity'],
            'unicodeKeyboard': CONNECT['unicodeKeyboard'],
            'resetKeyboard': CONNECT['resetKeyboard']
        }
        self.driver = webdriver.Remote(CONNECT['baseUrl'], desired_caps)

    def tearDown(self):
        print("Register tearDown")

        self.driver.close_app()
        self.driver.quit()

    def testCase1(self):
        u"""正常注册"""
        # 跳过引导页
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/tv_skip_guide_activity")).click()

        # 点击登录按钮
        # WebDriverWait(driver, 10, 0.5).until(
        #    lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/rlv_button_login")).click()

        # 点击注册按钮
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/rt_register")).click()

        # 输入姓名
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_real_name")).send_keys("测试demo")

        # 选择学校
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_select_school")).click()
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/tv_school_name")).click()

        # 输入手机号码
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_phone_number")).send_keys(
            "13277748551")

        # 输入验证码
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_sms_vertify_code")).send_keys("123456")

        # 输入密码
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_password")).send_keys("123456")

        # 点击下一步
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/rlv_rigister_next")).click()

def hello():
    return "hello world"

class testNum(unittest.TestCase):
    def testHello(self):
        self.assertEqual("hello world",hello())

if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Login)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Register)
    alltest = unittest.TestSuite([suite1, suite2])

    # 确定生成报告的路径 这是放在桌面上了
    filePath = '/Users/lina/Desktop/TestReport.html'
    fp = open(filePath, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='自动化测试报告',
        description='这运行的都什么玩意儿',
        tester='今天怎么不开心'
    )
    # 运行测试用例
    runner.run(alltest)
    # 关闭文件，否则会无法生成文件
    # fp.close()

