from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from time import sleep
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def make_screenshot(okno):
    teraz = datetime.datetime.now()
    filename = teraz.strftime('screeny\\screenshot_%H_%M_%S.png')
    okno.get_full_page_screenshot_as_file(filename)

def wait_for_it(element_id):
    timeout = 5
    timeout_message = f'Element {element_id} nie pojawił się w czasie {timeout}'
    lokalizator = (By.ID, element_id)
    znaleziono = EC.visibility_of_element_located(lokalizator)
    oczekiwator = WebDriverWait(driver, timeout)
    return oczekiwator.until(znaleziono, timeout_message)
#    return WebDriverWait(driver, 5).until(EC.visibility_of_element_located(By.ID, element_id), timeout_message)


driver = webdriver.Firefox()
driver.get('https://www.saucedemo.com/')
print(f'Nazwa strony: {driver.title}')
print(f'Adres strony: {driver.current_url}')

try:
    username_field = driver.find_element('id', 'user-name')
    password_field = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.XPATH,
                                       '/html/body/div/div/div[2]/div[1]/div/div/form/input')
except NoSuchElementException:
    print('Nie znaleziono pola')
    make_screenshot(driver)
    driver.quit()
    raise

sleep(5)
username_field.clear()
username_field.send_keys('standard_user')
password_field.clear()
password_field.send_keys('secret_sauce')

# print(f'atrybut disabled {login_button.get_attribute("disabled")}')
if not login_button.get_attribute("disabled"):
    login_button.click()
else:
    print('Nie da się kliknąć, przycisk wyłączony')

sleep(2)
make_screenshot(driver)
driver.quit()