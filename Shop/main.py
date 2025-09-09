class MainMenu:

    menu = [
        {
            'title': 'Все товары',
            'func': "all_product"
        },
        {
            'title': 'Создать товар',
            'func': "create_product"
        },
        {
            'title': 'Завершить работу',
            'func': "exit"
        },
    ]

    def __init__(self):
        self.get_command()

    def show_menu(self):
        print("\n Главное меню: \n")
        for i, item in enumerate(self.menu):
            print(f"{i+1}) {item.get('title')}")

    def get_command(self):
        self.show_menu()
        command = input("\nВыбери пункт меню:")
        try:
            eval('self.' + self.menu[int(command) - 1].get('func'))()
        except Exception:
            print("\nТакого пункта меню не существует")
            self.get_command()


    def all_product(self): pass


    def create_product(self): pass


    def Exit(self):
        print("Завершение работы...")




MainMenu()




