from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://portal.nycu.edu.tw/#/login?redirect=%2F')
#browser.get('https://www.facebook.com')
browser.find_element_by_id('account').send_keys('yourid')
browser.find_element_by_id('password').send_keys('password')
browser.find_element_by_class_name('login').click()
