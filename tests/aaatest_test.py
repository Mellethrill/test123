
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_class import Base

driver = webdriver.Chrome(executable_path="C:\\Users\\Пользователь\\PycharmProjects\\resource\\chromedriver.exe")
# url = "https://release-3-10-1.front.ctx.dev.lan/ru/auth/signup"
# driver.get(url)
# driver.maximize_window()
# el = driver.find_element(By.XPATH, "//label[@for='agree']")
# print("элемент ок")
#
# action = ActionChains(driver)
# action.move_to_element_with_offset(el, -1, 0).click().perform()
# print("все ок")
#
#
# url = "https://www.geeksforgeeks.org/"
# driver.get(url)
# driver.maximize_window()
# el = driver.find_element(By.XPATH, "//li[@class='header-main__list-item']")
# action = ActionChains(driver)
# action.move_to_element_with_offset(el, 100, 200).click().perform()

url = "https://ctx.mydevdomain.space/admin/core/emailmessage/"
driver.get(url)
driver.maximize_window()

xx = Base(driver)
xx.last_letter_text()
