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
