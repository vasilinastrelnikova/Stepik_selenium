from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Checkout_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    locator_phone = '//input[@id="client_phone"]'
    locator_delivery = '//input[@id="shipping_address_full_locality_name"]'
    locator_radio_post = '//*[@id="delivery_variants"]/div[2]/div[3]/label/span[1]/span'
    locator_street = '//input[@id="shipping_address_street"]'
    locator_house = '//input[@id="shipping_address_house"]'
    locator_flat = '//input[@id="shipping_address_flat"]'




    #Getters

    def get_locator_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_phone)))

    def get_locator_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_delivery)))

    def get_radio_post(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_radio_post)))

    def get_locator_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_street)))

    def get_locator_house(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_house)))

    def get_locator_flat(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_flat)))


    #Actions

    def input_phone(self, user_phone):
        self.get_locator_phone().send_keys(user_phone)


    def input_city(self, city):
        self.get_locator_delivery().clear()
        self.get_locator_delivery().send_keys(Keys.RETURN)
        self.get_locator_delivery().send_keys(city)
        self.get_locator_delivery().send_keys(Keys.RETURN)

    def click_post(self):
        self.get_radio_post().click()

    def input_address(self, street, house, flat):
        self.get_locator_street().send_keys(street)
        self.get_locator_house().send_keys(house)
        self.get_locator_flat().send_keys(flat)



    # Methods

    def do_input_phone(self):
        self.get_current_url()
        self.input_phone("+79007990990")
        print("Input phone number")

    def do_input_city(self):
        self.get_current_url()
        self.input_city("Москва")
        print("Input city")

    def choose_post(self):
        self.get_current_url()
        self.click_post()
        print("Click post")

    def do_input_address(self):
        self.get_current_url()
        self.input_address("Первая", "1", "1")
        print("Input address")



