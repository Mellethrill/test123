# Хедер
from selenium import webdriver
import time
from pages.convert import Convert
from pages.sign_in import Sign_in


def test_1():  # из trade переходим в convert
    driver = webdriver.Chrome(executable_path="C:\\ctx_autotests\\utilities\\chromedriver.exe")
    print("Начало теста")

    login = Sign_in(driver)
    login.authorization()

    header = Convert(driver)
    header.go_to_convert()

    print("Конец теста")
    time.sleep(3)
    driver.quit()


def test_2():  # хедер -> блог ру
    driver = webdriver.Chrome(executable_path="C:\\ctx_autotests\\utilities\\chromedriver.exe")
    print("Начало теста")

    login = Sign_in(driver)
    login.authorization()

    header = Convert(driver)
    header.go_to_blog_header_ru()

    print("Конец теста")
    time.sleep(3)
    driver.quit()


def test_3():  # хедер -> тикеты
    driver = webdriver.Chrome(executable_path="C:\\ctx_autotests\\utilities\\chromedriver.exe")
    print("Начало теста")

    login = Sign_in(driver)
    login.authorization()

    header = Convert(driver)
    header.go_to_tickets_header()

    print("Конец теста")
    time.sleep(3)
    driver.quit()

# def test_4(): # хедер -> тикеты
#     driver = webdriver.Chrome(executable_path="C:\\Users\\Пользователь\\PycharmProjects\\resource\\chromedriver.exe")
#     print("Начало теста")
#
#     login = Sign_in(driver)
#     login.authorization()
#
#     header = Convert(driver)
#     header.go_to_tickets_header()
#
#     print("Конец теста")
#     time.sleep(3)
#     driver.quit()

