from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Sign_in(Base):

    url = "https://release-3-14-0.front.ctx.dev.lan/ru/auth/signin"  # потом можно убрать привязку языка

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы:

    id = "//input[@id='login']"
    password = "//input[@id='password']"
    sign_in_button = "//button[@type='submit']"
    checkbox = "//label[@for='stay']"  # добавить id
    forgot_password_link = "//a[@href='/en/forgot']"  # добавить id
    forgot_id_link = "//a[@href='/en/forgot/id']"  # добавить id
    toggle_password_button = "//span[@class='icon-eye-off togglePassword_2Ar5H toggle-password']"  # добавить id
    # sign_in_tab =
    # sign_up_tab =
    user_name_id = "//a[@href='/ru/profile/edit']"
    # user_name_id = "//*[@id='__layout']/div/div[1]/div/header/div/div[2]/ul/li[3]/a"


    # Получатели:


    def get_id(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.id)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_sign_in_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_button)))

    def get_checkbox(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkbox)))

    def get_forgot_password_link(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.forgot_password_link)))

    def get_forgot_id_link(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.forgot_id_link)))

    def get_toggle_password_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.toggle_password_button)))

    #def get_sign_in_tab(self):
        #return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_tab)))

    #def get_sign_up_tab(self):
        #return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sign_up_tab)))

    def get_user_name_id(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.user_name_id)))

    # Действия:


    def input_id(self, id):
        self.get_id().send_keys(id)
        print("Ввод ID - ОК.")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Ввод пароля - ОК.")

    def click_sign_in_button(self):
        self.get_sign_in_button().click()
        print("Нажатие кнопки авторизации - ОК.")

    # тут будет ещё много вариаций взаимодействия с элементами

    # Методы:

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.input_id("piggy")
        self.input_password("33H9w8}HPk")
        self.click_sign_in_button()
        self.assert_word(self.get_user_name_id(), "piggy")

