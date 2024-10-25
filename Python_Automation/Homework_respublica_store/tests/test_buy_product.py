import time

import pytest
from selenium import webdriver #импортируется функция webdriver из selenium
from selenium.webdriver.chrome.service import Service #импортируется модуль Service из библиотеки Selenium
from pages.bestsellers_page import Bestseller_page
from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page
from pages.main_page import Main_page


def test_buy_products():
    """Открытие браузера"""
    options = webdriver.ChromeOptions()  # создаем экземпляр класса ChromeOptions и добавляем опцию "detach", чтобы браузер не закрывался после завершения сеанса тестирования.
    options.add_experimental_option("detach", True)
    g = Service()  # создаем экземпляр класса Service, который представляет собой фоновый процесс драйвера Chrome. Этот процесс будет работать в фоновом режиме и управлять браузером.
    driver = webdriver.Chrome(options=options, service=g)  # создаем экземпляр класса WebDriver, который представляет собой драйвер для управления браузером. В параметре options мы передаем опции, которые мы создали в первых двух строках кода, а в параметре service мы передаем экземпляр класса Service.
    print('start test 1')

    """Загрузка страницы и авторизация"""
    mp = Main_page(driver)
    mp.autorization()

    """Навигация по каталогу"""
    mp.navigation_catalog_to_bestsellers()

    """Работа с фильтрами"""
    bp = Bestseller_page(driver) #вызов класса страницы бестселлеров

    bp.choose_answer_message()  # отключение рекламного окна

    bp.change_left_price(l_price=20) #передвижение бегунка цены, левого
    bp.change_right_price(r_price=100) #передвижение бегунка цены, правого

    bp.choose_year_of_release_2018() #выбор 2018 года
    bp.choose_type_book_hardcover() #выбор твердой обложки

    """Сортировка"""

    bp.choose_discount_sort() #сортировка по скидке
    bp.check_discount_sort() #проверка сортировки

    """Скриншот с выбранными фильтрами и сортировкой"""
    bp.screen_beginning_of_page() #скрин страницы

    """Выбор товара"""
    bp.add_to_cart_product_1()
    bp.add_to_cart_product_2()

    """Сохранение для последующей проверки"""
    name_products = [bp.name_product_1_text(), bp.name_product_2_text()]
    price_products = [bp.int_price_product_1(), bp.int_price_product_2()]


    """Переход в корзину"""
    bp.go_to_cart()

    """Проверки имени товара и цены в корзине"""
    cp = Cart_page(driver)

    cp.assert_name_product(name_products) #проверка наименований
    cp.assert_price_product(price_products) #проверка цен
    cp.assert_sum_order() #проверка общих сумм

    cp.change_count_product() #изменение количества

    """Сохранение для последующей проверки"""
    total_count = cp.int_count_product()
    total_price = cp.int_total_price()

    """Переход на завершение оформления"""
    cp.place_order()

    chp = Checkout_page(driver)
    """Проверка количества и цены"""
    chp.assert_price(total_price)
    chp.assert_count(total_count)

    time.sleep(2)
    print('test finish')
    driver.close()



