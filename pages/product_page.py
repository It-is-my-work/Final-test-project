from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        adding_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        adding_button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def should_be_correct_name(self):
        product_name = self.get_product_name()
        adding_message = self.browser.find_element(*ProductPageLocators.ADDING_MESSAGE_NAME).text
        assert product_name == adding_message, f"{product_name} not in adding message"

    def should_be_correct_price(self):
        product_price = self.get_product_price()
        adding_message = self.browser.find_element(*ProductPageLocators.ADDING_MESSAGE_PRICE).text
        assert product_price == adding_message, f"{product_price} not in adding message"

    def should_element_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDING_MESSAGE_NAME), "Element is presented, but should be disappeard"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDING_MESSAGE_NAME), "Success message is presented, but should not be"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

