# Muallif: Elmurodov Javohir
# OOP va obyektlar bilan ishlash


# class Car:

#     def __init__(self, model, price, color, build_year):
#         self.model = model
#         self.price = price
#         self.color = color
#         self.build_year = build_year

#     def start(self):
#         print(self.model + " yurmoqda...")

#     def stop(self):
#         print(self.model + " to'xtadi...")

#     def feul(self, feul):
#         print(self.model + "  " + str(feul) + " litr benzin oldi...")

#     # magic method
#     def __str__(self):
#         return f"{self.model} {self.price} {self.color} {self.build_year}"


# volvo = Car('Volvo S90', 50000, 'black', 2020)
# print(volvo)
# print(volvo.model)
# print(volvo.price)
# print(volvo.color)
# print(volvo.build_year)
# volvo.start()
# volvo.stop()
# volvo.feul(20)
# print("--------------------\n")
# nissan = Car('Nissan GTR', 100000, 'red', 2021)
# print(nissan)
# print(nissan.model)
# print(nissan.price)
# print(nissan.color)
# print(nissan.build_year)
# nissan.start()
# nissan.stop()
# nissan.feul(30)


class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Mablag' yetarli emas...")

    def __str__(self):
        return f"{self.name} {self.balance}"


account = Account("Javohir", 100000)
print(account)
account.deposit(50000)
print(account)
account.withdraw(20000)
print(account)
