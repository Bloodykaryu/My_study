import csv
import sqlite3
import random as r
import datetime
import os.path


"""Создание БД"""
db = sqlite3.connect('mobile_calls.db') #создание БД
cur = db.cursor() #переменная для управления бд

"""Создание таблиц mobile_users и mobile_price"""
cur.execute("""CREATE TABLE IF NOT EXISTS mobile_users(
     UserID INTEGER PRIMARY KEY AUTOINCREMENT,
     User TEXT NOT NULL,
     Balance INTEGER NOT NULL);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS mobile_price(
     PriceID INTEGER PRIMARY KEY AUTOINCREMENT,
     Mts_Mts INTEGER NOT NULL,
     Mts_Tele2 INTEGER NOT NULL,
     Mts_Yota INTEGER NOT NULL);
""")
db.commit() #сохранение запроса

"""Заполнение таблицы mobile_users"""
cur.execute("""SELECT User FROM mobile_users;""") #запрос для получения всех пользователей из таблицы mobile_users
users = [i[0] for i in cur.fetchall()] #составление списка из имен пользователей
user_data = ('User1', 500)
if users == []: #если список пользователей не пустой
    cur.execute("""INSERT INTO mobile_users(User, Balance)
        VALUES(?, ?);""",user_data)
    db.commit()

"""Заполнение таблицы mobile_price"""
cur.execute("""SELECT PriceID FROM mobile_price;""") #запрос для получения id
ids = [i[0] for i in cur.fetchall()] #составление списка из id
tariffs = (1, 2, 3)
if ids == []: #если тарифа нет в списке тарифов выполняется запрос на добавление его в таблицу
    cur.execute("""INSERT INTO mobile_price(Mts_Mts, Mts_Tele2, Mts_Yota)
        VALUES(?, ?, ?);""",tariffs)
    db.commit()

"""Создание  файла report_mobile.csv"""
if os.path.exists('report_mobile.csv') != True: #Если файла репорт мобайл не существует
    with open('report_mobile.csv', 'w', newline='') as file: #создать файл репорт мобайл
        columns_data = [('Date', 'Operator', 'Count_min', 'Amount')] #заголовки столбцов
        writer = csv.writer(file, delimiter=';') #запись данных в файл
        writer.writerows( #запись строк в файл
            columns_data
        )





"""Возврат баланса к первоначальному значению"""
def initial_data():
    with sqlite3.connect('mobile_calls.db') as db:
        cur = db.cursor()  # переменная для управления бд
        cur.execute(f"""UPDATE mobile_users SET Balance = 500 WHERE User = 'User1'""")


"""Выбор оператора"""
def choice_operator():
    with sqlite3.connect('mobile_calls.db') as db:
        cur = db.cursor()
        cur.execute("""SELECT * FROM mobile_price""") #получение данных из таблицы mobile_price
        columns = [i[0] for i in cur.description][1:] #список названия операторов
        prices =  [i for i in cur.fetchone()][1:] #список цен
        dict_prices = dict(zip(columns, prices))
        return dict_prices


"""Получение баланса"""
def getting_balance():
    with sqlite3.connect('mobile_calls.db') as db:
        cur = db.cursor()
        cur.execute("""SELECT Balance FROM mobile_users""")  # получение данных из таблицы mobile_users
        balance = cur.fetchone()[0]
        return balance


"""Списание денежных средств с баланса"""
def withdraw_balance(date):
    operators = choice_operator()  # получение словаря в виде оператор : цена
    operator = r.choice(list(operators.keys()))  # выбор рандомного оператора
    price = operators[operator] #получение тарифа по оператору
    count_min = r.randint(1, 10)  # выбор рандомного количества минут
    amount = price*count_min #сумма списания
    balance = getting_balance() #получение баланса
    new_balance = balance - amount #получение новой суммы баланса
    with sqlite3.connect('mobile_calls.db') as db:
        cur = db.cursor()
        if new_balance >= 0:  # проверка баланса на положительное значение
            print(f'Списано {amount} рублей')
            cur.execute(f"""UPDATE mobile_users SET Balance = {new_balance} WHERE User = 'User1'""")
            db.commit()
            report_operation(date, operator, count_min, amount)
        else:
            print('Недостаточно средств на балансе')


"""Создание отчета"""
def report_operation(date, operator, count_min, amount):
    user_data = [(date, operator, count_min, amount )]
    with open('report_mobile.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerows(
            user_data
        )
        print('Данные внесены в отчет об операциях')


"""Программа"""
def start():
    date = datetime.date.today() #получение даты
    initial_data() #возврат баланса к первоначальному значению
    for _ in range(30):
        withdraw_balance(date) #списание с баланса
        date += datetime.timedelta(days=1) #увеличение дня на 1

start()
