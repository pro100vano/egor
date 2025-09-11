import model_a1
from tkinter import ttk, Tk
import json
import gc


class MainMenu:

    window = None  # дочернее окно
    models = {
        'A1': model_a1.ModelA1
    }
    cars = []
    menu = []

    def __init__(self):
        # наполнение меню
        self.menu.append({"title": "Статистика", "func": self.draw_stat})
        self.menu.append({"title": "Создать авто", "func": self.create_auto})

        # создание окна
        root = Tk()
        root.title('Мой завод')
        root.geometry("300x200")
        self.draw_menu()
        self.load_data()
        root.mainloop()

    def draw_menu(self):
        for item in self.menu:
            btn = ttk.Button(text=item.get('title'), command=item.get('func'))
            btn.pack()

    def draw_stat(self):
        self.window = Tk()
        self.window.title("Статистика")
        self.window.geometry("400x600")
        ttk.Label(self.window, text=f"Кол-во машин: {self.cars.__len__()}").pack()
        if self.cars.__len__() > 0:
            ttk.Label(self.window, text=f"Список машин").pack()
            for car in self.cars:
                ttk.Label(self.window, text=f"{car.get_info()}").pack()

    def create_auto(self):
        self.window = Tk()
        self.window.title("Создать авто")
        self.window.geometry("300x200")
        ttk.Label(self.window, text="Выберите модель").pack()
        for model in self.models:
            ttk.Button(self.window, text=model, command= lambda: self.add_car(model)).pack()

    def add_car(self, model):
        self.cars.append(self.models[model]().asks())
        self.window.destroy()

    def load_data(self):
        try:
            with open('./data.json', 'r') as f:
                for car in json.loads(f.read()):
                    car_class = ""
                    car_paras = ""
                    for param in car:
                        if param != 'class':
                            car_paras += f'{param}="{car[param]}", '
                    self.cars.append(eval(f"{car.get('class')}({car_paras[0:-2]})"))
        except Exception:
            print('Пустая бд')

    def save_data(self):
        with open('./data.json', 'w+') as f:
            f.write(json.dumps([car.get_params() for car in self.cars]))


main_window = MainMenu()
main_window.save_data()
