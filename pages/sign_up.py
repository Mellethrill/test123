from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time

class Sign_up(Base):

    url = "https://release-3-12-0.front.ctx.dev.lan/ru/auth/signup"  # потом можно убрать привязку языка

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы:

    email = "//input[@id='login']"
    password = "//input[@id='password']"
    repeat_password = "//input[@id='confirmPassword']"
    terms_checkbox = "//label[@for='agree']"
    privacy_checkbox = "//label[@for='privacy']"
    sign_up_button = "//button[@type='submit']"
    toggle_password_button = "//span[@class='icon-eye-off togglePassword_2Ar5H toggle-password']"  # добавить id
    # sign_in_tab =
    # sign_up_tab =
    user_name_id = "//a[@href='/profile/edit']"
    email_confirm_tan_text = "//*[@id='__layout']/div/div[2]/div/div/div/div/div[1]/div[2]"
    tan_input = "//input[@class='input w70 invalid']"



    # Получатели:


    def get_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_repeat_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.repeat_password)))

    def get_terms_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.terms_checkbox)))

    def get_privacy_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.privacy_checkbox)))

    def get_sign_up_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_up_button)))

    def get_toggle_password_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.toggle_password_button)))

    #def get_sign_in_tab(self):
        #return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_tab)))

    #def get_sign_up_tab(self):
        #return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_up_tab)))

    def get_user_name_id(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name_id)))

    def get_email_confirm_tan_text(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_confirm_tan_text)))

    def get_tan_input(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.tan_input)))

    # Действия:

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Ввод Email - ОК")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Ввод пароля - ОК")

    def input_repeat_password(self, password):
        self.get_repeat_password().send_keys(password)
        print("Ввод пароля(повторный) - ОК")

    def click_terms_checkbox(self):
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.get_terms_checkbox(), -100, 0).click().perform()
        print("Проставление чекбокса 'Правила использования' - ОК")

    def click_privacy_checkbox(self):
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(self.get_privacy_checkbox(), -100, 0).click().perform()
        print("Проставление чекбокса 'Политика конфиденциальности' - ОК")

    def click_sign_up_button(self):
        self.get_sign_up_button().click()
        print("Нажатие кнопки 'Зарегистрироваться' - ОК")

    def input_tan(self, code):
        self.get_tan_input().send_keys(code)
        print("Нажатие кнопки 'Зарегистрироваться' - ОК")

    # тут будет ещё много вариаций взаимодействия с элементами

    # Методы:

    def registration(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        email = "tester3_" + self.now_date() + "@mail.ru"
        self.input_email(email)
        self.input_password("ctx_autotest_2023")
        self.input_repeat_password("ctx_autotest_2023")
        self.click_terms_checkbox()
        self.click_privacy_checkbox()
        self.click_sign_up_button()
        a = self.get_email_confirm_tan_text()
        print(a)
        #self.assert_word(self.get_email_confirm_tan_text(), "Письмо было отправлено на " + email)
        text = self.last_letter_text()
        code = text[216:222]
        self.input_tan(code)
        time.sleep(2)

        # тут ввод кода тана
        # тут кнопка подтверждение
        # тут ассерт на авторизацию после регистрации по 4 буквам юзер


        # self.input_email("test_")
        # self.input_password("33H9w8}HPk")
        # self.click_sign_in_button()
        # self.assert_word(self.get_user_name_id(), "piggy")