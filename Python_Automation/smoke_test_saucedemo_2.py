import time

from selenium import webdriver #импортируется функция webdriver из selenium
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service #импортируется модуль Service из библиотеки Selenium
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions() #создаем экземпляр класса ChromeOptions и добавляем опцию "detach", чтобы браузер не закрывался после завершения сеанса тестирования.
options.add_experimental_option("detach", True)
g = Service() #создаем экземпляр класса Service, который представляет собой фоновый процесс драйвера Chrome. Этот процесс будет работать в фоновом режиме и управлять браузером.
driver = webdriver.Chrome(options=options, service=g) #создаем экземпляр класса WebDriver, который представляет собой драйвер для управления браузером. В параметре options мы передаем опции, которые мы создали в первых двух строках кода, а в параметре service мы передаем экземпляр класса Service.
base_url = 'https://www.saucedemo.com/' #базовая url
driver.get(base_url) #открыть сайт https://www.saucedemo.com/.
driver.maximize_window() #для разворачивания окна браузера на полный экран

time.sleep(1)

"""Authorization"""
login_standart_user = 'standard_user'
password_all = 'secret_sauce'

user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']") #локатор поля user_name
user_name.send_keys(login_standart_user) #ввод логина
print('input login')
password = driver.find_element(by=By.XPATH, value="//input[@id='password']") #локатор поля password
password.send_keys(password_all) #ввод пароля
print('input password')
button_login = driver.find_element(by=By.XPATH, value="//input[@value='Login']") #локатор кнопки логин
button_login.click() #клик по кнопке логин
print('ckick login buttom')

time.sleep(1)

"""Info Product #1"""
product_1 = driver.find_element(by=By.XPATH, value="//a[@id='item_1_title_link']") #локатор первого товара
value_product_1 = product_1.text #название первого товара
print(f'name of the product #1: {value_product_1}')

price_product_1 = driver.find_element(by=By.XPATH, value='//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div') #локатор цены первого товара
value_price_product_1 = price_product_1.text #цена первого товара
print(f'price of the product #1: {value_price_product_1}')

"""Add product #1 to cart"""
select_product_1 = driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']") #локатор кнопки добавления в корзину
time.sleep(1)
select_product_1.click() #клик по кнопке добавления в корзину
print(f"{value_product_1} added in cart")


"""Info Product #2"""
product_2 = driver.find_element(by=By.XPATH, value="//a[@id='item_5_title_link']")
value_product_2 = product_2.text #название продукта
print(f'name of the product #2: {value_product_2}')

price_product_2 = driver.find_element(by=By.XPATH, value='//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div')
value_price_product_2 = price_product_2.text #цена продукта
print(f'price of the product #1: {value_price_product_2}')

"""Add product #2 to cart"""
select_product_2 = driver.find_element(by=By.XPATH, value="//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
time.sleep(1)
select_product_2.click()
print(f"{value_product_2} added in cart")


"""Enter cart"""
shopping_cart_link = driver.find_element(by=By.XPATH, value="//a[@class='shopping_cart_link']")
shopping_cart_link.click()
print('Enter cart')

"""Info Cart Product #1"""
cart_product_1 = driver.find_element(by=By.XPATH, value="//a[@id='item_1_title_link']")
value_cart_product_1 = cart_product_1.text #название продукта
assert value_product_1 == value_cart_product_1
print('Name Cart Product #1 is correct')

cart_price_product_1 = driver.find_element(by=By.XPATH, value='//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
value_cart_price_product_1 = cart_price_product_1.text #цена продукта
assert  value_price_product_1 == value_cart_price_product_1
print('Price Cart Product #1 is correct')

"""Info Cart Product #2"""
cart_product_2 = driver.find_element(by=By.XPATH, value="//a[@id='item_5_title_link']")
value_cart_product_2 = cart_product_2.text #название продукта
assert value_product_2 == value_cart_product_2
print('Name Cart Product #2 is correct')

cart_price_product_2 = driver.find_element(by=By.XPATH, value='//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
value_cart_price_product_2 = cart_price_product_2.text #цена продукта
assert  value_price_product_2 == value_cart_price_product_2
print('Price Cart Product #2 is correct')

time.sleep(1)

"""Click Checkout"""
button_checkout = driver.find_element(by=By.XPATH, value="//button[@class='btn btn_action btn_medium checkout_button ']")
button_checkout.click()
print('Click checkout')

"""Input user info"""
first_name = driver.find_element(by=By.XPATH, value="//input[@id='first-name']") #поиск локатора
first_name.send_keys('Amely') #ввод данных в элемент
print('Input first_name')
last_name = driver.find_element(by=By.XPATH, value="//input[@id='last-name']")
last_name.send_keys('Grey')
print('Input last_name')
zip = driver.find_element(by=By.XPATH, value="//input[@id='postal-code']")
zip.send_keys('1234')
print('Input postal_code')

time.sleep(1)

button_continue = driver.find_element(by=By.XPATH, value="//input[@id='continue']")
button_continue.click()
print('Click continue')


"""Info finish Product_1"""
finish_product_1 = driver.find_element(by=By.XPATH, value="//a[@id='item_1_title_link']")
value_finish_product_1 = finish_product_1.text #название продукта
assert value_product_1 == value_finish_product_1
print('Name product #1 in cart is correct')

finish_price_product_1 = driver.find_element(by=By.XPATH, value='//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
finish_value_price_product_1 = finish_price_product_1.text #цена продукта
assert  value_price_product_1 == finish_value_price_product_1
print('Price product #1 in cart is correct')

"""Info finish Product_2"""
finish_product_2 = driver.find_element(by=By.XPATH, value="//a[@id='item_5_title_link']")
value_finish_product_2 = finish_product_2.text #название продукта
assert value_product_2 == value_finish_product_2
print('Name product #2 in cart is correct')

finish_price_product_2 = driver.find_element(by=By.XPATH, value='//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div')
finish_value_price_product_2 = finish_price_product_2.text #цена продукта
assert  value_price_product_2 == finish_value_price_product_2
print('Price product #2 in cart is correct')

summary_price = driver.find_element(by=By.XPATH, value='//div[@class="summary_subtotal_label"]')
value_summary_price = summary_price.text
print(value_summary_price)

float_finish_value_price_product_1 = float(finish_value_price_product_1.strip('$')) #удаление знака $ из строки и преобразование строки в float формат
float_finish_value_price_product_2 = float(finish_value_price_product_2.strip('$')) #удаление знака $ из строки и преобразование строки в float формат

item_total = 'Item total: $' + str(float_finish_value_price_product_1+float_finish_value_price_product_2) #приведение строки в формат для сравнения с полученной строкой из локатора summary_price

assert  item_total == value_summary_price
print('Summary price is correct')

time.sleep(1)
driver.close() #закрываем окно