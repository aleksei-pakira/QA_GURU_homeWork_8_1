class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        return self.quantity >= quantity

        #raise NotImplementedError

    def buy(self, quantity):
        if self.check_quantity(quantity):
            return True
        else:
            raise ValueError
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        #raise NotImplementedError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    products: dict[Product, int]
    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        self.products[Product] = self.products.get(product, 0) + buy_count
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        #raise NotImplementedError

    def remove_product(self, product: Product, remove_count=None):
        if product in self.products:
            if remove_count > self.products[product] or remove_count is None:
                del self.products[product]
            else:
                self.products[product] -= remove_count


        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        #raise NotImplementedError

    def clear(self):
        self.products.clear()
        #raise NotImplementedError

    def get_total_price(self) -> float:
        checkout_price = 0
        for product, count in self.products.items():
            checkout_price = product.price * count
        return checkout_price
        #raise NotImplementedError

    def buy(self):
        for product, buy_product in self.products.items():
            product.buy(buy_product)

        self.clear()