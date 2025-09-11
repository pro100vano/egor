import car
from tkinter import Tk, ttk, messagebox


class ModelA1(car.Car):

    ent_color = None
    ent_price = None

    def __init__(self, **kwargs):
        super().__init__(max_speed=100, boost_speed=20, fuel="Бензин", fuel_max=40, model='A1')
        if kwargs.get('color', None) is not None:
            self.color = kwargs.get('color')
        else:
            self.color = 'Серый'
        if kwargs.get('price', None) is not None:
            self.price = int(kwargs.get('price'))
        else:
            self.price = 10_000

    def get_fuel_type(self):
        return self.fuel

    def get_fuel_max(self):
        return self.fuel_max

    def asks(self):
        super().asks()
        ttk.Label(self.car_window, text='Цвет:').pack()
        self.ent_color = ttk.Entry(self.car_window)
        self.ent_color.pack()
        ttk.Label(self.car_window, text='Цена:').pack()
        self.ent_price = ttk.Entry(self.car_window)
        self.ent_price.pack()
        ttk.Button(self.car_window, text='OK', command=self.save_params).pack()
        return self

    def save_params(self):
        color = self.ent_color.get()
        if color.strip().__len__() > 0:
            self.color = color
        price = self.ent_price.get()
        try:
            if int(price) > self.price:
                self.price = int(price)
        except Exception:
            pass
        messagebox.showinfo(title="Информация", message="Модель А1 добавлена")
        self.car_window.destroy()

    def get_params(self):
        response = super().get_params()
        response['class'] = 'model_a1.ModelA1'
        response['price'] = self.price
        return response
