# Muallif: Elmurodov Javohir
# OOP, Inheritance va Polymorphism

# class Animal:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self, sound):
#         print(f"{self.name} {sound} deb gapiradi...")


# class Mushuksimonlar:
#     def body(self):
#         print("Mushuksimonlar dumlari bo'ladi...")


# class Cat(Animal, Mushuksimonlar):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         self.__sound = "meow"

#     def speak(self):
#         print(f"{self.name} meowlaydi...")
#         print(self.__sound)

#     def eat(self, food):
#         print(f"{self.name} {food} ni yeydi...")


# cat_1 = Animal("Murchik", 2)


# cat = Cat("Murchik", 2)
# print(cat.name)
# cat.speak()
# cat.eat("sut")
# cat.body()
# print(cat._Cat__sound)


class Car:

    def __init__(self, model, price, color, build_year):
        self.model = model
        self.price = price
        self.color = color
        self.build_year = build_year

    @classmethod
    def new_car_bmw(cls):
        return cls("BMW", 100000, "black", 2021)

    @staticmethod
    def calculate_price(millage, price):
        return millage*price


bmw = Car.new_car_bmw()
print(bmw.calculate_price(100, 1000))
