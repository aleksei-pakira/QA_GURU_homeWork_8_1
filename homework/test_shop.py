"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        assert product.check_quantity(1)
        assert product.check_quantity(0)
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        assert product.buy(1)
        assert product.buy(0)
        assert product.buy(999)

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, buy_count=2)
        assert cart.products[product] == 2

        cart.add_product(product, buy_count=3)
        assert cart.products[product] == 5

        cart.add_product(product, buy_count=0)
        assert cart.products[product] == 5

    def test_remove_product(self, cart, product):
        cart.add_product(product, buy_count=2)
        cart.remove_product(product)
        assert len(cart.products) == 0

        cart.add_product(product, buy_count=2)
        cart.remove_product(product, remove_count=4)
        assert len(cart.products) == 0

        cart.add_product(product, buy_count=5)
        cart.remove_product(product, remove_count=4)
        assert cart.products[product] == 1

    def test_clear(self, cart, product):
        cart.add_product(product, buy_count=2)
        cart.clear()
        assert len(cart.products) == 0

    def test_get_total_price(self, cart, product, product_count=5):
        cart.add_product(product, product_count)
        assert cart.get_total_price() == 500

    def test_buy_enough_in_shop(self, cart, product):
        cart.add_product(product, buy_count=0)
        cart.buy()
        assert product.quantity == 1000

        cart.add_product(product, buy_count=1)
        cart.buy()
        assert product.quantity == 999

        cart.add_product(product, buy_count=999)
        cart.buy()
        assert product.quantity == 0

    def test_buy_not_enough_in_shop(self, cart, product):
        cart.add_product(product, buy_count=1001)
        with pytest.raises(ValueError):
            cart.buy()