
import random

# Генерация списка
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Преобразование списка в one hot вид
one_hot_data = {'is_robot': [], 'is_human': []}

for item in lst:
    if item == 'robot':
        one_hot_data['is_robot'].append(1)
        one_hot_data['is_human'].append(0)
    else:
        one_hot_data['is_robot'].append(0)
        one_hot_data['is_human'].append(1)

# Преобразование one hot данных в формат таблицы
header = f"| {'Index':^5} | {'is_robot':^8} | {'is_human':^8} |"
separator = "+" + "-"*7 + "+" + "-"*10 + "+" + "-"*10 + "+"
rows = [header, separator]
for i in range(len(lst)):
    row = f"| {i:^5} | {one_hot_data['is_robot'][i]:^8} | {one_hot_data['is_human'][i]:^8} |"
    rows.append(row)

# Печать таблицы
table = "\n".join(rows)
print(table)

