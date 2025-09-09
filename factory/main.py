import model_a1


class MainMenu:

    models = {
        'A1': 'model_a1.ModelA1'
    }
    cars = []
    menu = [
        {
            'title': 'Статистика',
            "func": "show_stat"
        },
        {
            'title': 'Создать авто',
            "func": 'create_auto'
        },
        {
            'title': 'Выход',
            "func": 'exit'
        },
    ]

    def __init__(self):
        self.get_command()

    def show_menu(self):
        print("\n\n--||--")
        print("Главное меню: \n")
        for i, item in enumerate(self.menu):
            print(f"{i + 1}) {item.get('title')}")

    def get_command(self):
        self.show_menu()
        command = input('Выберите пункт меню: ')
        try:
            eval('self.' + self.menu[int(command) - 1].get('func'))()
        except Exception:
            print('Неверный пункт меню')
            self.get_command()

    def show_stat(self):
        print(f'Статистика:\nКол-во машин: {self.cars.__len__()}')
        if self.cars.__len__() > 0:
            print("Список машин:")
            for car in self.cars:
                print(car.get_info())
        self.get_command()

    def create_auto(self):
        print("\n\n--||-- \nСоздание авто: \n")
        models_list = "Доступные модели: "
        for model in self.models:
            models_list += f"{model}, "
        print(models_list)
        command = input('Название модели: ')
        self.cars.append(eval(self.models.get(command))())
        print("Машина создана!")
        self.get_command()

    def exit(self):
        print('Завершение работы...')


MainMenu()
