# Дефолтная регистрация
from selenium import webdriver
import time
from pages.sign_up import Sign_up


def test_registration():
    driver = webdriver.Chrome(executable_path="C:\\Users\\Пользователь\\PycharmProjects\\resource\\chromedriver.exe")
    print("Начало теста")

    su = Sign_up(driver)
    su.registration()

    print("Конец теста")
    time.sleep(7)

    driver.quit()
