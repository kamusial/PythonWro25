from kod import LoginPage
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()

page = LoginPage(driver)
page.open()
sleep(2)
page.print_page_info()
page.enter_username('Kamil')
page.enter_password('Merito')
sleep(2)
page.click_login()
sleep(2)
page.close()
