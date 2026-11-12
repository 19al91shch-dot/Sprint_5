from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


import locators


class TestSignIn:     
    #Проверка входа при нажатии на кнопку Войти 
    def test_sign_in_through_into_account_button(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
    
    # Кликаем по кнопке «Войти в аккаунт» на главной странице
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, locators.sign_in_into_account_button))).click()
    
    # Ждём появления поля ввода email (подтверждение, что открылась страница входа)
        email_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_email_field)))
    
        email = "sherbitskaya_alenka_54.123@yandex.kz"
        password = "a1Bcde"
    
    # Заполнение полей 
        email_field.send_keys(email)
        driver.find_element(By.XPATH, locators.password_field).send_keys(password)
    
    # Ждём, пока кнопка Войти станет кликабельной, и кликаем
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, locators.sign_in_button))).click()
    
    # Ждём появления кнопки Оформить заказ
        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.create_order_button)))
    
    # Проверяем наличие текста в кнопке
        assert element.text == "Оформить заказ"



      # Проверка входа при нажатии на кнопку «Личный кабинет»
    def test_sign_in_through_personal_cabinet(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        driver.find_element(By.XPATH, locators.personal_cabinet_button).click()

        # Ждем перехода на страницу входа (появления поля email)
        email_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_email_field)))

        email = 'sherbitskaya_alenka_54.123@yandex.kz'
        password = 'a1Bcde'

        # Заполнение полей на открывшейся странице
        email_field.send_keys(email)
        driver.find_element(By.XPATH, locators.password_field).send_keys(password)

        # Ждем, пока кнопка «Войти» станет кликабельной, и кликаем
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, locators.sign_in_button))).click()

        # Ждем появления кнопки «Оформить заказ»
        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.create_order_button)))
        # Проверяем наличие текста в кнопке
        assert element.text == "Оформить заказ"


        
    #Проверка входа при нажатии на ссылку Войти на странице Регистрации
    def test_sign_in_through_link_in_register_form(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
    
    # Кликаем по ссылке «Войти» в форме регистрации
        driver.find_element(By.XPATH, locators.sign_in_registration_form).click()
    
    # Ждем перехода на страницу входа и появления поля для ввода email
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_email_field)))
    
        email = 'sherbitskaya_alenka_54.123@yandex.kz'
        password = 'a1Bcde'
    
    # Заполнение полей на открывшейся странице
        driver.find_element(By.XPATH, locators.sign_in_email_field).send_keys(email)
        driver.find_element(By.XPATH, locators.password_field).send_keys(password)
    
    # Ждем, пока кнопка «Войти» станет кликабельной, и кликаем
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, locators.sign_in_button))).click()
    
    # Ждем появления кнопки «Оформить заказ»
        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.create_order_button)))
    
    # Проверяем наличие текста в кнопке
        assert element.text == 'Оформить заказ'



    #Проверка перехода на страницу входа при нажатии на ссылку Войти на странице Восстановления пароля
    def test_sign_in_through_link_in_pswd_recovery(self, driver):
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
    
    # Ждем кликабельности ссылки «Войти» на странице восстановления пароля и кликаем
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, locators.sign_in_forgot_password))).click()
    
    # Ждем перехода на страницу входа и появления поля Email
        email_field = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.sign_in_email_field)))
    
        email = 'sherbitskaya_alenka_54.123@yandex.kz'
        password = 'a1Bcde'
    
        email_field.send_keys(email)
        driver.find_element(By.XPATH, locators.password_field).send_keys(password)
    
    # Ждем, пока кнопка «Войти» станет кликабельной, и кликаем
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, locators.sign_in_button))).click()
    
    # Ждем появления кнопки «Оформить заказ»
        element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, locators.create_order_button)))
        assert element.text == 'Оформить заказ'