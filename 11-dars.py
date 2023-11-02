# Muallif: Elmurodov Javohir
# try:
#     son = int(input("Istalgan son kiriting: "))
#     if son % 2 == 0:
#         print("Bu son juft son")
#     else:
#         print("Bu son toq son")
# except:
#     pass
# son = int(input("Son kiriting:"))
# print(10/son)
try:
    son = int(input("Son kiriting:"))
    print(10/son)
except ZeroDivisionError as e:
    print(e)
    print(e.__cause__)
    print(dir(e))
    print("0 ga bo'lib bo'lmaydi")
except Exception as e:
    print(e)
    print(e.__cause__)
    print(dir(e))
    print("0 ga bo'lib bo'lmaydi")
else:
    print("Xatolik yo'q")
