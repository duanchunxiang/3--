# 需求：对《注册实例.html》进行信息注册
# 账号：admin,密码：123456，电话：18600000000，电子邮件：123@qq.com
# 要求： 1. 对注册《主界面、注册A、注册B》三个注册信息进行注册信息填写
# 2. 定位方式不限
# 3. 暂停3秒钟关闭浏览器
from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('file:///C:/Users/lf/Desktop/source_26/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html')

driver.find_element_by_css_selector('#user').send_keys('admin')
driver.find_element_by_css_selector('#password').send_keys('123456')
driver.find_element_by_css_selector('#tel').send_keys('18600000000')
driver.find_element_by_css_selector('#email').send_keys('123@qq.com')
driver.find_element_by_css_selector('#zc>fieldset>button').click()

driver.switch_to.frame('myframe1')
driver.find_element_by_css_selector('#userA').send_keys('admin')
driver.find_element_by_css_selector('#passwordA').send_keys('123456')
driver.find_element_by_css_selector('#telA').send_keys('18600000000')
driver.find_element_by_css_selector('#emailA').send_keys('123@qq.com')
driver.find_element_by_css_selector('#zc>fieldset>button').click()

driver.switch_to.default_content()
driver.switch_to.frame('myframe2')
driver.find_element_by_css_selector('#userB').send_keys('admin')
driver.find_element_by_css_selector('#passwordB').send_keys('123456')
driver.find_element_by_css_selector('#telB').send_keys('18600000000')
driver.find_element_by_css_selector('#emailB').send_keys('123@qq.com')
driver.find_element_by_css_selector('#zc>fieldset>button').click()
sleep(3)
driver.quit()