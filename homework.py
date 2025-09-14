# 1 задание
class Soda:
    def __init__(self, taste = None):
        self.taste = taste

    def __str__(self):
        if self.taste:
            return f"Газировка с {self.taste} вкусом"
        else:
            return "Газировка без вкуса"

drink_1 = Soda("клубничным")
drink_2 = Soda()
print(drink_1)
print(drink_2)


# 2 задание
class Calculate:
    def __init__(self):
        pass
    def addition(self, x, y):
        print("Сумма:", x + y)

    def subtraction(self, x, y):
        print("Разность:", x - y)

    def multiplication(self, x, y):
        print("Произведение:", x * y)

    def division(self, x, y):
        if y != 0:
            print("Частное:", x / y)
        else:
            print("Ошибка: деление на ноль")

m = Calculate()
m.addition(6, 3)
m.subtraction(6, 3)
m.multiplication(6, 3)
m.division(6, 3)
m.division(6, 0)


# 3 задание
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведён")

    def stop(self):
        print("Автомобиль заглушён")

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type

    def set_year(self, year):
        self.year = year

car1 = Car("Красная", "Легковушка", 2015)
print(car1.color, car1.type, car1.year)

car1.start()
car1.stop()

car1.set_color("Жёлтая")
car1.set_type("Маршрутка")
car1.set_year(2018)

print(car1.color, car1.type, car1.year)


# 4 задание
class Sphere:
    def __init__(self, radius = 1, x = 0, y = 0, z = 0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return (4/3) * 3.14 * (self.radius)**3

    def get_square(self):
        return 4 * 3.14 * (self.radius)**2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        distance = (x - self.x)**2 + (y - self.y)**2 + (z - self.z)**2
        return distance <= self.radius

s1 = Sphere()
s2 = Sphere(2)
s3 = Sphere(3, 1, 4, 3)

print("Объём: ", s1.get_volume())
print("Площадь: ", s2.get_square())
print("Центр: ", s3.get_center())

s1.set_radius(5)
print("Радиус: ", s1.get_radius())

s1.set_center(2,2,3)
print("Новое значение центра радиуса: ", s1.get_center())

print(s1.is_point_inside(1,2,3))
print(s2.is_point_inside(2, 2, 4))


# 5 задание
class SuperStr(str):
    def is_repeatance(self, s):
        if not s:
            return False
        return self == s * (len(self) // len(s))
    def is_palindrom(self):
        return self.lower() == self.lower()[::-1]
a = SuperStr("abcabcabc")
print(a.is_repeatance("abc"))
print(a.is_repeatance("ab"))
print(a.is_repeatance(""))

b = SuperStr("RaceCar")
print(b.is_palindrom())

c = SuperStr("")
print(c.is_palindrom())


# задание 1
class Product:
    def __init__(self, name: str, shop: str, price: float):
        self.__name = name
        self.__shop = shop
        self.__price = price

    def __str__(self):
            return f"Product: {self.__name}, Shop: {self.__shop}, Price: {self.__price}"

    def get_name(self):
            return self.__name

    def get_shop(self):
            return self.__shop

    def get_price(self):
            return self.__price

    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price + other.__price
        return NotImplemented

class Warhouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product: Product):
        self.__products.append(product)

    def get_by_index(self, index: int):
        return self.__products[index]

    def get_by_name(self, name: str):
        for product in self.__products:
            if product.get_name() == name:
                return product
        return None

    def sort_by_name(self):
        self.__products.sort(key=lambda p: p.get_name())

    def sort_by_shop(self):
        self.__products.sort(key=lambda p: p.get_shop())

    def sort_by_price(self):
        self.__products.sort(key=lambda p: p.get_price())

    def show_all(self):
        for product in self.__products:
            print(product)

p1 = Product("Computer", "5 Element", 3000)
p2 = Product("Laptop", "21vek", 1800)
p3 = Product("Tablet", "ElektoSila", 900)

warehouse = Warhouse()

warehouse.add_product(p1)
warehouse.add_product(p2)
warehouse.add_product(p3)

print("Sort for index: ", warehouse.get_by_index(1))
print("Sort for name: ", warehouse.get_by_name("Computer"), "\n")

print("Sort for price: ")
warehouse.sort_by_price()
warehouse.show_all()

print("Combination of products: ", p1 + p2)


# задание 2
class Pcheloslon:
    def __init__(self, bee: int, elephant: int):
        self.__bee = bee
        self.__elephant = elephant

    def fly(self):
        return self.__bee >= self.__elephant

    def trumpet(self):
        if self.__elephant >= self.__bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal:str, value:int):
        if meal == "nectar":
            self.__bee += value
            self.__elephant -= value
        elif meal == "grass":
            self.__bee -= value
            self.__elephant += value
        else:
            raise ValueError("Invalid meal")

    def __str__(self):
        return f"Pcheloslon (bee: {self.__bee}, elephant: {self.__elephant})"

ps = Pcheloslon(70, 30)

print(ps.fly())
print(ps.trumpet())
ps.eat("nectar", 20)
print(ps)
ps.eat("grass", 50)
print(ps)


# 3 задание
class Bus:
    def __init__(self, max_seats: int, max_speed: int):
        self.__speed = 0
        self.__max_seats = max_seats
        self.__max_speed = max_speed
        self.__passengers = []
        self.__seats = {i: None for i in range(1, self.__max_seats + 1)}
        self.__has_free_seats = True

    def __update_free_flag(self):
        self.__has_free_seats = any(seat is None for seat in self.__seats.values())

    def board(self, names):
        if isinstance(names, str):
            names = [names]
        for name in names:
            for seat, passenger in self.__seats.items():
                if passenger is None:
                    self.__seats[seat] = name
                    self.__passengers.append(name)
                    break
            else:
                print("No seats available", name)
        self.__update_free_flag()

    def drop(self, names):
        if isinstance(names, str):
            names = [names]
        for name in names:
            if name in self.__passengers:
                self.__passengers.remove(name)
                for seat, passenger in self.__seats.items():
                    if passenger == name:
                        self.__seats[seat] = None
                        break
        self.__update_free_flag()

    def change_speed(self, delta: int):
        self.__speed = self.__speed + delta
        self.__speed = max(0, min(self.__speed, self.__max_speed))

    def __contains__(self, name: str):
        return name in self.__passengers

    def __iadd__(self, name: str):
        self.board(name)
        return self

    def __isub__(self, name: str):
        self.drop(name)
        return self

    def __str__(self):
        return (f"Speed: {self.__speed}, "
               f"Passengers: {self.__passengers}, "
               f"Free seats: {self.__has_free_seats}, "
               f"Seats: {self.__seats}")

bus = Bus(3, 120)

bus += "Oleg"
bus += "Vasia"
print(bus)

print("Oleg" in bus)
print("Dmitry" in bus)

bus.change_speed(80)
print(bus)

bus -= "Oleg"
print(bus)

bus.board(["Sergej", "Viktor"])
print(bus)

bus.change_speed(-30)
print(bus)