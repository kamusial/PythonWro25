from kod import LoginPage
from time import sleep
from selenium import webdriver
import pytest
import sys

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('standard_user', 'XX', 'https://www.saucedemo.com/'),
    ('locked_out_user', 'XX', 'https://www.saucedemo.com/'),
    ('problem_user', 'XX', 'https://www.saucedemo.com/'),
    ('performance_glitch_user', 'XX', 'https://www.saucedemo.com/')
]

@pytest.mark.skip()
@pytest.mark.parametrize('username, password, url', test_data)
def test_login_page(username, password, url):
    driver = webdriver.Firefox()
    page = LoginPage(driver)
    page.open()
    page.print_page_info()
    page.enter_username(username)
    page.enter_password(password)
    page.click_login()
    sleep(1)
    try:
        assert page.get_current_url() == url
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

@pytest.mark.skipif(len('piesek')==6, reason='Not implemented')
def test2():
    assert 2 == 2

@pytest.mark.xfail(reason='nie nasz dział')
def test3():
    assert 3 == 3


if sys.platform.startswith("win"):
    @pytest.mark.skip("skipping linux-only tests")
    def test_default():
        assert 3 == 4