from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://perso.telecom-paristech.fr/eagan/class/igr204/datasets')
sleep(5)
element = browser.find_element_by_xpath('//*[@id="datasets"]/div[2]/div/article/ul[2]/li[1]/a').click()


actionChains = ActionChains(browser)
actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
