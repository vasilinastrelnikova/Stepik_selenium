from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Forhair_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    locator_broccoli_balm = '//a[@href="/collection/balzamy/product/tverdyy-smyagchayuschiy-balzam-dlya-volos-broccoli-hair-balsam-70gr"]'
    locator_shampoo_to_cart = '/html/body/div[2]/div/div/div[2]/div[2]/div[10]/form/button'



    #Getters

    def get_broccoli_balm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_broccoli_balm)))

    def get_shampoo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_shampoo_to_cart)))

    #Actions

    def click_broccoli_balm(self):
        self.get_broccoli_balm().click()

    def click_shampoo_to_cart(self):
        self.get_shampoo().click()

    # Methods

    def goto_description_broccoli_balm(self):
        self.get_current_url()
        self.click_broccoli_balm()
        print("Go to description broccoli balsam")

    def shampoo_to_cart(self):
        self.get_current_url()
        self.click_shampoo_to_cart()
        print("Shampoo to cart")
