import datetime
class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method check word"""


    def check_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """Take price"""


    def take_price(self, price):
        price = price.text
        price = price.replace(" ", "")
        price = price.replace("Р", "")
        price = int(price)
        return price



    """Method check price"""


    def check_price(self, total, price_1, price_2):
        total = self.take_price(total)
        price_1 = self.take_price(price_1)
        price_2 = self.take_price(price_2)
        assert total == price_1 + price_2, "Стоимость не совпадает!!!"
        print("Good prices")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\HP\\PycharmProjects\\mainProject\\screen\\' + name_screenshot)
        print(name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good url")