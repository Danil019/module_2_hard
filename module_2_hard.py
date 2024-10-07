import random

n = random.randint(3, 20)
password_list = []

for i in range(1, n):
    for j in range(i + 1, n):
        sum_num = i + j  # Сумма пары
        if n % sum_num == 0:  # Проверяем делится ли число на сумму
            password_list.append(str(i) + str(j))

password = ''.join(password_list)

print(f"Число из первой вставки: {n}")
print(f"Нужный пароль: {password}")