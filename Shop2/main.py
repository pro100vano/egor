from tkinter import ttk,Tk


class MainMenu:
    products = []
    menu = []
    window = None

    def __init__(self):
        self.menu.append({"title": "Склад", "func": self.draw_stat})
        self.menu.append({"title": "Добавить продукт", "func": self.create_product})


        root = Tk()
        root.title('Мой магазин')
        root.geometry('300x200')
        self.draw_menu()

    def draw_menu(self):
        for item in self.menu:
            btn = ttk.Button(text=item.get('title'), command=item.get('func'))
            btn.pack()

    def draw_stat(self):
        self.window = Tk()
        self.window.title('Продукты на складе')
        self.window.geometry("400x600")
        ttk.Label(self.window, text=f'Наименований: {self.products.__len__()}' )
        if self.products.__len__() > 0:
            ttk.Label(self.window, text=f"Список продуктов: ").pack()
            for product in self.products:
                ttk.Label(self.window, text=f"{product.get_info()}").pack()

    def create_product(self):
        self.window = Tk()
        self.window.title('Добавить продукт')
        self.window.geometry('300x200')
        name_create = ttk.Entry(t)
        cost_create = int(input("Введите количество: "))
        product_create = {'name': name_create,
                          'cost': cost_create}
window = MainMenu()