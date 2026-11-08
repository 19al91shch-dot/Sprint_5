from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from generator import generate_login
import locators


class TestRegistration:
    def test_registration_success(self, driver):
        test_pswd = 'a1Bcde' # корректный пароль длиной 6 символов
        test_user_name = 'Alyona'
        test_email = generate_login()
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(By.XPATH, locators.registration_account_name_field).send_keys(test_user_name)
        driver.find_element(By.XPATH, locators.registration_mail_field).send_keys(test_email)
        driver.find_element(By.XPATH, locators.registration_password_field).send_keys(test_pswd)
        driver.find_element(By.XPATH, locators.registration_button).click()
        WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.education-services.ru/login'))
        assert driver.current_url == 'https://stellarburgers.education-services.ru/login'

    def test_registration_error(self, driver):
        test_pswd = 'a1Bcd' # некорректный пароль длиной меньше 6 символов
        test_user_name = 'Alyona'
        test_email = generate_login()
        driver.get("https://stellarburgers.education-services.ru/register")
        driver.find_element(By.XPATH, locators.registration_account_name_field).send_keys(test_user_name)
        driver.find_element(By.XPATH, locators.registration_mail_field).send_keys(test_email)
        driver.find_element(By.XPATH, locators.registration_password_field).send_keys(test_pswd)
        driver.find_element(By.XPATH, locators.registration_button).click()
        error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.password_validation_error)))
        assert error.text == "Некорректный пароль"
