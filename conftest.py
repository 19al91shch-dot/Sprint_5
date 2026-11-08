import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators


# Создание экземпляра браузера Chrome и выход из него в конце каждого теста
@pytest.fixture
def driver():
    browser = webdriver.Chrome() 
    yield browser  
    browser.quit() 

# Фикстура для данных зарегистрированного пользователя
@pytest.fixture(scope="session")
def user_data():
    return {
        "name": "Alena",
        "email": "sherbitskaya_alenka_54.123@yandex.kz",
        "password": "a1Bcde"
    }    

@pytest.fixture(scope="function")
def register_user(driver, user_data):
    """Выполняет регистрацию на сайте и возвращает данные пользователя."""
    driver.get("https://stellarburgers.education-services.ru/register") 
        # Заполнение полей формы 
    driver.find_element(By.XPATH, locators.registration_account_name_field).send_keys(user_data["name"])
    driver.find_element(By.XPATH, locators.registration_mail_field).send_keys(user_data["email"])
    driver.find_element(By.XPATH, locators.registration_password_field).send_keys(user_data["password"])
    driver.find_element(By.XPATH, locators.registration_button).click()
    WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.education-services.ru/login'))
    assert driver.current_url == 'https://stellarburgers.education-services.ru/login'
                
    # Возвращаем данные, чтобы их можно было использовать внутри тестов
    return user_data

@pytest.fixture(scope="function")
def auth_user(driver, user_data):
    """Выполняет авторизацию на сайте """
    driver.get("https://stellarburgers.education-services.ru/login") 
        # Заполнение полей формы 
    driver.find_element(By.XPATH, locators.sign_in_email_field).send_keys(user_data["email"])
    driver.find_element(By.XPATH, locators.password_field).send_keys(user_data["password"])
    driver.find_element(By.XPATH, locators.sign_in_button).click()
    element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.create_order_button)))
    assert element.text == 'Оформить заказ'
                    
    # Возвращаем данные, чтобы их можно было использовать внутри тестов
    return user_data
    
