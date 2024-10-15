import sys
import time

from faker import Faker
from selenium import webdriver #импортируется функция webdriver из selenium
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service #импортируется модуль Service из библиотеки Selenium
from selenium.webdriver.common.by import By

"""Приветствие"""
print('Приветствую тебя в нашем интернет магазине')
print('Выбери один из следующих товаров и укажи его номер:\n'
      '1 - Sauce Labs Backpack\n'
      '2 - Sauce Labs Bike Light\n'
      '3 - Sauce Labs Bolt T-Shirt\n'
      '4 - Sauce Labs Fleece Jacket\n'
      '5 - Sauce Labs Onesie\n'
      '6 - Test.allTheThings() T-Shirt (Red)\n')

products = {1:"Sauce Labs Backpack", 2: "Sauce Labs Bike Light", 3: "Sauce Labs Bolt T-Shirt", 4: "Sauce Labs Fleece Jacket", 5: "Sauce Labs Onesie", 6: "Test.allTheThings() T-Shirt (Red)"}

"""Введение номера продукта"""
product = int(input('Введите номер: '))

"""Цикл который не отпускает пока не введут то что надо"""
while product not in range(1,7):
    print('Введено неверное значение')
    print('Выбери один из следующих товаров и укажи его номер:\n'
          '1 - Sauce Labs Backpack\n'
          '2 - Sauce Labs Bike Light\n'
          '3 - Sauce Labs Bolt T-Shirt\n'
          '4 - Sauce Labs Fleece Jacket\n'
          '5 - Sauce Labs Onesie\n'
          '6 - Test.allTheThings() T-Shirt (Red)\n')
    product = int(input('Введите номер: '))

print(f'Вы выбрали: {products[product]}')

"""Открытие браузера"""
options = webdriver.ChromeOptions() #создаем экземпляр класса ChromeOptions и добавляем опцию "detach", чтобы браузер не закрывался после завершения сеанса тестирования.
options.add_experimental_option("detach", True)
g = Service() #создаем экземпляр класса Service, который представляет собой фоновый процесс драйвера Chrome. Этот процесс будет работать в фоновом режиме и управлять браузером.
driver = webdriver.Chrome(options=options, service=g) #создаем экземпляр класса WebDriver, который представляет собой драйвер для управления браузером. В параметре options мы передаем опции, которые мы создали в первых двух строках кода, а в параметре service мы передаем экземпляр класса Service.
base_url = 'https://www.saucedemo.com/' #базовая url
driver.get(base_url) #открыть сайт
driver.maximize_window() #для разворачивания окна браузера на полный экран

"""Авторизация"""
login_standart_user = 'standard_user' #логин
password_all = 'secret_sauce' #пароль
user_name = driver.find_element(by=By.XPATH, value="//input[@id='user-name']") #локатор поля user_name
user_name.send_keys(login_standart_user) #ввод логина
print('Введен логин')
password = driver.find_element(by=By.XPATH, value="//input[@id='password']") #локатор поля password
password.send_keys(password_all) #ввод пароля
print('Введен пароль')
button_login = driver.find_element(by=By.XPATH, value="//input[@value='Login']") #локатор кнопки логин
button_login.click() #клик по кнопке логин
print('Клик по кнопке логин')
time.sleep(1)

"""Информация с страницы выбора"""
loc_name = driver.find_element(by=By.XPATH, value=f'(//div[@class="inventory_item_name "])[{product}]') #локатор имени продукта
name = loc_name.text
loc_price = driver.find_element(by=By.XPATH, value=f'(//div[@class="inventory_item_price"])[{product}]') #локатор цены
price = loc_price.text

"""Добавление товара в корзину"""
loc_add_to_cart = driver.find_element(by=By.XPATH, value=f'(//button[contains(text(),"Add to cart")])[{product}]') #локатор кнопки
action = ActionChains(driver) #вызов функции ActionChainc
action.move_to_element(loc_add_to_cart).perform() #перемещение к выбранному товару
time.sleep(1)
loc_add_to_cart.click()
print(name, 'добавлен в корзину по цене: ', price)
time.sleep(1)

"""Переход в корзину"""
shopping_cart_link = driver.find_element(by=By.XPATH, value="//a[@class='shopping_cart_link']")
shopping_cart_link.click()
print('Переход в корзину выполнен')

"""Проверка информации в корзине"""
loc_cart_name = driver.find_element(by=By.XPATH, value='//div[@class="inventory_item_name"]') #локатор наименования в корзине
cart_name = loc_cart_name.text
try:
    assert cart_name == name
    print('Наименование в корзине корректно')
except AssertionError as exception:
    print('Наименование в корзине некорректно')
    driver.close()
    sys.exit(0)

loc_cart_price = driver.find_element(by=By.XPATH, value='//div[@class="inventory_item_price"]') #локатор цены товара в корзине
cart_price = loc_cart_price.text
try:
    assert cart_price == price
    print('Цена в корзине корректна')

except AssertionError as exception:
    print('Цена в корзине некорректна')
    driver.close()
    sys.exit(0)

time.sleep(1)

"""Нажатие кнопки Checkout"""
button_checkout = driver.find_element(by=By.XPATH, value="//button[@class='btn btn_action btn_medium checkout_button ']") #локатор кнопки checkout
button_checkout.click()
print('Клик по кнопке Checkout')

"""Ввод информации о покупателе"""
faker = Faker("en_US") #создания класса для геренации случайных данных на английском языке

first_name = driver.find_element(by=By.XPATH, value="//input[@id='first-name']") #поиск локатора
first_name.send_keys(faker.first_name()) #ввод данных в элемент
last_name = driver.find_element(by=By.XPATH, value="//input[@id='last-name']")
last_name.send_keys(faker.last_name())
zip = driver.find_element(by=By.XPATH, value="//input[@id='postal-code']")
zip.send_keys(str(faker.random_number(digits=4)))
print('Информация о покупателе введена')
time.sleep(1)

"""Нажатие на кнопку Continue"""
button_continue = driver.find_element(by=By.XPATH, value="//input[@id='continue']") #локатор кнопки
button_continue.click()
print('Клик по кнопке Continue')

"""Проверка на финальной странице"""
loc_final_name = driver.find_element(by=By.XPATH, value='//div[@class="inventory_item_name"]') #локатор имени
final_name = loc_final_name.text
try:
    assert final_name == name
    print(f'Наименование на странице оформления заказа корректно: {final_name}')
except AssertionError as exception:
    print('Наименование на странице оформления заказа некорректно')
    driver.close()
    sys.exit(0)

loc_final_price = driver.find_element(by=By.XPATH, value='//div[@class="inventory_item_price"]') #локатор цены товара в корзине
final_price = loc_final_price.text
try:
    assert final_price == price
    print(f'Цена на странице оформления заказа корректна: {final_price}')

except AssertionError as exception:
    print('Цена на странице оформления заказа некорректна')
    driver.close()
    sys.exit(0)

loc_total_price = driver.find_element(by=By.XPATH, value='//div[@class="summary_subtotal_label"]') #локатор окончательной цены
total_price = loc_total_price.text.split()[-1] #взятие из текста локатора цены

try:
    assert total_price == price
    print(f'Окончательная цена на странице оформления заказа корректна: {total_price}')

except AssertionError as exception:
    print('Окончательная цена на странице оформления заказа некорректна')
    driver.close()
    sys.exit(0)

"""Нажатие кнопки финиш"""
finish_button = driver.find_element(by=By.XPATH, value='//button[@id="finish"]') #локатор кнопки
finish_button.click()

driver.close()

print('Заказ оформлен, спасибо что воспользовались нашими услугами')