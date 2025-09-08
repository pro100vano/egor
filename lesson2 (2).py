# a1 = [  # list
#     "Иван",
#     "Егор",
#     "Алексей"
# ]

# a1 = [
#     [
#         "Иван",
#         "Иван",
#         "Иван"
#     ],
#     [
#         [
#             "1"
#         ],
#         "1",
#         "1",
#     ]
# ]

# a1.append("test")
# v = a1.pop(0)
# v = a1[0]

# l_id = 1
# v = a1[l_id]

# a1.insert(1, "test")
# a1.pop(1)

# a2 = sorted(a1)
# a1.sort()

# a1.reverse()
# a1.__len__()

# print(a1)


# a2 = {  # dict
#     "name": "Иван",
#     "age": "30",
#     "discount": "5"
# }

# v = a2.get('name', "Фамилия")
# v = a2['name2']
# a2["last_name"] = "Файрушин"
# a2.update({'name': "Егор"})

# if "last_name" in a2:
#     a2['last_name'] =
# print("last_name" in a2)

# i = 0
# while i < 0:
#     i += 1
#     print(i)

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
# for item in a1:
#     if item.get('age', 0) >= 30:
#         break
#     print(item.get('name'))
#
# a = 0
# while True:
#     inp = input('Число: ')
#     try:
#         a = int(inp)
#         break
#     except Exception:
#         continue
# print(a)

#
# obj = {
#     "params": "t",
#     "value": 30
# }
#
# if obj is not None and "param" in obj and obj.get('param') == 't':
#     print(obj.get('value'))

# string = input('Строка: ')
#
# if len(string.strip()) > 3:
#     print(string.strip())
# else:
#     print("Error")

