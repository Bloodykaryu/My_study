import sqlite3

"""Создание БД"""
db = sqlite3.connect('registration.db') #Создание БД
cur = db.cursor() #Переменная для управления БД

"""Создание таблицы user_data"""
cur.execute("""CREATE TABLE IF NOT EXISTS user_data(
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Login TEXT NOT NULL,
    Password TEXT NOT NULL,
    Code TEXT NOT NULL);
""")
db.commit()

"""Добавление пользователя 'Ivan'"""
cur.execute("""SELECT * FROM user_data;""") #получение данных из таблицы
all_login = [i[1] for i in cur.fetchall()] #составление списка из логинов в таблице
new_person = ('Ivan', 'qwer1234','1234') #данные пользователя
if new_person[0].title() not in all_login: #Добавление пользователя в таблицу если такого логина в таблице нет
    cur.execute("""INSERT INTO user_data(Login, Password, code)
        VALUES(?, ?, ?);""", new_person)
    db.commit()

"""Функция старта, для выбора действия"""
def start():
    var = input('Для регистрации введите - 1, Для авторизации введите - 2, Для восстановления пароля введите - 3: ')
    while var not in ['1','2','3']:
        print('Введено некоректное значение')
        var = input('Для регистрации введите - 1, Для авторизации введите - 2, Для восстановления пароля введите - 3: ')
    else:
        if var == '1':
            registration()
        elif var == '2':
            avtorization()
        elif var == '3':
            change_password()



"""Функция для проверки логина на уникальность"""
def name():
    login = input('Придумайте логин: ')
    while len(login.strip()) < 1: #цикл для ввода не пустого логина
        login = input('Логин не может быть пустым, придумайте логин: ')
    cur.execute("""SELECT * FROM user_data;""")  # получение данных из таблицы
    all_login = [i[1] for i in cur.fetchall()]  # составление списка из логинов в таблице
    while login.title() in all_login: # цикл по вводу логина пока не будет введен уникальный логин
        print('Данный логин занят другим пользователем')
        login = input('Придумайте логин: ')
    return login



"""Функция для проверки кода"""
def code():
    nums = input('Придумайте 4х значный цифровой код (необходим для возможности восстановления пароля): ')
    while nums.isdigit() == False: #проверка является ли код цифровым
        print('Введены не цифровые значения')
        nums = input('Придумайте 4х значный цифровой код (необходим для возможности восстановления пароля): ')
    while len(str(nums)) != 4: #проверка длины кода
        print('Цифровой код содержит больше или меньше 4х цифр')
        nums = input('Придумайте 4х значный цифровой код (необходим для возможности восстановления пароля): ')
    return nums


"""Функция для проверки пароля"""
def password():
    pas = input('Введите пароль: ')
    while len(pas) < 1: #проверка пароля на "пустой" пароль
        print('Введен слишком короткий пароль')
        pas = input('Введите пароль (не менее 1 символа): ')
    return pas

"""Функция для регистрации пользователя"""
def registration():
    log = name().title() #получение логина
    pas = password() #получение пароля
    cod = code() #получение цифрового кода
    new_person = (log, pas, cod)
    db = sqlite3.connect('registration.db')
    cur = db.cursor()
    cur.execute("""INSERT INTO user_data(Login, Password, code) 
            VALUES(?, ?, ?);""", new_person) #добавление пользователя в БД
    db.commit()
    print('Регистрация пользователя завершена')


"""Функция для авторизации пользователя"""
def avtorization():
    db = sqlite3.connect('registration.db') #подключение к базе
    cur = db.cursor()
    cur.execute("""SELECT * FROM user_data;""") #получение данных из БД
    log_pas = {i[1] : i[2] for i in cur.fetchall()} #составление словаря из логина и пароля пользователей
    log = input('Введите логин: ').title()
    while log not in log_pas:
        print('Пользователь не найден')
        log = input('Введите логин: ').title()
    pas = input('Введите пароль: ')
    while pas != log_pas[log]: #проверка на соответствие логина и пароля
        print('Введен некорректный пароль')
        pas = input('Введите пароль: ')
    else:
        print('Пользователь авторизован')

"""Функция для восстановления пароля"""
def change_password():
    db = sqlite3.connect('registration.db')  # подключение к базе
    cur = db.cursor()
    cur.execute("""SELECT * FROM user_data;""")  # получение данных из БД
    log_cod = {i[1]: i[3] for i in cur.fetchall()}  # составление словаря из логина и кода пользователей
    log = input('Введите логин: ').title()
    while log not in log_cod:
        print('Пользователь не найден')
        log = input('Введите логин: ').title()
    cod = input('Введите цифровой код: ')
    while cod != log_cod[log]: #Проверка на соответсвие кода логину
        print('Введен неверный цифровой код')
        cod = input('Введите цифровой код: ')
    print('Изменение пароля')
    pas = password() #функция по вводу пароля
    data = (pas, log)
    cur.execute("""UPDATE user_data SET Password = ? WHERE Login = ?;""", data) #изменение пароля в БД
    db.commit()
    print('Пароль изменен')


start()
