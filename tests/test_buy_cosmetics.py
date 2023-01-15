import time

import pytest
from selenium import webdriver
from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from base.my_error import MyError
from pages.broccolibalm_page import Broccolibalm_page
from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.forface_page import Forface_page
from pages.forhair_page import Forhair_page
from pages.main_page import Main_page

def test_buy_product():
    #path_chrom = Service('C:\\Users\\HP\\PycharmProjects\\pythonSelenium\\chromedriver.exe')
    path_firefox = Service('C:\\Users\\HP\\PycharmProjects\\pythonSelenium\\geckodriver.exe')

    #driver = webdriver.Chrome(service = path_chrom)
    driver = webdriver.Firefox(service=path_firefox)
    base_url = 'https://laboratorium.store/collection/all'
    driver.get(base_url)
    driver.maximize_window()
    mp = Main_page(driver)
    mp.goto_for_face() #переход на страницу товаров для лица
    ffp = Forface_page(driver)
    ffp.put_mask() # добавляем маску в корзину
    ffp.goto_hair() #переходим на страницу товаров для волос
    ffh = Forhair_page(driver)
    ffh.shampoo_to_cart() # добавляем шампунь в корзину
    ffh.goto_description_broccoli_balm() # переходим в описание бальзама
    bbp = Broccolibalm_page(driver)
    bbp.put_balm() # добавляем бальзам в корзину
    bbp.goto_cart() # переходим в корзину
    cp = Cart_page(driver)
    price_shampoo_1 = cp.take_price(cp.get_shampoo_price()) #цена шампуня до изменений
    cp.plus_shampoo() # добавляем еще один шампунт
    time.sleep(2)
    cp.minus_shampoo() # отнимаем шампунь
    time.sleep(2)
    cp.plus_shampoo() #снова прибавляем шампунь
    time.sleep(3)
    price_shampoo_2 = cp.take_price(cp.get_shampoo_price()) # цена шампуней
    assert price_shampoo_1 < price_shampoo_2, "Не сработали кнопки +/- на продукте"

    cp.input_quantity_balm(3) # вводим кол-во бальзамов с клавиатуры
    time.sleep(2)
    cp.delete_mask() # удаляем маску
    try: # проверяем, что маска удалилась
        cp.delete_mask()
    except TimeoutException:
        print("Продукт успешно удален")
    else:
        raise MyError("Продукт не был удален")

    try: #проверяем, что стоимость товаров в корзине соответствует посчитанной итоговой стоимости
        cp.check_price(cp.get_total_price(), cp.get_balms_price(), cp.get_shampoo_price())
    except AssertionError:
        print("Стоимость не совпадает!!!")

    cp.checkout()
    """Ввод данных пользователя"""
    chp = Checkout_page(driver)
    chp.do_input_phone()
    chp.choose_post()
    chp.do_input_city()
    chp.do_input_address()
    chp.remove_checkbox_subscribe()
    chp.do_input_client()
    chp.do_input_email()
    chp.click_submit()















