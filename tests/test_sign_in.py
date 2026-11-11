from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


import locators


class TestSignIn:     
    #Проверка входа при нажатии на кнопку Войти 
    def test_sign_in_through_into_account_button(self, driver): 
        driver.get("https://stellarburgers.education-services.ru")
        driver.find_element(By.XPATH, locators.sign_in_into_account_button).click()
        email = 'sherbitskaya_alenka_54.123@yandex.kz'
        password = 'a1Bcde'
        driver.get("https://stellarburgers.education-services.ru/login")
        # Заполнение полей
        driver.find_element(By.XPATH, locators.sign_in_email_field).send_keys(email)
        driver.find_element(By.XPATH, locators.password_field).send_keys(password)
        # Ждем, пока кнопка «Войти» станет кликабельной, и кликаем
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, locators.sign_in_button))
        ).click()
        # Ждем появления кнопки «Оформить заказ»
        element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, locators.create_order_button))
        )
        # Проверяем наличие текста в кнопке
        assert element.text == 'Оформить заказ'

    #Проверка  входа при нажатии на кнопку Личный кабинет 
    def test_sign_in_through_personal_cabinet(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        driver.find_element(By.XPATH, locators.personal_cabinet_button).click()
        email = 'sherbitskaya_alenka_54.123@yandex.kz'
        password = 'a1Bcde'
        driver.get("https://stellarburgers.education-services.ru/login")
        # Заполнение полей
        driver.find_element(By.XPATH, locators.sign_in_email_field).send_keys(email)
        driver.find_element(By.XPATH, locators.password_field).send_keys(password)
        # Ждем, пока кнопка «Войти» станет кликабельной, и кликаем
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, locators.sign_in_button))
        ).click()
        # Ждем появления кнопки «Оформить заказ»
        element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, locators.create_order_button))
        )
        # Проверяем наличие текста в кнопке
        assert element.text == 'Оформить заказ'

    #Проверка входа при нажатии на ссылку Войти на странице Регистрации
    def test_sign_in_through_link_in_register_form(self, driver):        
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(By.XPATH, locators.sign_in_registration_form).click()
        email = 'sherbitskaya_alenka_54.123@yandex.kz'
        password = 'a1Bcde'
        driver.get("https://stellarburgers.education-services.ru/login")
        # Заполнение полей
        driver.find_element(By.XPATH, locators.sign_in_email_field).send_keys(email)
        driver.find_element(By.XPATH, locators.password_field).send_keys(password)
        # Ждем, пока кнопка «Войти» станет кликабельной, и кликаем
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, locators.sign_in_button))
        ).click()
        # Ждем появления кнопки «Оформить заказ»
        element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, locators.create_order_button))
        )
        # Проверяем наличие текста в кнопке
        assert element.text == 'Оформить заказ'

    #Проверка перехода на страницу входа при нажатии на ссылку Войти на странице Восстановления пароля
    def test_sign_in_through_link_in_pswd_recovery(self, driver):
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        driver.find_element(By.XPATH, locators.sign_in_forgot_password).click()
        email = 'sherbitskaya_alenka_54.123@yandex.kz'
        password = 'a1Bcde'
        driver.get("https://stellarburgers.education-services.ru/login")
        # Заполнение полей
        driver.find_element(By.XPATH, locators.sign_in_email_field).send_keys(email)
        driver.find_element(By.XPATH, locators.password_field).send_keys(password)
        # Ждем, пока кнопка «Войти» станет кликабельной, и кликаем
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, locators.sign_in_button))
        ).click()
        # Ждем появления кнопки «Оформить заказ»
        element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, locators.create_order_button))
        )
        # Проверяем наличие текста в кнопке
        assert element.text == 'Оформить заказ'