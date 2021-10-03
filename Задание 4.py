print(" ")
print("Задание #4")
my_str = input("введите первое слово: ")
my_str2 = input("введите воторое слово: ")
items = [my_str, my_str2]
for i, item in enumerate(items):
    print(i + 1, item)