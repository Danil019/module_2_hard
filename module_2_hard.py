import random

n = random.randint(3, 20)
password_list = []

for i in range(1, 20):
    for j in range(i + 1, 20):
        sum_num = i + j
        if sum_num % n == 0:
            password_list.append(str(i) + str(j))

password = ''.join(password_list)

print(f"Число из первой вставки: {n}")
print(f"Нужный пароль: {password}")