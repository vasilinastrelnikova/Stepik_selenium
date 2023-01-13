import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    locator_delete_mask = '//div[@data-item-delete="270286708"]'
    locator_plus_shampoo = '//div[@data-item-id="321095605"]//span[@data-quantity-change="1"]'
    locator_minus_shampoo = '//div[@data-item-id="321095605"]//span[@data-quantity-change="-1"]'
    locator_quantity_balm = '//div[@data-item-id="404758501"]//input[@value="1"]'
    locator_price = '//div[@class="js-total"]'
    locator_balms_price = '//div[@class="price full-total-price-404758501"]'
    locator_shampoo_price = '//div[@class="price full-total-price-321095605"]'
    locator_checkout = '//input[@type = "submit"]'

    #Getters

    def get_delete_mask(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_delete_mask)))

    def get_plus_shampoo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_plus_shampoo)))

    def get_minus_shampoo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_minus_shampoo)))

    def get_locator_quantity_balm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_quantity_balm)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_price)))

    def get_balms_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_balms_price)))

    def get_shampoo_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_shampoo_price)))

    def get_locator_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_checkout)))

    #Actions

    def click_delete_mask(self):
        self.get_delete_mask().click()

    def click_plus_shampoo(self):
        self.get_plus_shampoo().click()

    def click_minus_shampoo(self):
        self.get_minus_shampoo().click()

    def input_quantity_balm(self, quantity):
        self.get_locator_quantity_balm().send_keys(Keys.BACKSPACE)
        self.get_locator_quantity_balm().send_keys(quantity)
        self.get_locator_quantity_balm().send_keys(Keys.RETURN)
        print("Input quantity balms:" + str(quantity))

    def click_checkout(self):
        self.get_locator_checkout().click()

    # Methods

    def delete_mask(self):
        self.get_current_url()
        self.click_delete_mask()
        time.sleep(10)
        print("Delete mask")

    def plus_shampoo(self):
        self.get_current_url()
        self.click_plus_shampoo()
        print("Plus shampoo")

    def minus_shampoo(self):
        self.get_current_url()
        self.click_minus_shampoo()
        print("Minus shampoo")

    def checkout(self):
        self.get_current_url()
        self.click_checkout()
        print("Click checkout")



