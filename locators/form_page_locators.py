from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, '#first-name')
    LAST_NAME = (By.ID, "last-name")
    JOB_TITLE = (By.ID, 'job-title')
    SUBMIT = (By.CSS_SELECTOR, "a[role='button']")