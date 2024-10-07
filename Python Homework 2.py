import sqlite3 #подключение sql

"""Создание БД"""
db = sqlite3.connect('exchanger.db') #Создание БД
cur = db.cursor() #Переменная для управления БД

"""Создание таблицы user_data"""
cur.execute("""CREATE TABLE IF NOT EXISTS users_balance(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Balance_RUB FLOAT NOT NULL,
    Balance_USD FLOAT NOT NULL,
    Balance_EUR FLOAT NOT NULL);
""")
db.commit()

"""Добавление пользователя"""
cur.execute("""SELECT * FROM users_balance;""") #получение данных из таблицы
all_id = [i[0] for i in cur.fetchall()] #составление списка из id
new_user = ('100000', '1000','1000') #данные пользователя
if all_id == []: #Добавление пользователя в таблицу если ни одного пользователя не существует
    cur.execute("""INSERT INTO users_balance(Balance_RUB, Balance_USD, Balance_EUR)
        VALUES(?, ?, ?);""", new_user)
    db.commit()

"""Запрос баланса"""
def balance():
    cur.execute("""SELECT * FROM users_balance WHERE UserID = 1;""")  # получение данных из таблицы
    all_money = [float(i) for i in cur.fetchone()][1:]  # составление списка из id
    return all_money

"""Проверка суммы на преобразование в число с плавающей точкой"""
def count(count_currency): #Функция для запроса чисел, пока не введут число удовлетворяющее требованиям
    def check(count_currency): #Функция для проверки может ли число быть преобразовано в число с плавающей точкой
        try:
            float(count_currency)
            return True
        except ValueError:
            return False
    while check(count_currency) != True: # Цикл для проверки, что число преобразуется в число с плав. точкой
        print('Введено неверное значение, допускаются числовые значения')
        count_currency = input('Какая сумма Вас интересует?\n')
    return float(count_currency)

"""Получение данных для обмена"""
rub_usd = 70 #1 доллар к рублю
rub_eur = 80 #1 евро к рублю
usd_eur = 0.87 #1 доллар к евро
eur_usd = 1.15 #1 евро к доллару
var = '123' #Варианты ответа для проверки выбора валюты

print(f'Добро пожаловать в наш обменный пункт, курс валют следующий:\n1 USD = {rub_usd} RUB\n1 EUR = {rub_eur} RUB\n1 USD = {usd_eur} EUR\n1 EUR = {eur_usd} USD') #Информационное сообщение

buy_currency = input('Введите какую валюту желаете получить:\n1. RUB\n2. USD\n3. EUR\n') #Выбор валюты для покупки
while buy_currency not in var or buy_currency == '': #Цикл для проверки ввода необходимых значений
    print('Введено неверное значение, выберите цифру напротив названия валюты.')
    buy_currency = input('Введите какую валюту желаете получить:\n1. RUB\n2. USD\n3. EUR\n')
var = var.replace(buy_currency, '') #Убираем из вариантов ответа выбранную валюту

count_currency = input('Какая сумма Вас интересует?\n') #ввод суммы обмена
count_currency = count(count_currency)
while count_currency <= 0 or count_currency != round(count_currency,2):
    print('Число должно быть больше нуля и иметь не более двух знаков после точки')
    count_currency = input('Какая сумма Вас интересует?\n') #ввод суммы обмена
    count_currency = count(count_currency)


sell_currency = input('Какую валюту готовы предложить взамен?\n1. RUB\n2. USD\n3. EUR\n') #Выбор валюты для продажи
while sell_currency not in var or sell_currency == '': #Цикл для проверки ввода необходимых значений
    print('Введено неверное значение. Необходимо ввести цифру напротив валюты, валюта должна отличаться от валюты для покупки.')
    sell_currency = input('Какую валюту готовы предложить взамен?\n1. RUB\n2. USD\n3. EUR\n')

all_money = balance() #Получение информации из БД

"""Обмен Долларов и Евро на Рубли"""
if buy_currency == '1': #Если выбрана покупка рублей

   if sell_currency == '2': #Если выбрана продажа долларов
       new_count = round(count_currency/rub_usd,2) #сумма запрашиваемой суммы в долларах
       if all_money[1] < new_count:
           print(f'Сумма для покупки недостаточна, на вашем счету {all_money[1]} долларов.\nДля покупки {count_currency} рублей необходимо {new_count} долларов.')
       else:
           new_info = [(round(all_money[1] - new_count,2)),(round(all_money[0] + count_currency,2))]
           cur.execute("""UPDATE users_balance SET Balance_USD = ?, Balance_RUB = ? Where UserID = 1;""", new_info)
           db.commit()
           all_money = balance() # составление списка из id
           print(f'Обмен валюты произведен, списано {new_count} долларов, начислено {count_currency} рублей.\nВаш баланс:\n{all_money[0]} рублей;\n{all_money[1]} долларов;\n{all_money[2]} евро.')

   elif sell_currency == '3': #Если выбрана продажа Евро
       new_count = round(count_currency / rub_eur, 2)
       if all_money[2] < new_count:
           print(f'Сумма для покупки недостаточна, на вашем счету {all_money[2]} евро.\nДля покупки {count_currency} рублей необходимо {new_count} евро.')
       else:
           new_info = [(round(all_money[2] - new_count, 2)), (round(all_money[0] + count_currency, 2))]
           cur.execute("""UPDATE users_balance SET Balance_EUR = ?, Balance_RUB = ? Where UserID = 1;""", new_info)
           db.commit()
           all_money = balance()  # составление списка из id
           print(f'Обмен валюты произведен, списано {new_count} евро, начислено {count_currency} рублей.\nВаш баланс:\n{all_money[0]} рублей;\n{all_money[1]} долларов;\n{all_money[2]} евро.')

