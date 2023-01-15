import datetime
from datetime import datetime

from selenium.webdriver.common.by import By


class Base():

    def __init__(self, driver):
        self.driver = driver

    # получение текущего URL:

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Текущий url: " + get_url)

    # сравнение текста:

    def assert_word(self, word, result):
        value_word = word.text
        print(value_word + " <-- наш текст, тестовый принт")  # потом удалить мб
        assert value_word == result
        print("Assert по тексту '" + value_word + "' - ОК.")


    # метод для скриншота:

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_schreenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot("C:\\ctx_autotests\\screen\\" + name_schreenshot)

    # метод для проверки url:

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Assert по URL - ОК.")

    # узнать текущую дату и время + разбить их на строки:
    # потом переделать, чтобы было короче
    def now_date(self):
        now_date = str(datetime.now())
        year = now_date[0:4]
        month = now_date[5:7]
        day = now_date[8:10]
        hour = now_date[11:13]
        minute = now_date[14:16]
        second = now_date[17:19]
        date_good_format = year + "_" + month + "_" + day + "_" + hour + "_" + minute + "_" + second
        # print(now_date)
        # print(year)
        # print(month)
        # print(day)
        # print(hour)
        # print(minute)
        # print(second)
        # print(date_good_format)
        return date_good_format

    def last_letter_text(self):
        self.driver.execute_script("window.open('https://ctx.mydevdomain.space/admin/core/emailmessage/')")
        # self.driver.get("https://ctx.mydevdomain.space/admin/core/emailmessage/")
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("cfk85l")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("inF0Voe9eCLOcZ4W")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        text_selector = self.driver.find_element(By.XPATH, "//*[@id='result_list']/tbody/tr[1]/td[3]")
        text = text_selector.text
        self.driver.switch_to.window(self.driver.window_handles[0])
        print("Авторизовались в админке и взяли код")
        return text
        # code = text[216:222]


        # print(text)
        # print(code)



        # тут переходим на прошлую вкладку