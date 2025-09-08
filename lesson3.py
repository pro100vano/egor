# db = [
#     {
#         'name': "Иван",
#         'age': 30
#     },
#     {
#         'name': "Егор",
#         'age': 25
#     },
#     {
#         'name': "Алёна",
#         'age': 24
#     },
# ]
#
#
# def print_user_age(user):
#     print(f"Пользователю {user.get('name')} {user.get('age')} лет")
#
#
# def ask_user():
#     name = input("Введите имя пользователя: ")
#     for user in db:
#         if name == user.get('name'):
#             print_user_age(user)
#             return
#     print("Такого пользователя не существует!")
#     ask_user()
#
#
# ask_user()
