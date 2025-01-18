from selenium import webdriver
import time

print('hello')
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(2)
button_accept = driver.find_element('id', 'L2AGLb')
button_accept.click()

# driver.find_element('id', 'L2AGLb').click()

time.sleep(2)

driver.quit()