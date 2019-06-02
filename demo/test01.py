# 需求：对《注册A.html》进行信息注册
# 账号：admin,密码：123456，电话：18600000000，电子邮件：123@qq.com 要求：
# 1. 定位方式统一使用CSS定位
# 2. 暂停2秒钟点击注册用户A按钮
# 3. 暂停3秒钟后关闭浏览器
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('file:///C:/Users/lf/Desktop/source_26/%E6%B3%A8%E5%86%8CA.html')

driver.find_element_by_css_selector('#userA').send_keys('admin')
driver.find_element_by_css_selector('#passwordA').send_keys('123456')
driver.find_element_by_css_selector('#telA').send_keys('18600000000')
driver.find_element_by_css_selector('#emailA').send_keys('123@qq.com')

sleep(2)
driver.find_element_by_css_selector('#zc>fieldset>button').click()

sleep(3)
driver.quit()