"""Обмен Рублей и Евро на Доллары"""
if buy_currency == '2': #Если выбрана покупка долларов

    if sell_currency == '1':  # Если выбрана продажа рублей
        new_count = round(count_currency*rub_usd, 2) #сумма запрашиваемой суммы в рублях
        if all_money[0] < new_count: #Если сумма рублей на счете меньше запрашиваемой суммы в рублях
            print(f'Сумма для покупки недостаточна, на вашем счету {all_money[0]} рублей.\nДля покупки {count_currency} долларов необходимо {new_count} рублей.')
        else:
            new_info = [(round(all_money[0] - new_count, 2)), (round(all_money[1] + count_currency, 2))]
            cur.execute("""UPDATE users_balance SET Balance_RUB = ?, Balance_USD = ? Where UserID = 1;""", new_info)
            db.commit()
            all_money = balance()  # составление списка из id
            print(f'Обмен валюты произведен, списано {new_count} рублей, начислено {count_currency} долларов.\nВаш баланс:\n{all_money[0]} рублей;\n{all_money[1]} долларов;\n{all_money[2]} евро.')

    elif sell_currency == '3':  # Если выбрана продажа Евро
        new_count = round(count_currency * usd_eur, 2) #сумма запрашиваемой суммы в евро
        if all_money[2] < new_count:  #Если сумма евро на счете меньше запрашиваемой суммы в евро
            print(f'Сумма для покупки недостаточна, на вашем счету {all_money[2]} евро.\nДля покупки {count_currency} долларов необходимо {new_count} евро.')
        else:
            new_info = [(round(all_money[2] - new_count, 2)), (round(all_money[1] + count_currency, 2))]
            cur.execute("""UPDATE users_balance SET Balance_EUR = ?, Balance_USD = ? Where UserID = 1;""", new_info)
            db.commit()
            all_money = balance()  # составление списка из id
            print(f'Обмен валюты произведен, списано {new_count} евро, начислено {count_currency} долларов.\nВаш баланс:\n{all_money[0]} рублей;\n{all_money[1]} долларов;\n{all_money[2]} евро.')

"""Обмен Рублей и Долларов на Евро"""
if buy_currency == '3': #Если выбрана покупка евро

    if sell_currency == '1':  # Если выбрана продажа рублей
        new_count = round(count_currency*rub_eur, 2) #сумма запрашиваемой суммы в рублях
        if all_money[0] < new_count: #Если сумма рублей на счете меньше запрашиваемой суммы
            print(f'Сумма для покупки недостаточна, на вашем счету {all_money[0]} рублей.\nДля покупки {count_currency} евро необходимо {new_count} рублей.')
        else:
            new_info = [(round(all_money[0] - new_count, 2)), (round(all_money[2] + count_currency, 2))]
            cur.execute("""UPDATE users_balance SET Balance_RUB = ?, Balance_EUR = ? Where UserID = 1;""", new_info)
            db.commit()
            all_money = balance()  # составление списка из id
            print(f'Обмен валюты произведен, списано {new_count} рублей, начислено {count_currency} евро.\nВаш баланс:\n{all_money[0]} рублей;\n{all_money[1]} долларов;\n{all_money[2]} евро.')

    elif sell_currency == '2':  # Если выбрана продажа долларов
        new_count = round(count_currency * eur_usd, 2) #сумма запрашиваемой суммы в долларах
        if all_money[2] < new_count:  #Если сумма долларов на счете меньше запрашиваемой суммы
            print(f'Сумма для покупки недостаточна, на вашем счету {all_money[1]} долларов.\nДля покупки {count_currency} евро необходимо {new_count} долларов.')
        else:
            new_info = [(round(all_money[1] - new_count, 2)), (round(all_money[2] + count_currency, 2))]
            cur.execute("""UPDATE users_balance SET Balance_USD = ?, Balance_EUR = ? Where UserID = 1;""", new_info)
            db.commit()
            all_money = balance()  # составление списка из id
            print(f'Обмен валюты произведен, списано {new_count} долларов, начислено {count_currency} евро.\nВаш баланс:\n{all_money[0]} рублей;\n{all_money[1]} долларов;\n{all_money[2]} евро.')
