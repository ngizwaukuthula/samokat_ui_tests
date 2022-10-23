import allure
from selenium.webdriver.common.by import By
from utils import click_on_element

class CommonControls:

    # Логотип "Яндекс" вверху сайта
    yandex_logo = [By.XPATH, ".//img[@alt = 'Yandex']"]

    # Логотип "Самоката" вверху сайта
    samokat_logo = [By.XPATH, ".//img[@alt = 'Scooter']"]

    # Кнопка согласия использования кук
    accept_cookies_button = [By.XPATH, ".//button[@class = 'App_CookieButton__3cvqF']"]

    def __init__(self, driver):

        self.driver = driver

    @allure.step('Соглашаемся на использование куки')
    def accept_cookies(self):
        click_on_element(self.driver, self.accept_cookies_button)