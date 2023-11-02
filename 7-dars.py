

# def test():
#     print("HBS Akademiyasi darslari")


# test()


# def add(num1, num2):
#     print(num1 + num2)


# num1 = int(input("Birinchi raqamni kiriting: "))
# num2 = int(input("Ikkinchi raqamni kiriting: "))
# add(num1, num2)

# input_num1 = int(input("1- sonni kiriting: "))
# input_num2 = int(input("2- sonni kiriting: "))
# input_num3 = int(input("3- sonni kiriting: "))
# input_num4 = int(input("4- sonni kiriting: "))


# def func(num1, num2, num3, num4):
#     print(f"Num1 {num1}")
#     print(f"Num2 {num2}")
#     print(f"Num3 {num3}")
#     print(f"Num4 {num4}")
#     num1 += 1
#     num2 += 1
#     num3 += 1
#     num4 += 1


# print(input_num1, input_num2, input_num3, input_num4)
# func(input_num1, input_num2, input_num3, input_num4)
# print(input_num1, input_num2, input_num3, input_num4)


def power(num, power=2):
    return num**power


son = int(input("Sonni kiriting: "))
daraja = int(input("Darajani kiriting: "))

if daraja < 0:
    natija = power(son)
    print(natija)
else:
    natija = power(power=daraja, num=son)
    print(natija)
