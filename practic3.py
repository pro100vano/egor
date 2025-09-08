# TODO: Сделать программу, которая имеет базу данных. И ее цель заполнить ее 3-мя записями.
#  В бд содержаться обьекты с именем и возрастом пользователей
#  Необходимо информацию запрашивать через консоль
#
# db = []
#
#
# def new_user_bd():
#     name_user = input("Введите имя пользователя: ")
#     age_user = input("Введите возраст пользователя: ")
#     new_user = {'name': name_user,
#     'age': age_user}
#     db.append(new_user)
#     if len(db) < 3:
#
#         new_user_bd()
#     else:
#         nice_print()
#
#
# def nice_print():
#     for user in db:
#         print(f'Имя: {user.get('name')} Возраст: {user.get('age')}')
#
# new_user_bd()
#
#
# def del_user():
#     name_user = input("Введите имя для удаления пользователя: ")
#     for user in db:
#         if name_user == user.get('name'):
#             db.remove(user)
#             break
#     nice_print()


# del_user()


# TODO: Напишите функцию, рассчитывающую стоимость поездки на такси в зависимости от расстояния.
#  В качестве аргументов функция должна принимать именованные параметры: км – расстояние поездки в километрах,
#  мин_цена – базовый тариф, включающий подачу такси и первые три километра пути,
#  цена_за_км – цена за каждый километр, начиная с четвертого.
#  Рассчитайте и выведите на экран стоимость поездки за 17.5 км,
#  если по умолчанию базовый тариф составляет 2 у.е., а цена за километр сверх минимума – 0.3 у.е.

# min_price = 2
# el_price = 0.3
# dist = input("Введите расстояние: ")
#
#
# def total_price():
#     total = (float(dist) - 3) * el_price + min_price
#     print(f'Цена поездки составит: {total}')
# total_price()




def total_price(min_price = 2,el_price = 0.3):
    dist = float(input("Введите расстояние: "))
    total = (dist - 3) * el_price + min_price

    print(f'Cтоимость поездки составит: {total} у.е.')


total_price()


