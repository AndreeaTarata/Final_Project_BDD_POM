from selenium.webdriver.common.by import By


class HomePageLocators:
    HOME_BTN = (By.CSS_SELECTOR, '#logo')
    FORM = (By.CSS_SELECTOR, "a[class='nav-link']")
    AUTOCOMPLETE = (By.CSS_SELECTOR, 'body > div > div > li:nth-child(5) > a')
    CHECKBOX = (By.CSS_SELECTOR, 'body > div > div > li:nth-child(7) > a')
