from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time # потом убрать мб


class Convert(Base):

    url = "https://release-3-14-0.front.ctx.dev.lan/ru/convert"  # потом можно убрать привязку языка

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы:
    # 1) Header:
    # logo_cryptex_header_link = "//img[@class='logo_1uCv6']" #заменить потом
    # trade_link =
    convert_link = "//a[@href='/ru/convert']"
    blog_header_link = "//a[@href='/blog/']"
    # support_centre_header_link =
    tickets_header_link = "//a[@href='/ru/support/tickets']"
    # language_switch =
    # en_language =
    # ru_language =
    # ch_language =
    # balance_link =
    # balance_dropdown =
    # order_history_dropdown =
    # deposit_dropdown =
    # withdrawal =
    # notification_link =
    # notification_see_all_button =
    # notification_mark_all_as_read_button =
    # id_profile =
    # verification_dropdown =
    # security_dropdown =
    # edit_profile_dropdown =
    # notification_dropdown =
    # referrals_dropdown =
    # merchant_dropdown =
    # log_out_dropdown =
    # sign_in_link =
    # sign_up_link =
    #
    # # 2) Footer:
    # logo_cryptex_footer_link = "//input[@id='login']"
    # home_link =
    # api_link =
    # trading_fees_link =
    # resellers_link =
    # blog_footer_link =
    # press_centre_link =
    # terms_link =
    # privacy_policy_link =
    # exchange_link =
    # broker_footer_link =
    # merchant_link =
    # market_link =
    # currency_converter_link =
    # support_centre_footer_link =
    # tickets_footer_link =
    # otc_deals_link =
    # system_status_link =
    # vk_link =
    # facebook_link =
    # twitter_link =
    # telegram_link =
    # linkedin_link =
    # reddit_link =
    # pinterest_link =
    # quora_link =
    # instagram_link =
    # youtube_link =
    # cruncbase_link =
    # steemit_link =
    # olark_chat_button =




    # 3) Broker:
    # 4) Exchange:
    tab_instant_exchange = "//div[@class='tabHeader_sQFC8']"  # заменить локатор потом

    # 5) For asserts:
    blog_h1 = "//h1[@class='h1']"
    create_ticket_button = "//a[@href='/support/tickets/create']"


    # Получатели:

    def get_convert_link(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.convert_link)))

    def get_tab_instant_exchange(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.tab_instant_exchange)))

    def get_blog_header_link(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.blog_header_link)))

    def get_blog_h1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.blog_h1)))

    def get_tickets_header_link(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.tickets_header_link)))

    def get_create_ticket_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.create_ticket_button)))





    # Действия:

    def click_convert_link(self):
        self.get_convert_link().click()
        print("Клик по переходу в Convert - ОК.")

    def click_blog_header_link(self):
        self.get_blog_header_link().click()
        print("Клик по переходу в Блог - ОК.")

    def click_tickets_header_link(self):
        self.get_tickets_header_link().click()
        print("Клик по переходу в Тикеты - ОК.")








    # тут будет ещё много вариаций взаимодействия с элементами

    # Методы:

    def go_to_convert(self):
        self.click_convert_link()
        self.assert_word(self.get_tab_instant_exchange(), "Мгновенный Обмен")
        self.assert_url("https://release-3-14-0.front.ctx.dev.lan/ru/convert")

    def get_convert(self):
        self.driver.get(self.url)
        print("Переход на страницу Convert - ОК.")
        self.assert_word(self.get_tab_instant_exchange(), "Мгновенный Обмен")
        self.assert_url("https://release-3-14-0.front.ctx.dev.lan/ru/convert")

    def go_to_blog_header_ru(self):
        self.get_convert()
        self.click_blog_header_link()
        self.assert_word(self.get_blog_h1(), "Блог")
        self.assert_url("https://release-3-14-0.front.ctx.dev.lan/blog/")

    def go_to_tickets_header(self):
        self.get_convert()
        self.click_tickets_header_link()
        self.assert_word(self.get_create_ticket_button(), "Создать Тикет")
        self.assert_url("https://release-3-14-0.front.ctx.dev.lan/ru/support/tickets")





    # def authorization(self):
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.input_id("piggy")
    #     self.input_password("33H9w8}HPk")
    #     self.click_sign_in_button()
    #     self.assert_word(self.get_user_name_id(), "piggy")
