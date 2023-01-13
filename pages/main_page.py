from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    locator_for_face = '//a[@href="/collection/face"]'



    #Getters

    def get_locator_face(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.locator_for_face)))


    #Actions

    def click_for_face(self):
        self.get_locator_face().click()

    # Methods

    def goto_for_face(self):
        self.get_current_url()
        self.click_for_face()
        print("Go to for face")

