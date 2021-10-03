print(" ")
print("Задание #1")
my_list = [10, None, -30, 'True', True, 4.8]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)