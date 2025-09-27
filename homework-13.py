# 1 задание
def fibonacci_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":

    n = int(input("Введите номер числа Фибоначчи: "))

    for num in fibonacci_generator(n):
        print(num, end=" ")

# 2 задание
def cycle_generator(sequence):
    while True:
        for item in sequence:
            yield item

if __name__ == "__main__":
    n = int(input("Введите количество чисел для вывода: "))

    seq = [1, 2, 3]

    gen = cycle_generator(seq)
    for i in range(n):
        num = next(gen)
        print(num, end=" ")

# 3 задание
class Pizza:
    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        ingredients = []
        if self.cheese: ingredients.append("Cheese")
        if self.pepperoni: ingredients.append("Pepperoni")
        if self.mushrooms: ingredients.append("Mushrooms")
        if self.onions: ingredients.append("Onions")
        if self.bacon: ingredients.append("Bacon")
        return f"Pizza size: {self.size}, ingredients: {', '.join(ingredients) if ingredients else 'None'}"

class PizzaBuilder:
    def __init__(self, size):
        self.pizza = Pizza(size)

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        self.builder.add_cheese().add_pepperoni().add_bacon()
        return self.builder.build()

if __name__ == "__main__":
    builder = PizzaBuilder("Large")
    director = PizzaDirector(builder)
    pizza = director.make_pizza()
    print(pizza)

# 4 задание
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

if __name__ == "__main__":
    factory = AnimalFactory()
    animal_type = input("Введите тип животного (dog/cat): ").lower()
    animal = factory.create_animal(animal_type)
    print(animal.speak())

# 5 задание
class Addition:
    def execute(self, a, b):
        return a + b

class Subtraction:
    def execute(self, a, b):
        return a - b

class Multiplication:
    def execute(self, a, b):
        return a * b

class Division:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль!")
        return a / b

class Calculator:
    def __init__(self):
        self.strategy = None  # текущая стратегия не установлена

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        if self.strategy is None:
            raise ValueError("Стратегия не установлена!")
        return self.strategy.execute(a, b)

if __name__ == "__main__":
    calc = Calculator()

    calc.set_strategy(Addition())
    print("5 + 3 =", calc.calculate(5, 3))

    calc.set_strategy(Subtraction())
    print("5 - 3 =", calc.calculate(5, 3))

    calc.set_strategy(Multiplication())
    print("5 * 3 =", calc.calculate(5, 3))

    calc.set_strategy(Division())
    print("5 / 3 =", calc.calculate(5, 3))