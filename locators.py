
# Формa регистрации
registration_account_name_field = "//div[contains(@class, 'input') and .//label[text()='Имя']]//input"
registration_mail_field = "//div[contains(@class, 'input') and .//label[text()='Email']]//input"
registration_password_field = "//input[@name='Пароль']"
registration_button = "//button[text()='Зарегистрироваться']"
password_validation_error = "//p[text()='Некорректный пароль']"

# Вход в аккаунт и переход в личный кабинет
sign_in_email_field = "//input[@name='name']"
password_field = "//input[@name='Пароль']"
sign_in_button = "//button[text()='Войти']"
create_order_button = "//button[text()='Оформить заказ']"
sign_in_into_account_button = "//button[text()='Войти в аккаунт']"
personal_cabinet_button = "//a[@href='/account']"

# Переход в конструктор
go_to_constructor = "//p[text()='Конструктор']/.."
constructor_header = "//h1[text()='Соберите бургер']"
logo_link = "//div[contains(@class, 'AppHeader_header__logo')]/a"

# Выход из аккаунта
exit_button = "//button[text()='Выход']"

# Переход к разделам конструктора
buns_section = "//span[text()='Булки']"
sauces_section = "//span[text()='Соусы']"
fillings_section = "//span[text()='Начинки']"

# Раздел конструктора, когда section_name  принимает 1 из 3-х значений: Булки, Соусы, Начинки
active_section = "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='{section_name}']]"