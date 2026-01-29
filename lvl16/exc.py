# def a():
#     b()
#
# def b():
#     c()
#
#
# def c():
#     return 1/0 # ZeroDivisionError
#
# a()


# try:
#     num1 = int(input("Введіть число 1: "))
#     num2 = int(input("Введіть число 2: "))
#     print(f"{num1}/{num2}={round(num1/num2, 3)}")
# except ValueError:
#     print("Введіть будь ласка число")
# except ZeroDivisionError:
#     print("Не можу поділити на нуль")

# with Session() as session:
#     try:
#         session.start()
#     finally:
#         session.close()
#
# s = input("Enter integer: ")
#
# try:
#     n = int(s)
#     result = 100 / n
# except ValueError:
#     print("That was not an integer.")
# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
# else:
#     print("Result:", result)
# finally:
#     print("Done processing input.")
#
#
# path = "data.txt"
# f = None
#
# try:
#     f = open(path, "r", encoding="utf-8")
#     text = f.read()
# except FileNotFoundError:
#     print("File not found:", path)
# else:
#     print("File length:", len(text))
# finally:
#     if f is not None:
#         f.close()
#     print("File handle closed (if it was opened).")

# import traceback
#
# line = "10, 25, not_a_number, 7"
# parts = [p.strip() for p in line.split(",")]
#
# try:
#     numbers = list(map(int, parts))
# except ValueError as e:
#     # print("Bad value in CSV:", e)
#     traceback.print_exc()
# else:
#     print("Sum:", sum(numbers))
#
# import logging
#
# logging.basicConfig(
#     format="%(asctime)s [%(levelname)s] - %(message)s | %(filename)s:%(lineno)d",
#     level=logging.INFO,
#     filename='error.log',
# )

# def function_c():
#     return 1 / 0
#
# def function_b():
#     function_c()
#
# def function_a():
#     try:
#         function_b()
#     except ZeroDivisionError as e:
#         logging.error("Error: user tried to divide by zero")
#
# function_a()


# def parse_age(raw: str) -> int:
#     """Helper: parse age as int with a clear chained cause."""
#     try:
#         age = int(raw)
#     except ValueError as e:
#         raise ValueError(f"Age must be an integer, got: {raw!r}") from e
#
#     return age
#
#
# parse_age("aws")


class DataParseError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class UserCreationError(Exception):
    def __init__(
            self,
            required_fields: list[str] | None = None,
            message: str = "Помилка створення користувача"
    ):
        self.message = message

        if required_fields is not None:
            self.message += f"Обов'язкові поля: ({", ".join(required_fields)})"
        super().__init__(self.message)


def parse_csv_ints(csv_line: str) -> list[int]:
    """Example 1: wrap ValueError -> DataParseError using `raise from`."""
    parts = [p.strip() for p in csv_line.split(",")]
    try:
        return [int(p) for p in parts]
    except ValueError as e:
        raise DataParseError(f"Expected only integers in CSV, got: {csv_line!r}") from e


def parse_age(raw: str) -> int:
    """Helper: parse age as int with a clear chained cause."""
    try:
        age = int(raw)
    except ValueError as eAge cannot be negative, got:
        raise DataParseError(f"Age must be an integer, got: {raw!r}") from e

    if age < 0:
        raise DataParseError(f": {age}")

    return age


def create_user(user_dict: dict) -> dict:
    try:
        age = parse_age(user_dict["age"])
        return {"name": user_dict.get("name", "Unknown"), "age": age}
    except KeyError as e:
        raise UserCreationError(["age"]) from e
    except DataParseError as e:
        raise UserCreationError(message="Десь є невалідні поля") from e


create_user({
    "age": -12
})