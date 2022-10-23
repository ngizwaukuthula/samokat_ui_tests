import allure
from pages.main import MainPage

@allure.step('Проверяем соответствие текстов вопроса и ответа')
def check_question_answer_pair(driver, number, question, answer):

    page = MainPage(driver)
    page.get()
    page.click_on_question_with_text(number, question)

    return page.check_answer_with_this_text_is_displayed(answer)

@allure.title("Проверка вопрос-ответа про стоимость")
def test_price_question(driver):

    assert check_question_answer_pair(driver, 0, 'Сколько это стоит? И как оплатить?', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')

    driver.close()

@allure.title("Проверка вопрос-ответа про несколько самокатов")
def test_multiple_scooters_question(driver):

    assert check_question_answer_pair(driver, 1, 'Хочу сразу несколько самокатов! Так можно?', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')

    driver.close()

@allure.title("Проверка вопрос-ответа про расчет времени аренды")
def test_rent_time_calculation_question(driver):

    assert check_question_answer_pair(driver, 2, 'Как рассчитывается время аренды?', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')

    driver.close()

@allure.title("Проверка вопрос-ответа про доставку в тот же день")
def test_day_to_day_order_question(driver):

    assert check_question_answer_pair(driver, 3, 'Можно ли заказать самокат прямо на сегодня?', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')

    driver.close()

@allure.title("Проверка вопрос-ответа про изменение длительности аренды")
def test_changing_order_time_question(driver):

    assert check_question_answer_pair(driver, 4, 'Можно ли продлить заказ или вернуть самокат раньше?', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')

    driver.close()

@allure.title("Проверка вопрос-ответа про зарядку")
def test_charger_question(driver):

    assert check_question_answer_pair(driver, 5, 'Вы привозите зарядку вместе с самокатом?', 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')

    driver.close()

@allure.title("Проверка вопрос-ответа про отмену заказа")
def test_cancel_order_question(driver):

    assert check_question_answer_pair(driver, 6, 'Можно ли отменить заказ?', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')

    driver.close()

@allure.title("Проверка вопрос-ответа про зону за МКАДом")
def test_beyond_mkad_question(driver):

    assert check_question_answer_pair(driver, 7, 'Я жизу за МКАДом, привезёте?', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')

    driver.close()