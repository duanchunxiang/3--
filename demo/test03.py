# 需求：对TPshop/iweb_shop项目进行前台登录设计脚本
# 要求：
# 1. 使用unittest框架
# 2. 使用Fixture(setup、tearDown)
# 3. 浏览器最大化、隐式等待30秒
# 4. 使用断言判断登录用户是否为admin，不是则截屏保存图片
# 5. 图片命名格式为脚本执行时间
import unittest
import time

from selenium import webdriver


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://localhost')
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):

        self.driver.find_element_by_partial_link_text('登录').click()
        self.driver.find_element_by_css_selector('#username').send_keys('13800001111')
        self.driver.find_element_by_css_selector('#password').send_keys('123456')
        self.driver.find_element_by_css_selector('#verify_code').send_keys('8888')

        try:
            a = self.driver.find_element_by_css_selector('#username').get_attribute('value')
            self.assertEqual('admin', a)
        except:
            self.driver.get_screenshot_as_file('../image/{}.png'.format(time.strftime("%Y_%m_%d %H_%M_%S")))
        finally:
            self.driver.find_element_by_css_selector('.J-login-submit').click()
