from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import allure

class MainPage:

    # Адрес страницы
    url = "https://qa-scooter.praktikum-services.ru/"

    # Элемент списка с вопросами в разделе "Вопросы о важном"
    question_item = [By.XPATH, ".//div[@id='accordion__heading-{}' and text() = '{}']"]

    # Элемент списка с ответами в разделе "Вопросы о важном"
    answer_item = [By.XPATH, ".//p[text() = '{}']"]

    # Верхняя кнопка заказа
    top_order_button = [By.XPATH, ".//button[@class = 'Button_Button__ra12g' and text() = 'Заказать']"]

    # Нижняя кнопка заказа
    bottom_order_button = [By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text() = 'Заказать']"]

    def __init__(self, driver):

        self.driver = driver


    def get(self):

        self.driver.get(self.url)
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(self.url))

    @allure.step('Проверяем, что отображается ответ: {text}')
    def check_answer_with_this_text_is_displayed(self, text):

        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located((self.answer_item[0], self.answer_item[1].format(text))))

        return self.driver.find_element(self.answer_item[0], self.answer_item[1].format(text)).is_displayed()

    @allure.step('Кликаем на вопрос: {text}')
    def click_on_question_with_text(self, number, text):

        WebDriverWait(self.driver, 3).until(
            expected_conditions.presence_of_element_located((self.question_item[0], self.question_item[1].format(number, text))))

        question_element = self.driver.find_element(self.question_item[0], self.question_item[1].format(number, text))
        self.driver.execute_script("arguments[0].scrollIntoView();", question_element)

        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable((self.question_item[0], self.question_item[1].format(number, text))))
        question_element.click()