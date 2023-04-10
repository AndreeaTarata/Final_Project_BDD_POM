from selenium.webdriver.common.by import By

from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):

    def open(self):
        self.driver.get(self.URL)

    def get_first_name_filed(self):
        return self.driver.find_element(*FormPageLocators.FIRST_NAME).is_displayed()

    def enter_first_name(self, value):
        self.driver.find_element(*FormPageLocators.FIRST_NAME).send_keys(value)

    def enter_last_name(self, value):
        self.driver.find_element(*FormPageLocators.LAST_NAME).send_keys(value)

    def enter_job_title(self, value):
        self.driver.find_element(*FormPageLocators.JOB_TITLE).send_keys(value)

    def submit(self):
        self.driver.find_element(*FormPageLocators.SUBMIT).click()

    def get_form_submit_msg(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[role='alert']").text

# TODO in loc de By.CSS sa mutam si locatorul asta dar intr-o alta pagina care e gen succes page