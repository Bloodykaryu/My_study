from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Checkout_page(Base):
    """locators"""
    loc_count_product = '//span[@class="text-sm text-gray-secondary"]'
    loc_total_price = '(//div[@class="text-2xl font-bold"])[1]'
    loc_order_price = '(//div[@class="text-xl font-medium"])[1]'


    """Getters"""

    def get_count_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_count_product)))

    def get_order_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_order_price)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_total_price)))


    """Actions"""

    def int_order_price(self):
        return int(self.get_order_price().text.replace(' ',''))

    def int_total_price(self):
        return int(self.get_total_price().text.replace(' ',''))

    def int_count_product(self):
        return int(self.get_count_product().text.split()[0])

    """Methods"""

    def assert_price(self, cart_total_price):
        self.get_current_url()
        total_price = self.int_total_price()
        order_price = self.int_total_price()
        assert total_price == order_price == cart_total_price
        print('order and total price correct')

    def assert_count(self, cart_count):
        total_count = self.int_count_product()
        try:
            assert total_count == cart_count
            print('count correct')
        except:
            print('count incorrect')

    def screenshot(self):
        self.screenshot()























