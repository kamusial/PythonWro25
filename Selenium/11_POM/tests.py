from kod import LoginPage
from time import sleep
from selenium import webdriver

def test_login_page():
    driver = webdriver.Firefox()
    page = LoginPage(driver)
    page.open()
    sleep(2)
    page.print_page_info()
    page.enter_username('Kamil')
    page.enter_password('Merito')
    sleep(2)
    page.click_login()
    sleep(2)

    try:
        assert page.get_current_url() == page.after_login_url
    except AssertionError:
        print('Asercja NIE przeszła\nstrona sie NIE zgadza')
        print(f'jesteś na stronie {page.get_current_url()}')
        raise
    else:
        print('Asercja przeszła\nstrona sie zgadza')
        print(f'jesteś na stronie {page.get_current_url()}')
    finally:
        print('Zamykam strone')
        page.close()
