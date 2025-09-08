# TODO: С помощью цикла создать массив из 30 элементов с случайными числами от 1 до 100

# import random
# array_size = 30
# total_list = []
# for i in range(array_size):
#     total_list.append(random.randint(1, 100))
# print(total_list)

# TODO: создать список обьектов пользователей с именем и возрастом, и с помозью цикла вывести в коносоль информацию пользователей
# a1 = [
#     {
#         'name': "Иван",
#         "age": 29
#     },
#     {
#         'name': "Егор",
#         'age': 30
#     },
#     {
#         'name': "Максим",
#         'age': 27
#     }
# ]
#
# for i in a1:
#     i.get('name')
#
#     print(i.get('name'))


# TODO: Напишите программу, в которой в бексонечном цикле пользователь вводит два числа, а программа выводит их сумму.
# Затем программа запрашивает, надо ли завершить ввод. И если пользователь вводит букву "Y" или "y",
# то происходит выход из бесконечного цикла, и программа завершается. При нажатии любой другой клавиши, программа продолжает работу

# while True:
#     a1 = input("Введи число 1: ")
#     a2 = input("введи число 2: ")
#     i = int(a1) + int(a2)
#     print(i)
#     que = input("Надо ли завершить воод?")
#     if que in ["Y", "y"]:
#         break


#TODO: заполнить список случайными числами в диапазоне 20–100 и подсчитать отдельно число чётных и нечётных элементов.
#
# import random
# total_list = []
# a = 0
# for i in range(random.randint(10, 40)):
#     total_list.append(random.randint(20, 100))
# print(total_list)
# for e in total_list:
#     if e % 2 == 0:
#         a +=1
#
#
# print(a)
# print(total_list.__len__() - a)
# #TODO: Посчитайте количество символов в строке 'Python - это Питон!',
# # использовав счетчики на основе циклов for и while

# string = "Python - это Питон!"
# a = 0
# for e in string:
#     a += 1
# print(a)
#
# num = input("Введи число: ")
# fact = 1
# for i in range(1, int(num) + 1):
#     fact *= i
#
# print(fact)

#Вводим число и присваиваем ему переменную.
# Объявляем сам факториал
#Создаем цикл для i в массиве от 1 до n+1
# Внутри цикла fact множаем на i
# Выводим факториал

# #TODO: запросить у пользователя число и заполнить массив всеми четными натуральными числами меньше этого числа
# num = input("Введи число: ")
# total_list = []
# for e in range(1, int(num)):
#     if e % 2 == 0:
#         total_list.append(e)
# print(total_list)

# result = [
#     {
#         "param": "t",
#         "value": 30
#     },
#     {
#         "param": "v",
#         "value": 15
#     },
#     {
#         "param": "c",
#         "value": 10
#     }
# ]
#
# par = input("Введите название параметра: ")
#
# a = 0
# while True:
#     val = input("Введите значение параметра: ")
#     try:
#         a = int(val)
#         break
#     except Exception:
#         continue
#
# obj = {"param": par,
#       "value": int(a)}
#
# result.append(obj)
# print(result)