# ============================================================
# 1) ІНКАПСУЛЯЦІЯ (Encapsulation)
# ============================================================
# Ідея: "ховати" внутрішній стан і давати доступ через методи/властивості.

class BankAccount:
    """Приклад 1: інкапсулюємо баланс і змінюємо його лише методами."""

    def __init__(self, owner: str, initial: int = 0) -> None:
        self.owner = owner
        self._balance = initial  # _balance — "внутрішнє поле" (домовленість: не чіпати напряму)

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self._balance:
            raise ValueError("Not enough money")
        self._balance -= amount

    def get_balance(self) -> int:
        return self._balance


# account = BankAccount("User1", 1000)
# account.withdraw(200)
#
# print(account.get_balance())


class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.__password = password  # Python перейменує на _User__password

    def check_password(self, attempt: str) -> bool:
        return attempt == self.__password


class ShoppingCart:
    """Приклад 4: ховаємо список товарів, віддаємо тільки копію."""

    def __init__(self) -> None:
        self._items: list[str] = []

    def add(self, item: str) -> None:
        self._items.append(item)

    def items(self) -> list[str]:
        # Повертаємо копію, щоб зовні не могли випадково зламати внутрішній список.
        return list(self._items)


# ============================================================
# 2) НАСЛІДУВАННЯ (Inheritance)
# ============================================================
# Ідея: "дитина" успадковує поведінку/дані "батька" і може розширювати/змінювати.


class Vehicle:
    """Приклад 1: базовий клас для транспорту."""

    def __init__(self, brand: str) -> None:
        self.brand = brand

    def move(self) -> str:
        return "Moving..."


class Car(Vehicle):
    """Має все з Vehicle + додає своє."""

    def honk(self) -> str:
        return "Beep!"


class Bicycle(Vehicle):
    def ring(self):
        return "Ring..."

    def move(self):
        ...


class Bird:
    """Приклад 2: перевизначення методу (override)."""

    def sound(self) -> str:
        return "Some bird sound"


class Sparrow(Bird):
    def sound(self) -> str:
        return "Chirp!"

# bicycle = Bicycle("Mercedes")
# print(bicycle.ring())
# print(bicycle.move())


class Employee:
    """Приклад 3: розширення через super()."""

    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

    def info(self) -> str:
        return f"{self.name}, salary={self.salary}"


class Manager(Employee):
    def __init__(self, name: str, salary: int, team_size: int) -> None:
        super().__init__(name, salary)
        self.team_size = team_size

    def info(self) -> str:
        return f"{super().info()}, team_size={self.team_size}"


# ============================================================
# 3) ПОЛІМОРФІЗМ (Polymorphism) — 4 приклади
# ============================================================
# Ідея: "один інтерфейс — різна поведінка".
# Тобто ми викликаємо однаково, але різні об'єкти роблять по-різному.


class Shape:
    """Приклад 1: поліморфізм через однаковий метод area()."""

    def area(self) -> float:
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, w: float, h: float) -> None:
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r: float) -> None:
        self.r = r

    def area(self) -> float:
        return 3.14159 * self.r * self.r


class Square(Shape):
    def __init__(self, w: float) -> None:
        self.w = w
    def area(self) -> float:
        return self.w * self.w

# shapes = [Circle(5), Rectangle(2, 6), Rectangle(3, 7), Square(7)]
#
# for shape in shapes:
#     print(shape.area())


class Notifier:
    """Приклад 2: однаковий метод send(), різні реалізації."""

    def send(self, message: str) -> None:
        raise NotImplementedError


class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[EMAIL] {message}")


class SMSNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"[SMS] {message}")


# notifiers = [SMSNotifier(), EmailNotifier()]
#
# for n in notifiers:
#     n.send("Всім привіт!")


# ============================================================
# 4) АБСТРАКЦІЯ (Abstraction) — 4 приклади
# ============================================================
# Ідея: показуємо "що робити", але ховаємо "як саме зробити".
# Часто це робиться через абстрактні класи/інтерфейси.


from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """Приклад 1: абстрактний клас — задає інтерфейс pay()."""

    @abstractmethod
    def pay(self, amount: int) -> str:
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount: int) -> str:
        return f"Paid {amount} by card"


class CashPayment(PaymentMethod):
    def pay(self, amount: int) -> str:
        return f"Paid {amount} by cash"


def checkout(payment: PaymentMethod, amount: int) -> None:
    print(payment.pay(amount))


CardPayment()