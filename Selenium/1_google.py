from selenium import webdriver
from selenium.webdriver import Keys
import time

print('hello')
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(2)
# button_accept = driver.find_element('id', 'L2AGLb')
# button_accept.click()
driver.find_element('id', 'L2AGLb').click()
time.sleep(2)
search_field = driver.find_element('name', 'q')
search_field.send_keys('Czy AI zwojuje światmnbv?')
time.sleep(5)
search_field.send_keys(Keys.ENTER)
# search_button = driver.find_element('name', 'btnK')
# search_button.click()
time.sleep(1)
driver.quit()