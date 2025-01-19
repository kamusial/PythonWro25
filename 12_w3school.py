from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/")
sleep(1)

# menu = driver.find_element(By.ID, 'navbtn_tutorials')
# HTMLtutorial = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/nav[2]/div[1]/div/div[2]/div[1]/div[1]/a[2]')
# #webdriver.ActionChains(driver).move_to_element(menu).click().move_to_element(HTMLtutorial).click().perform()
# sleep(1)
# (webdriver.ActionChains(driver).move_to_element(menu).
#  click().move_to_element(HTMLtutorial).click().perform())
# sleep(3)

menu = driver.find_element('id', 'navbtn_tutorials')
HTMLtutorial = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div/nav[1]/div[1]/div/div[2]/div[1]/div[1]/a[2]')
webdriver.ActionChains(driver).move_to_element(menu).click().move_to_element(HTMLtutorial).click().perform()
sleep(3)
driver.quit()
