from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    def open(self):
        self.driver.get(self.URL)

    def get_logo(self):
        return self.driver.find_element(*HomePageLocators.HOME_BTN).is_displayed()

    def click_form(self):
        self.driver.find_element(*HomePageLocators.FORM).click()