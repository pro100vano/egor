import abc
from tkinter import Tk


class Car(abc.ABC):

    car_window = None  # Окно для создания машины
    max_speed = None  # Макс скорорсть
    boost_speed = None  # Ускорение
    fuel = None  # Вид топлива
    fuel_max = None  # обьем бака
    price = None
    color = None
    model = None  # Название модели

    def __init__(self, **kwargs):
        if kwargs.get('max_speed') is not None:
            self.max_speed = kwargs.get('max_speed')
        if kwargs.get('boost_speed') is not None:
            self.boost_speed = kwargs.get('boost_speed')
        if kwargs.get('fuel') is not None:
            self.fuel = kwargs.get('fuel')
        if kwargs.get('fuel_max') is not None:
            self.fuel = kwargs.get('fuel_max')
        if kwargs.get('price') is not None:
            self.price = kwargs.get('price')
        if kwargs.get('color') is not None:
            self.color = kwargs.get('color')
        if kwargs.get('model') is not None:
            self.model = kwargs.get('model')

    def get_info(self):
        return f"Машина {self.model} цвет: {self.color}, c макс. скоростью {self.max_speed} и ценой {self.price}"

    @abc.abstractmethod
    def get_fuel_type(self): pass

    @abc.abstractmethod
    def get_fuel_max(self): pass

    def asks(self):
        self.car_window = Tk()
        self.car_window.title(self.model)
        self.car_window.geometry("300x400")

    def get_params(self):
        response = {
            "model": self.model,
            "color": self.color
        }
        return response
