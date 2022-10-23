from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import random
import string

def random_string(length, language = 'ru'):
    """Генерит рандомную строку заданной длины"""
    if language in ('ru', 'RU'):
        letters = ['А','а','Б','б','В','в','Г','г','Д','д','Е','е','Ё','ё','Ж','ж','З','з','И','и','Й','й','К','к','Л','л','М','м','Н','н','О','о','П','п','Р','р','С','с','Т','т','У','у','Ф','ф','Х','х','Ц','ц','Ч','ч','Ш','ш','Щ','щ','Ъ','ъ','Ы','ы','Ь','ь','Э','э','Ю','ю','Я','я']
    else:
        letters = string.ascii_letters

    return ''.join(random.choice(letters) for i in range(length))

def random_client_info():
    """Генерит словарь с рандомными данными для заполнения полей заказа"""


    info = {
        'name': random_string(10),
        'last_name': random_string(10),
        'address': "{}, {} {}".format(random_string(10),random_string(10),random_string(10)),
        'phone_number': "+{}".format(random.randrange(10000000000, 99999999999)),
        'delivery_date': "{}.{}.{}".format(random.randrange(1,31),random.randrange(1,12), random.randrange(2022,2122)),
        'comment': "{}, {} {}".format(random_string(10), random_string(10), random_string(10))
    }

    return info

@allure.step('Кликаем на элемент {locator}')
def click_on_element(driver, locator):
    """Кликнуть на кнопку с данным локатором"""

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(locator))
    button = driver.find_element(*locator)
    button.click()

@allure.step('Заполняем текстовое поле {locator}')
def fill_in_field(driver, locator, text):
    """Заполнить поле с данным локатором данным текстом"""

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((locator)))
    name_input = driver.find_element(*locator)
    name_input.click()
    name_input.send_keys(text)

@allure.step('Переходим в новое открытое окно')
def switch_to_new_opened_window(driver):
    """Переключает WebDriver на новое открытое окно или вкладку"""

    WebDriverWait(driver, 3).until(expected_conditions.new_window_is_opened)
    current_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != current_window:
            driver.switch_to.window(window_handle)
            break