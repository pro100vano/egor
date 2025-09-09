import car


class ModelA1(car.Car):

    def __init__(self, **kwargs):
        super().__init__(max_speed=100, boost_speed=20, fuel="Бензин", fuel_max=40, price=10_000, model='A1')
        if kwargs.get('color', None) is not None:
            self.color = kwargs.get('color')
        else:
            self.color = 'Серый'
        self.ask_color()

    def get_fuel_type(self):
        return self.fuel

    def get_fuel_max(self):
        return self.fuel_max

    def ask_color(self):
        color = input('Какого цвета? ')
        if color.strip().__len__() > 0:
            self.color = color
