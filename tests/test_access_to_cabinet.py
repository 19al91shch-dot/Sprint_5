from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import locators


class TestAccessToCabinet:
    def test_access_to_cabinet(self, driver):
        # авторизация
        driver.get("https://stellarburgers.education-services.ru/login")
        driver.find_element(By.XPATH, locators.sign_in_email_field).send_keys('sherbitskaya_alenka_54.123@yandex.kz')
        driver.find_element(By.XPATH, locators.password_field).send_keys('a1Bcde')
        driver.find_element(By.XPATH, locators.sign_in_button).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.create_order_button)))
        # проверяем переход в личный кабинет
        driver.find_element(By.XPATH, locators.personal_cabinet_button).click()
        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.education-services.ru/account/profile'))
        assert driver.current_url == 'https://stellarburgers.education-services.ru/account/profile'