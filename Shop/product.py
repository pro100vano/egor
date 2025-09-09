import abc


class Shop(abc.ABC):
    name = None
    price = None
    count = None #колличество


    def __init__(self,**kwargs):
        if kwargs.get('name') is not None:
            self.name = kwargs.get('name')
        if kwargs.get('price') is not None:
            self.price = kwargs.get('price')
        if kwargs.get('count') is not None:
            self.count = kwargs.get('count')


    def get_info(self): pass



