from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from utils import *
from pages.common import CommonControls

class OrderPage:

    # Адрес страницы
    url = "https://qa-scooter.praktikum-services.ru/order"

    # Поле ввода имени клиента в заказе
    name_input = [By.XPATH, ".//input[starts-with(@class, 'Input_Input__1iN_Z') and @placeholder = '* Имя']"]

    # Поле ввода фамлии клиента в заказе
    last_name_input = [By.XPATH, ".//input[starts-with(@class, 'Input_Input__1iN_Z') and @placeholder = '* Фамилия']"]

    # Поле ввода адреса клиента
    address_input = [By.XPATH, ".//input[starts-with(@class, 'Input_Input__1iN_Z') and @placeholder = '* Адрес: куда привезти заказ']"]

    # Поле ввода телефонного номера клиента
    phone_number_input = [By.XPATH,
                     ".//input[starts-with(@class, 'Input_Input__1iN_Z') and @placeholder = '* Телефон: на него позвонит курьер']"]

    # Поле ввода станции метро
    metro_station_name_input = [By.XPATH, ".//input[starts-with(@class, 'select-search__input') and @placeholder = '* Станция метро']"]

    # Кнопка "Далее" под формой заказа
    continue_button = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Далее']"]

    # Выпадающий список со станциями метро
    metro_stations_list = [By.XPATH, ".//div[@class = 'select-search__select']/*"]

    # Поле ввода даты доставки заказа
    delivery_date_input = [By.XPATH, ".//input[starts-with(@class, 'Input_Input__1iN_Z') and @placeholder = '* Когда привезти самокат']"]

    # Поле ввода срока аренды
    rental_period_dropped_down = [By.XPATH, ".//div[@class = 'Dropdown-placeholder' and text() = '* Срок аренды']"]

    # Выбранный день на календаре
    day_selected_on_date_picker = [By.XPATH, ".//div[contains(@class, 'day--selected')]"]

    # Опции периода аренды
    rental_period_options = [By.XPATH, ".//div[@class = 'Dropdown-option']"]

    # Чекбокс выбора серого цвета самоката
    scooter_grey_color_checkbox = [By.XPATH, ".//input[@id = 'grey']"]

    # Чекбокс выбора черного цвета самоката
    scooter_black_color_checkbox = [By.XPATH, ".//input[@id = 'black']"]

    # Поле ввода комментария курьеру
    comment_input = [By.XPATH, ".//input[starts-with(@class, 'Input_Input__1iN_Z') and @placeholder = 'Комментарий для курьера']"]

    # Кнопка "Заказать"
    order_button = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Заказать']"]

    # Кнопка "Заказать"
    yes_button = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Да']"]

    # Заголовок окна подтверждения заказа
    order_confirmation_title = [By.XPATH, ".//div[@class = 'Order_ModalHeader__3FDaJ' and text() = 'Заказ оформлен']"]


    def __init__(self, driver):

        self.driver = driver

    # Перейти на страницу заказа и дождаться, пока она загрузится
    def get(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(self.url))

    @allure.step('Проверяем, что отображается элемент: {locator}')
    def check_element_is_displayed(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)

        return element.is_displayed()

    @allure.step('Заполняем форму заказа')
    def fill_in_order_form(self, client_info):
        fill_in_field(self.driver, self.name_input, client_info['name'])
        fill_in_field(self.driver, self.last_name_input, client_info['last_name'])
        fill_in_field(self.driver, self.phone_number_input, client_info['phone_number'])
        fill_in_field(self.driver, self.address_input, client_info['address'])

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.metro_station_name_input))
        metro_input = self.driver.find_element(*self.metro_station_name_input)
        metro_input.click()
        metro_stations = self.driver.find_elements(*self.metro_stations_list)
        random.choice(metro_stations).click()

        click_on_element(self.driver, self.continue_button)
        fill_in_field(self.driver, self.delivery_date_input, client_info['delivery_date'])

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.day_selected_on_date_picker))
        day_selected = self.driver.find_element(*self.day_selected_on_date_picker)
        day_selected.click()


        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.rental_period_dropped_down))
        rental_period_dropped_down = self.driver.find_element(*self.rental_period_dropped_down)
        rental_period_dropped_down.click()
        rental_period_options = self.driver.find_elements(*self.rental_period_options)
        random_rental_period_option = random.choice(rental_period_options)
        random_rental_period_option.click()

        scooter_color_checkbox = random.choice([self.scooter_black_color_checkbox, self.scooter_grey_color_checkbox])
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(scooter_color_checkbox))
        scooter_color_checkbox_element = self.driver.find_element(*scooter_color_checkbox)
        scooter_color_checkbox_element.click()

        fill_in_field(self.driver, self.comment_input, client_info['comment'])
        click_on_element(self.driver, self.order_button)
        click_on_element(self.driver, self.yes_button)