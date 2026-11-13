from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators


class TestConstructor:
    def test_access_to_sauces_section(self, driver):
        # авторизация
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(By.XPATH, locators.sign_in_email_field).send_keys('sherbitskaya_alenka_54.123@yandex.kz')
        driver.find_element(By.XPATH, locators.password_field).send_keys('a1Bcde')
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        # Проверка перехода к разделу Соусы конструктора бургеров
        # ждем кликабельности раздела Соусы и кликаем на него
        section = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, locators.sauces_section)))
        section.click()
        # ждем изменения активного раздела конструктора и сохраняем его в переменную
        active_section = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.active_section.format(section_name='Соусы'))))
        # проверка наличия слова Соусы в текстовом содержимом элемента active_section и вложенных в него элементов
        assert 'Соусы' in active_section.text

    def test_access_to_fillings_section(self, driver):
        # авторизация
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(By.XPATH, locators.sign_in_email_field).send_keys('sherbitskaya_alenka_54.123@yandex.kz')
        driver.find_element(By.XPATH, locators.password_field).send_keys('a1Bcde')
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        # проверяем переход к разделу Начинки (аналогично тестовому шагу для раздела Соусы)
        section = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, locators.fillings_section)))
        section.click()
        active_section = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.active_section.format(section_name='Начинки'))))
        assert 'Начинки' in active_section.text

    def test_access_to_buns_section(self, driver):
        # авторизация
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(By.XPATH, locators.sign_in_email_field).send_keys('sherbitskaya_alenka_54.123@yandex.kz')
        driver.find_element(By.XPATH, locators.password_field).send_keys('a1Bcde')
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        # предварительно переходим к другому разделу конструктора (т.к. раздел Булки выбран по умолчанию) и дожидаемся когда он будет активным
        section = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, locators.fillings_section)))
        section.click()
        active_section = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.active_section.format(section_name='Начинки'))))
        # переходим обратно к разделу Булки
        driver.find_element(By.XPATH, locators.buns_section).click()
        # ожидаем изменения активного раздела конструктора и сохраняем его в переменную
        active_section = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.active_section.format(section_name='Булки'))))
        # проверяем наличие слова Булки в текстовом содержимом элемента active_section и вложенных в него элементов
        assert 'Булки' in active_section.text