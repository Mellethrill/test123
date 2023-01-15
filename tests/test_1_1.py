# Дефолтная авторизация за поросенка
from selenium import webdriver
import time
from pages.sign_in import Sign_in


def test_authorization():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Пользователь\\PycharmProjects\\resource\\chromedriver.exe")
    print("Начало теста")

    login = Sign_in(driver)
    login.authorization()

    print("Конец теста")
    time.sleep(7)
    driver.quit()
