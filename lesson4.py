import abc


class MyClass(abc.ABC):

    @abc.abstractmethod
    def my_func(self): pass

    @abc.abstractmethod
    def my_func_2(self): pass


class MyClass2(MyClass):

    variable2 = "test2"

    def my_func(self):
        pass

    def my_func_2(self):
        result = super().my_func_2()
        return result + 1


# my_class = MyClass()

#
# my_class = MyClass(variable="Егор")
# my_class2 = MyClass(variable="Иван")
#
# my_class.my_func()
# my_class2.my_func()

