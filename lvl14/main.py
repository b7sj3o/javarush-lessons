class Cat:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

    def say_model(self):
        print(f"Cat name is {self.name} and age is {self.get_age()}")

    def get_age(self):
        return self.age

    def __str__(self):
        return f"Кота звати {self.name}"

    def __repr__(self):
        return f"Cat(name={self.name!r}, age={self.age})"


murzik = Cat("Мурзік", 3)
barsik = Cat("Барсік", 5)
some_cat = Cat()

# murzik.say_model()
# barsik.say_model()
# some_cat.say_model()

# print(murzik)


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    pass


dog = Dog("Rex", 5)

# isinstance - перевіряє не сам клас, а й батьківські класи
# Також можна передавати tuple класів для перевірки
if isinstance(dog, Animal):
    print("Dog is an Animal")
else:
    print("Dog is not an Animal")