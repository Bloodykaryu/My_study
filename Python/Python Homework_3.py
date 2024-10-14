import sqlite3


"""Создание БД"""
db = sqlite3.connect('mobile.db') #создание БД
cur = db.cursor() #переменная для управления бд

"""Создание таблиц mobile_users и mobile_tariff"""
cur.execute("""CREATE TABLE IF NOT EXISTS mobile_users(
     UserID INTEGER PRIMARY KEY AUTOINCREMENT,
     User_name TEXT NOT NULL,
     Balance INTEGER NOT NULL,
     Mobile_tariff_ref INTEGER NOT NULL,
     Activity TEXT NOT NULL);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS mobile_tariff(
     TariffID INTEGER PRIMARY KEY AUTOINCREMENT,
     Tariff TEXT NOT NULL,
     Price INTEGER NOT NULL);
""")
db.commit() #сохранение запроса

"""Заполнение таблицы mobile_users"""
cur.execute("""SELECT User_name FROM mobile_users;""") #запрос для получения всех user_name из таблицы mobile_users
users = [i[0] for i in cur.fetchall()] #составление списка из имен пользователей
users_data = [('User1', 10000, 2, 'YES'),('User2', 10000, 3, 'YES'),('User3', 10000, 1, 'YES')]
for user in users_data: #цикл для списка users_data
    if user[0] not in users: #если userID нет в списке пользователей выполняется запрос на добавление его в таблицу
        cur.execute("""INSERT INTO mobile_users(User_name, Balance, Mobile_tariff_ref, Activity)
            VALUES(?, ?, ?, ?);""",user)
        db.commit()

"""Заполнение таблицы mobile_tariff"""
cur.execute("""SELECT Tariff FROM mobile_tariff;""") #запрос для получения всех тарифов
tariffs = [i[0] for i in cur.fetchall()] #составление списка из тарифов
tariff_data = [('Standard', 500),('VIP', 1000),('Premium', 1500)]
for tariff in tariff_data: #цикл для списка тарифов
    if tariff[0] not in tariffs: #если тарифа нет в списке тарифов выполняется запрос на добавление его в таблицу
        cur.execute("""INSERT INTO mobile_tariff(Tariff, Price)
            VALUES(?, ?);""",tariff)
        db.commit()



"""Возврат баланса к первоначальному значению"""
def initial_data():
    with sqlite3.connect('mobile.db') as db:
        cur = db.cursor()  # переменная для управления бд
        cur.execute("""SELECT User_name FROM mobile_users""")
        users = [i[0] for i in cur.fetchall()]
        for user in users:
            cur.execute(f"""UPDATE mobile_users SET Balance = 10000 WHERE User_name = '{user}'""")
            cur.execute(f"""UPDATE mobile_users SET Activity = 'YES' WHERE User_name = '{user}'""")


"""Проверка правильного формата переменной month"""
def check_month(months):
    try: #Проверка на преобразования строки в число
        months = int(months)
        if months > 0: #проверка на неотрицательное значение
            return True
        else:
            print('Количество месяцев должно быть больше 0')
            return False
    except:
        return False

"""Получение данных из таблицы в формате пользователь : баланс, сумма для списания"""
def getting_balance(db):
    cur = db.cursor()
    cur.execute("""SELECT User_name, Balance, Price, Activity FROM mobile_users LEFT JOIN mobile_tariff on Mobile_tariff_ref = TariffID""")
    balance = {i[0] : i[1:] for i in cur.fetchall()}
    return balance


"""Списание денежных средств с баланса"""
def withdraw_balance(num):
    with sqlite3.connect('mobile.db') as db:
        cur = db.cursor()
        users_data = getting_balance(db) #получение данных
        for key in users_data.keys():
            new_balance = users_data[key][0] - users_data[key][1]
            if new_balance >= 0: #если новый баланс не отрицательный
                cur.execute(f"""UPDATE mobile_users SET Balance = {new_balance} WHERE User_name = '{key}'""")
                db.commit()
                print(f'{key} снятие денежных средств {users_data[key][1]} за месяц №{num}')
            elif users_data[key][2] == 'YES': #если баланс стал отрицательным, а статус активности до сих пор Активен
                cur.execute(f"""UPDATE mobile_users SET Activity = 'NO' WHERE User_name = '{key}'""")
                print(f'{key} недостаточно денежных средств на балансе')


"""Функция с программой списания денежных средств с баланса"""
def start():

    # initial_data() #функция для возврата первоначальных значений

    months = input('Введите период расчета: ') #Ввод количества месяцев для расчета
    while check_month(months) == False: #Функция по проверке что введено целое число
        print('Введено неккоректное значение')
        months = input('Введите период расчета: ')

    """Цикл по списанию денежных средств с баланса"""
    for num in range(1, int(months)+1): #цикл для запуска функции по списанию денежных средств с баланса
        withdraw_balance(num) #функция списания денежных средств с баланса




start() #запуск программы

