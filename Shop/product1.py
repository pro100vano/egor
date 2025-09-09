import product


class SosProduct(product.Product):

    def __init__(self, **kwags):
        super().__init__(name = "Cосиски", price = 120, count = 8)
