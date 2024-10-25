import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base



class Cart_page(Base):
    """locators"""

    loc_name_product_1 = '(//a[@class="font-medium text-gray-primary truncate-2 text-sm md:text-base"])[1]' #локатор наименования продукта
    loc_name_product_2 = '(//a[@class="font-medium text-gray-primary truncate-2 text-sm md:text-base"])[2]'  # локатор наименования продукта

    loc_price_product_1 = '(//div[@class="text-turquoise-500 text-xl text-end font-medium pr-4 md:pr-0 whitespace-nowrap"])[1]' #локатор цена продукта
    loc_price_product_2 = '(//div[@class="text-turquoise-500 text-xl text-end font-medium pr-4 md:pr-0 whitespace-nowrap"])[2]'  # локатор цена продукта

    loc_increase_count_product_button = '//button[@title="Увеличить количество товара"]' #локатор увеличения единицы товара
    loc_count_product = '//span[@class="text-gray-primary text-xs"]' #локатор количества товаров
    loc_price_order = '//div[@class="cart-order-item-cost"]' #локатор суммы товаров
    loc_total_price = '//div[@class="text-gray-primary text-2xl font-bold"]' #локатор окончательной суммы
    loc_place_order = '//a[@title="Оформить заказ"]' #локатор кнопки оформления заказа





    """Getters"""

    def get_name_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_name_product_1)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_price_product_1)))

    def get_name_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_name_product_2)))

    def get_price_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_price_product_2)))

    def get_increase_count_product_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_increase_count_product_button)))

    def get_count_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_count_product)))

    def get_order_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_price_order)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_total_price)))

    def get_place_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_place_order)))

    """Actions"""

    def click_increase_count_product_button(self):
        self.get_increase_count_product_button().click()
        print('click increase count product')

    def click_place_order(self):
        self.get_place_order().click()

    def int_price_product_1(self):
        return int(self.get_price_product_1().text.replace(' ',''))

    def int_price_product_2(self):
        return int(self.get_price_product_2().text.replace(' ',''))

    def int_order_price(self):
        return int(self.get_order_price().text.replace(' ',''))

    def int_total_price(self):
        return int(self.get_total_price().text.replace(' ',''))

    def int_count_product(self):
        return int(self.get_count_product().text.split()[1])

    """Methods"""

    def assert_name_product(self,name_products):
        self.get_current_url()
        products = [self.get_name_product_1().text, self.get_name_product_2().text]
        assert sorted(products) == sorted(name_products)
        print('name products correct')

    def assert_price_product(self,price_products):
        prices = [self.int_price_product_1(), self.int_price_product_2()]
        assert sorted(prices) == sorted(price_products)
        print('price products correct')

    def assert_sum_order(self):
        price_product_1 = self.int_price_product_1()
        price_product_2 = self.int_price_product_2()
        sum_price = price_product_1+price_product_2
        order_price = self.int_order_price()
        total_price = self.int_total_price()
        assert  sum_price == order_price == total_price
        print('order and total price correct')



    def change_count_product(self):
        count = self.int_count_product()
        price_product_1 = self.int_price_product_1()
        price_product_2 = self.int_price_product_2()

        self.click_increase_count_product_button()
        time.sleep(3)

        new_price_product_1 = self.int_price_product_1()
        new_sum_price = new_price_product_1+price_product_2
        new_order_price = self.int_order_price()
        new_total_price = self.int_total_price()
        new_count = self.int_count_product()


        assert new_count == count+1
        print('count increase correct')
        assert new_price_product_1 == price_product_1*2
        print('price increase correct')
        assert  new_order_price == new_sum_price == new_total_price
        print('total increase correct')

    def place_order(self):
        self.click_place_order()
        time.sleep(2)
        self.assert_url('https://www.respublica.ru/checkout')

















