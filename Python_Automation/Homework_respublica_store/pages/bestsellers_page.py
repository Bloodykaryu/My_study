import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Bestseller_page(Base):
    """locators"""

    loc_left_price_point = '(//div[@class="vue-slider-dot"])[1]' #локатор точки нижней цены
    loc_right_price_point = '(//div[@class="vue-slider-dot"])[2]' #локатор точки высшей цены

    loc_show_button = '//button[@class="filter-check-button"]' #локатор кнопки показать
    loc_show_button_2 = '(//button[@class="filter-check-button"])[2]' #локатор кнопки показать 2
    loc_show_button_3 = '(//button[@class="filter-check-button"])[3]' #локатор кнопки показать 3

    loc_year_of_release_2018 = '//span[@class="filter-title"][contains(text(), 2018)]' #локатор фильтра по 2018 году
    loc_type_book_hardcover = '//div[@class="filter-scrollable"]/div/div/div/ul/li/label/span[contains(text(), "Твердая")]' #локатор фильтра по твердой обложке

    loc_message = '//button[@class="popmechanic-submit popmechanic-submit-close"]' #локатор рекламного сообщения

    loc_sort_drop = '(//button[@title="Выбрать способ сортировки"])[2]' #локатор сортировки
    loc_sort_discont = '//li[@title="Сортировать по величине скидки"]'

    loc_discount_product_1 = '(//div[@class="absolute left-0 bottom-0 rounded-tr-md bg-turquoise-500 px-1.5 py-1 text-base font-medium leading-normal h-6 flex justify-center items-center text-white"])[1]' #локатор скидки продукта 1
    loc_discount_product_2 = '(//div[@class="absolute left-0 bottom-0 rounded-tr-md bg-turquoise-500 px-1.5 py-1 text-base font-medium leading-normal h-6 flex justify-center items-center text-white"])[2]' #локатор скидки продукта 2
    loc_discount_product_3 = '(//div[@class="absolute left-0 bottom-0 rounded-tr-md bg-turquoise-500 px-1.5 py-1 text-base font-medium leading-normal h-6 flex justify-center items-center text-white"])[3]' #локатор скидки продукта 3

    loc_button_add_cart_product_1 = '(//div[@class="mt-5"]/button)[1]' #локатор кнопки добавить в корзину продукта 1
    loc_price_product_1 = '(//span[@class="text-xl font-medium text-gray-700 whitespace-nowrap"])[1]' #локатор цены продукта 1
    loc_name_product_1 = '(//a[@class="title-link text-gray-700 text-sm sm:text-base font-medium h-10 sm:h-12 no-underline block w-full overflow-hidden mt-2.5 mb-1.5 hover:text-turquoise-500 hover:no-underline"])[1]' #локатор названия продукта 1

    loc_button_add_cart_product_2 = '(//div[@class="mt-5"]/button)[2]'  # локатор кнопки добавить в корзину продукта 2
    loc_price_product_2 = '(//span[@class="text-xl font-medium text-gray-700 whitespace-nowrap"])[2]'  # локатор цены продукта 2
    loc_name_product_2 = '(//a[@class="title-link text-gray-700 text-sm sm:text-base font-medium h-10 sm:h-12 no-underline block w-full overflow-hidden mt-2.5 mb-1.5 hover:text-turquoise-500 hover:no-underline"])[2]'  # локатор названия продукта 1

    loc_cart_button = '//div[@class="nr-header__user-nav-item relative"]' #локатор кнопки корзины




    """Getters"""

    def get_left_price_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_left_price_point)))

    def get_right_price_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_right_price_point)))

    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_show_button)))

    def get_show_button_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_show_button_2)))

    def get_show_button_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_show_button_3)))

    def get_year_of_release_2018(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_year_of_release_2018)))

    def get_message(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_message)))

    def get_type_book_hardcover(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_type_book_hardcover)))

    def get_sort_drop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_sort_drop)))

    def get_sort_discont(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_sort_discont)))

    def get_discount_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_discount_product_1)))

    def get_discount_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_discount_product_2)))

    def get_discount_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_discount_product_3)))

    def get_button_add_cart_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_button_add_cart_product_1)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_price_product_1)))

    def get_name_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_name_product_1)))

    def get_button_add_cart_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_button_add_cart_product_2)))

    def get_price_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_price_product_2)))

    def get_name_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_name_product_2)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loc_cart_button)))

    """Actions"""

    def move_left_price_point(self,price):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_left_price_point()).move_by_offset(xoffset=price, yoffset=0).release().perform()
        print('Change lower border of price')

    def move_right_price_point(self,price):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_right_price_point()).move_by_offset(xoffset=-int(price), yoffset=0).release().perform()
        print('Change higher border of price')

    def click_show_button(self):
        self.get_show_button().click()
        print('click show button')
        time.sleep(5)

    def click_show_button_2(self):
        self.get_show_button_2().click()
        print('click show button')
        time.sleep(5)

    def click_show_button_3(self):
        self.get_show_button_3().click()
        print('click show button')
        time.sleep(5)

    def click_year_of_release_2018(self):
        self.get_year_of_release_2018().click()
        print('click year of release 2018')

    def click_type_book_hardcover(self):
        self.get_type_book_hardcover().click()
        print('click type book hardcover')

    def click_no_message(self):
        self.get_message().click()
        print('click "No" message')

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_sort_drop(self):
        self.get_sort_drop().click()

    def click_sort_discount(self):
        self.get_sort_discont().click()

    def discount_product_1_text(self):
        return self.get_discount_product_1().text

    def discount_product_2_text(self):
        return self.get_discount_product_2().text

    def discount_product_3_text(self):
        return self.get_discount_product_3().text

    def click_button_add_cart_product_1(self):
        self.get_button_add_cart_product_1().click()

    def int_price_product_1(self):
        return int(self.get_price_product_1().text.replace(' ',''))

    def name_product_1_text(self):
        return self.get_name_product_1().text

    def name_product_2_text(self):
        return self.get_name_product_2().text

    def click_button_add_cart_product_2(self):
        self.get_button_add_cart_product_2().click()

    def int_price_product_2(self):
        return int(self.get_price_product_2().text.replace(' ', ''))



    def click_cart_button(self):
        return self.get_cart_button().click()


    """Methods"""

    def change_left_price(self,l_price):
        self.get_current_url()
        self.move_left_price_point(l_price)
        self.click_show_button()


    def change_right_price(self,r_price):
        self.move_right_price_point(r_price)
        self.click_show_button()


    def choose_year_of_release_2018(self):
        # self.scroll_to_element(self.get_year_of_release_2018())
        self.move_to_elements(self.get_year_of_release_2018())
        self.click_year_of_release_2018()
        self.move_to_elements(self.get_show_button_2())
        self.click_show_button_2()


    def choose_type_book_hardcover(self):
        # self.scroll_to_element(self.get_type_book_hardcover())
        self.move_to_elements(self.get_type_book_hardcover())
        self.click_type_book_hardcover()
        self.move_to_elements(self.get_show_button_3())
        self.click_show_button_3()


    def choose_answer_message(self):
        try:
            self.click_no_message()
        except:
            print('message not found')

    def screen_beginning_of_page(self):
        self.move_to_elements(self.get_right_price_point())
        self.screenshot()

    def choose_discount_sort(self):
        self.move_to_elements(self.get_sort_drop())
        self.click_sort_drop()
        self.click_sort_discount()

    def check_discount_sort(self):
        time.sleep(5)
        discount_1 = int(self.discount_product_1_text().strip('%'))
        discount_2 = int(self.discount_product_2_text().strip('%'))
        discount_3 = int(self.discount_product_3_text().strip('%'))
        assert discount_1 <= discount_2 <= discount_3
        print('discount sort success')

    def add_to_cart_product_1(self):
        self.move_to_elements(self.get_button_add_cart_product_1())
        self.click_button_add_cart_product_1()
        print('add product 1 to cart')

    def add_to_cart_product_2(self):
        self.move_to_elements(self.get_button_add_cart_product_2())
        self.click_button_add_cart_product_2()
        print('add product 2 to cart')

    def go_to_cart(self):
        self.move_to_elements(self.get_cart_button())
        self.click_cart_button()
        print('click cart button')
        time.sleep(3)
        self.assert_url('https://www.respublica.ru/cart')











