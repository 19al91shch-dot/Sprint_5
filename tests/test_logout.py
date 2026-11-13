from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators


class TestLogout:
    def test_logout(self, driver):
        # авторизация
        email = 'sherbitskaya_alenka_54.123@yandex.kz'
        password = 'a1Bcde'
        driver.get("https://stellarburgers.education-services.ru/login")
        # Заполнение полей
        driver.find_element(By.XPATH, locators.sign_in_email_field).send_keys(email)
        driver.find_element(By.XPATH, locators.password_field).send_keys(password)
        WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, locators.sign_in_button))
        ).click()
        # переход в личный кабинет
        driver.find_element(By.XPATH, locators.personal_cabinet_button).click()
        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.education-services.ru/account/profile'))
        # проверка выхода по кнопке Выйти
        driver.find_element(By.XPATH, locators.exit_button).click()
        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.education-services.ru/login'))
        assert driver.current_url == 'https://stellarburgers.education-services.ru/login'