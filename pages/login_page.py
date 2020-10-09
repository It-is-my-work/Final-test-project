from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_email = self.find_element(*LoginPageLocators.EMAIL_AREA)
        input_email.send_keys(email)
        input_password_1 = self.find_element(*LoginPageLocators.PASSWORD_AREA_1)
        input_password_1.send_keys(password)
        input_password_2 = self.find_element(*LoginPageLocators.PASSWORD_AREA_2)
        input_password_2.send_keys(password)
        registration_button = self.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        part_url = "login"
        assert part_url in login_url, f"{part_url} not in login_url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

