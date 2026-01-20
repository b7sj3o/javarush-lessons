# ============================================================
# @staticmethod
# ============================================================
# staticmethod — це "звичайна функція", але логічно належить класу.
# Вона НЕ отримує ні self, ні cls.


class MathUtils:
    @staticmethod
    def is_even(n: int) -> bool:
        # Перевірка — не потребує доступу до об'єкта чи класу
        return n % 2 == 0
MathUtils.is_even(2)


class PasswordUtils:
    @staticmethod
    def is_strong(password: str) -> bool:
        # Просте правило: мінімум 8 символів і є хоча б одна цифра
        return len(password) >= 8 and any(ch.isdigit() for ch in password)


# ============================================================
# @classmethod
# ============================================================
# classmethod отримує cls (клас), а не self (об'єкт).
# Часто використовується як "альтернативний конструктор" або фабрика.

class Order:
    tax_rate = 0.2  # 20%

    def __init__(self, amount: float) -> None:
        self.amount = amount

    @classmethod
    def with_tax(cls, amount_without_tax: float) -> "Order":
        # Створюємо замовлення, одразу додаючи податок, використовуючи cls.tax_rate
        total = amount_without_tax * (1 + cls.tax_rate)
        return cls(total)


order1 = Order.with_tax(100)
order2 = Order(50)


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int, current_year: int) -> "User":
        # Альтернативний спосіб створення об'єкта
        return cls(name=name, age=current_year - birth_year)


user = User.from_birth_year("User", 2002, 2026)
# print(user.name, user.age)


class Test:
    count = 0

    @classmethod
    def count_up(cls):
        cls.count += 1


obj1 = Test()
obj1.count_up()

obj2 = Test()
obj2.count_up()

# print(Test.count)


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
        Counter.print_count()

    @staticmethod
    def print_count():
        print(Counter.count)


# Counter()
# Counter()
# Counter()


# ============================================================
# @property
# ============================================================
# property дає вигляд "поля", але насправді це метод.
# Використовується для:
# - валідації при встановленні значення
# - обчислюваних властивостей (computed property)


class Product:
    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self._price = price  # піде в setter

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


product = Product("Name", 100)
product.price = 100
