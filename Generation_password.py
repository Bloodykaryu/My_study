def generate_password(length):
    import random

    ENG = [chr(i) for i in range(65, 91) if chr(i) != "O" and chr(i) != "I"]
    eng = [chr(i) for i in range(97, 122) if chr(i) != "l" and chr(i) != "o"]
    nums = [str(i) for i in range(2, 10)]
    symbols = ENG + eng + nums
    password = []
    password.append(random.choice(ENG))
    password.append(random.choice(eng))
    password.append(random.choice(nums))
    while len(password) < length:
        password.append(random.choice(symbols))
    random.shuffle(password)
    return "".join(password)


def generate_passwords(count, length):
    passwords = []
    for i in range(count):
        password = generate_password(length)
        passwords.append(password)
    return passwords


print("Введите количество генерируемых паролей")
n = int(input())
print("Введите длину генерируемого пароля (минимум 3 символа)")
m = int(input())
print(*generate_passwords(n, m), sep="\n")
