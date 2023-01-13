from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Forface_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    mask_to_cart = '/html/body/div[2]/div/div/div[2]/div[2]/div[11]/form/button'
    locator_for_hair = '//a[@href="/collection/dlya-volos"]'



    #Getters

    def get_mask_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mask_to_cart)))

    def get_locator_for_hair(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_for_hair)))


    #Actions

    def click_mask_to_cart(self):
        self.get_mask_to_cart().click()

    def click_for_hair(self):
        self.get_locator_for_hair().click()
        print("Go to for hair")

    # Methods

    def put_mask(self):
        self.get_current_url()
        self.click_mask_to_cart()
        print("Put mask")

    def goto_hair(self):
        self.get_current_url()
        self.click_for_hair()
        print("Go to hair")
