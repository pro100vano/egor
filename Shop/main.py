import product1


class MainMenu:

    products = []
    products_name = {
        'Сосиски':'product1.SosProduct'
    }
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
            'func': "Exit"
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
        command = input("\nВыбери пункт меню: ")
        try:
            eval('self.' + self.menu[int(command) - 1].get('func'))()
        except Exception:
            print("\nТакого пункта меню не существует")
            self.get_command()


    def all_product(self):
        print(f"В магазине:\nНаименований: {self.products.__len__()}")
        if self.products.__len__() > 0:
            print("Список продуктов:\n")
            for product in self.products:
                print(product.get_info())
        self.get_command()

    def create_product(self):
        print('\n\nДобавить товар в магазин:\n\n')
        products_list = f'Требуемые продукты: '
        for product in self.products_name:
            products_list += f"{product}, "
        print(products_list)
        command = input("Введите название продукта: ")
        self.products.append(eval(self.products_name.get(command))())
        print("Продукт добавлен")
        self.get_command()




    def Exit(self):
        print("Завершение работы...")




MainMenu()




