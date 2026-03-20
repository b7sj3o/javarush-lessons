class Employee:
    """
    Опис:
    - Створіть клас Employee з атрибутами name, base_salary.
    - Додайте метод get_salary(), який повертає base_salary.
    """

    def __init__(self, name: str, base_salary: float) -> None:
        self.name = name
        self.base_salary = base_salary

    def get_salary(self) -> float:
        return self.base_salary

    def print_salary(self, amount: float):
        print(f"{self.name} Заробив {amount} грн")


class Manager(Employee):
    def __init__(self, name: str, base_salary: float, bonus: float) -> None:
        super().__init__(name, base_salary)
        self.bonus = bonus

    def get_salary(self) -> float:
        return super().get_salary() + self.bonus



class HourlyRateEmployee(Employee):
    def __init__(self, name: str, hourly_rate: float, hours_worked: int):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_salary(self) -> float:
        return self.hourly_rate * self.hourly_rate


employee = Employee('Employee', 15000)
manager = Manager('Manager', 15000, 5000)
hourly_employee = HourlyRateEmployee("Employee 2", 500, 120)

# employee.print_salary(employee.get_salary())
# manager.print_salary(manager.get_salary())
# hourly_employee.print_salary(hourly_employee.get_salary())


class MessageBuilder:
    def build(self, text: str) -> str:
        return text


class TrimBuilder(MessageBuilder):
    """
    Має прибирати пробіли по краях (strip) і викликати базову логіку через super().
    """

    def build(self, text: str) -> str:
        result = super().build(text)
        return result.strip()


class PrefixBuilder(TrimBuilder):
    def build(self, text: str, prefix: str) -> str:
        result = super().build(text)
        return f'{prefix} {result}'


trim_builder = TrimBuilder()
prefix_builder = PrefixBuilder()

print(trim_builder.build("  Привіт!   "))
print(prefix_builder.build(" Привіт!!! ", "[x]"))