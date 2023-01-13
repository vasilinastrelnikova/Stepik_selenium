from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Broccolibalm_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    balm_to_cart = '/html/body/div[2]/div[1]/div/div[2]/div[2]/form/button'
    locator_cart = '//span[@class="icon-part added"]'

    #Getters

    def get_balm_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.balm_to_cart)))

    def get_locator_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_cart)))

    #Actions

    def click_balm_to_cart(self):
        self.get_balm_to_cart().click()

    def click_to_cart(self):
        self.get_locator_cart().click()

    # Methods

    def put_balm(self):
        self.get_current_url()
        self.click_balm_to_cart()
        print("Put balm to cart")

    def goto_cart(self):
        self.get_current_url()
        self.click_to_cart()
        print("Go to cart")

