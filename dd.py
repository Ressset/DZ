print(" ")
print("Задание #1")
my_list = [10, None, -30, 'True', True, 4.8]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)

print(" ")
print("Задание #2")
el_count = int(input(" - Введите количество элементов списка: "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка: "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

print(" ")
print("Задание #3")
seasons_list = ['RUS:  Зима', 'RUS:  Весна', 'RUS:  Лето', 'RUS:  Осень']
seasons_dict = {1 : 'ENG:  Winter', 2 : 'ENG:  Spring', 3 : 'ENG:  Summer', 4 : 'ENG:  Autumn'}
month = int(input(" - Введите номер месяца: "))
if month ==1 or month == 12 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print(" - Не корректная дата.Такого месяца не существует.")

print(" ")
print("Задание #4")
my_str = input("введите первое слово: ")
my_str2 = input("введите воторое слово: ")
items = [my_str, my_str2]
for i, item in enumerate(items):
    print(i + 1, item)

print(" ")
print("Задание #5")
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число *111 - выход для выхода* "))
while digit != 111:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"Текущий список - {my_list}")
    digit = int(input("Введите число "))

print(" Задание 6 не получилось ")