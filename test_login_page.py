from .pages.login_page import LoginPage

def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page_login = LoginPage(browser, link)
    page_login.open()
    page_login.should_be_login_page()
