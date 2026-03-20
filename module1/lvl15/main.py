class User:
    """
    Базовий клас користувача.

    Важливо для студентів:
    - "Базовий" клас задає мінімальний, зрозумілий інтерфейс
    - "Дочірній" клас може розширювати або змінювати поведінку
    """

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def display_name(self) -> str:
        """Публічне ім'я для UI/логів."""
        return self.username

    def greet(self) -> str:
        """Поводження за замовчуванням."""
        return f"Hi, I'm {self.display_name()}."

    def permissions(self) -> list[str]:
        """
        Повертаємо список прав.
        Це простий приклад: права тут як рядки.
        """
        return ["read"]


class Admin(User):
    """
    Admin "є" User, але з додатковими можливостями.

    Зверніть увагу:
    - Admin успадковує всі атрибути/методи User
    - але може додати свої атрибути/методи або перевизначити існуючі
    """

    def __init__(self, username: str, email: str, level: int) -> None:
        super().__init__(username=username, email=email)
        self.level = level

    def display_name(self) -> str:
        return f"{self.username} (admin lvl {self.level})"

    def permissions(self) -> list[str]:
        base = super().permissions()
        return ["read"] + ["ban_users", "delete_posts"]

    def ban_user(self, user: "User") -> str:
        return f"Admin {self.username} banned {user.username}"



# user1 = User("User1", "testemail@gmail.com")
# print(user1.display_name())
# user2 = User("User2", "")
# print(user2.display_name())
# admin = Admin("Admin", "admin@gmail.com", 3)
# print(admin.display_name())


class PriceCalculator:
    """
    Уявимо "production-like" компонент: рахує підсумкову ціну.
    Це база, яку можна розширювати різними правилами.
    """

    def total(self, subtotal: float) -> float:
        return subtotal


class TaxedPriceCalculator(PriceCalculator):
    """Додає податок поверх базової логіки."""

    def __init__(self, tax_rate: float) -> None:
        self.tax_rate = tax_rate

    def total(self, subtotal: float) -> float:
        base_total = super().total(subtotal)
        return base_total * (1 + self.tax_rate)


class DiscountedAndTaxedCalculator(TaxedPriceCalculator):
    """
    Приклад ланцюжка успадкування, де super() "проходить" по MRO.
    Спочатку застосуємо знижку, а потім податок (через super()).
    """

    def __init__(self, tax_rate: float, discount: float) -> None:
        super().__init__(tax_rate=tax_rate)
        self.discount = discount

    def total(self, subtotal: float) -> float:
        discounted = subtotal * (1 - self.discount)
        return super().total(discounted)


def demo_override_and_super() -> None:
    print("\n=== demo_override_and_super ===")

    subtotal = 100.0
    base = PriceCalculator()
    taxed = TaxedPriceCalculator(tax_rate=0.2)
    discounted_and_taxed = DiscountedAndTaxedCalculator(tax_rate=0.2, discount=0.1)

    print("Base total:", base.total(subtotal))
    print("Taxed total:", taxed.total(subtotal))
    print("Discounted + taxed total:", discounted_and_taxed.total(subtotal))


# demo_override_and_super()


class LoggerMixin:
    def log(self, message):
        print(f"LOG: {message}")

class Page:
    def __init__(self, content):
        self.content = content

class LoggablePage(Page, LoggerMixin):
    def show_and_log(self):
        self.log(f"Showing page content: {self.content}")
        print(self.content)


# page = LoggablePage("My secret content")
# page.show_and_log()


class A:
    def action(self) -> str:
        return "A.action"

class B(A):
    def action(self) -> str:
        return f"B -> {super().action()}"

class C(A):
    def action(self) -> str:
        return f"C -> {super().action()}"

class D(B, C):
    def action(self) -> str:
        return f"D -> {super().action()}"

d = D()
d.action()


class A:
    def action(self) -> str:
        return "A"


class B:
    def action_2(self) -> str:
        return f"B"


class C(A):
    def action(self) -> str:
        return f"C"


class D(B, C):
    def action(self) -> str:
        return super().action()


d = D()
print(D.mro())
print(d.action())


# class Test:
#     __slots__ = ("a", "b")
#
#     def __init__(self, a: int, b: int) -> None:
#         self.a = a
#         self.b = b