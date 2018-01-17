# coding=utf-8

import unittest
import HTMLTestReportCN
import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import json

# 1. 写一个 json 文件
# 2. 使用 with open 来读 json 文件。
# 	with open('文件路径') as reader:
# 		data = reader.read()
# 3. 使用 json 库，将 json 数据转换成 python 的 dict。
# 4. 最后就可以在 脚本中使用 json 文件里面的数据。

with open('./demo.json', encoding='utf-8') as reader:
    data = reader.read()

demo = json.loads(data)

CONNECT = {
    'platformName': 'Android',                               # 环境名
    'platformVersion': '8.0',                                # 系统版本号，需要对应修改不然会报错
    'deviceName': 'emulator-5554',                           # 设备名
    'appPackage': 'com.fudaojun.app.teacher',                # 包名，可通过uiautomatorviewer获取，也可以直接问开发
    'appActivity': '.activity.loading.LoadingActivity',      # 可以通过uiautomatorviewer获取
    "baseUrl": "http://localhost:4723/wd/hub",
    'unicodeKeyboard': True,                                 # 为了能够正常输入文字引入的设置
    'resetKeyboard': True
}


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
        self.driver = webdriver.Remote(CONNECT['baseUrl'], desired_caps)           # 连接到 appium

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()

    # 单元测试方法命名需要以 test 开头
    def test_login_case1(self):
        u"""已有账号正常登录"""

        # 跳过引导页
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/tv_skip_guide_activity")).click()

        # 填写已有的账号
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_login_account")).send_keys(
            demo['phone'])

        # 填写正确的密码
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_login_password")).send_keys(
            demo['password'])

        # 点击登录按钮
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/rlv_button_login")).click()

        # 判断是否登录成功 应当用一个方法判断一下页面是否有登录成功之后会有某个元素
        # 这里偷懒用点击代替一下 点击了我的课程
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/rl_workbanch_lesson")).click()


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
        self.driver.close_app()
        self.driver.quit()

    def test_register_case1(self):
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
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_real_name")).send_keys(demo['name'])

        # 选择学校
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_select_school")).click()
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/tv_school_name")).click()

        # 输入手机号码
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_phone_number")).send_keys(
            demo['phone_register'])

        # 输入验证码
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_sms_vertify_code")).send_keys(demo['key'])

        # 输入密码
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/et_password")).send_keys(demo['password_register'])

        # 点击下一步
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_id("com.fudaojun.app.teacher:id/rlv_rigister_next")).click()

        # 应当是判断是否注册成功
        # 这里只是点击了立即申请
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda view: view.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                "android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/"
                "android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.TextView")).click()

        # 点击确认权限
        WebDriverWait(self.driver, 10, 0.5).until(lambda view: view.find_element_by_id(
            "com.android.packageinstaller:id/permission_allow_button")).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda view: view.find_element_by_id(
            "com.android.packageinstaller:id/permission_allow_button")).click()

        # 填写邮箱 邮箱-->填入-->点击确定
        WebDriverWait(self.driver, 10, 0.5).until(lambda view: view.find_element_by_id(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/"
            "android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/"
            "android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/"
            "android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView[2]")).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda view: view.find_element_by_id(
            "com.fudaojun.app.teacher:id/tv_complete_info")).send_keys('32132@qq.com')
        WebDriverWait(self.driver, 10, 0.5).until(lambda view: view.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/"
            "android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")).click()

        # 填写QQ号  邮箱-->填入-->点击确定
        WebDriverWait(self.driver, 10, 0.5).until(lambda view: view.find_element_by_id(
            "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/"
            "android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/"
            "android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/"
            "android.widget.RelativeLayout[3]/android.widget.RelativeLayout/android.widget.TextView[2]")).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda view: view.find_element_by_id(
            "com.fudaojun.app.teacher:id/tv_complete_info")).send_keys(demo['qq'])
        WebDriverWait(self.driver, 10, 0.5).until(lambda view: view.find_element_by_id(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/"
            "android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")).click()

        # 选择大学
        WebDriverWait(self.driver, 10, 0.5).until(lambda view: view.find_element_by_id(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/"
            "android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/"
            "android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/"
            "android.widget.RelativeLayout[5]/android.widget.RelativeLayout/android.widget.TextView[2]")).click()
        WebDriverWait(self.driver, 10, 0.5).until(lambda view: view.find_element_by_id(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
            "android.widget.RelativeLayout[2]/android.support.v7.widget.RecyclerView/"
            "android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.TextView")).click()

        # 选择入学年份



if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Login)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Register)
    all_test = unittest.TestSuite([suite1, suite2])

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
    runner.run(all_test)
    # 关闭文件，否则会无法生成文件
    fp.close()


