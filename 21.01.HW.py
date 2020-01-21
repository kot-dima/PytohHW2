# Ex1

# print("Обчислення вартості поїздки на автомобілі")
# def Travel():
#     km = float(input("Відстань до дачі (км) :\n"))
#     gas = float(input("Росхід автомобіля на 100 км :\n"))
#     valGas = float(input("Вартість пального :\n"))

#     value = (km*(gas/100)*valGas)*2

#     print("Вартість поїздки становить", value, "грн.")
# Travel()





# Ex2

# print("Святкові дні")

# def holiday():
#     day = int(input("Введіть день місяця 1-31 : "))
#     month = int(input("Введіть місяць 1-12 : "))

#     if day == 1 and month == 1:
#         print(day, "/", month, "- НОВИЙ РІК !")
#     elif day == 7 and month == 1:
#         print(day, "/", month, "- Різдво")
#     elif day == 8 and month == 3:
#         print(day, "/", month, "- МІЖНАРОДНИЙ ЖІНОЧИЙ ДЕНЬ")
#     elif day == 9 and month == 5:
#         print(day, "/", month, "- ДЕНЬ ЧОЛОВІКІВ")
#     elif day == 13 and month == 6:
#         print(day, "/", month, "- ДЕНЬ НАРОДЖЕННЯ ДІМИ КОТА")
#     else:
#         print("!!! Я не знаю шо за свято !!!")

# holiday()



# Ex3

# print("Розрахунок швидкості")

# def cros():
#     l = int(input("Введіть відстань в метрах : "))
#     t = int(input("Введіть час в секундах : "))

#     v = (l/1000)/(t/3600)

#     print("Швидкість ", v, " км/год")

# cros()


#Ex4

# from random import randint

# print("ну шо, пограєм :D")

# def play():
#     n = int(input("Введи до скількох будем грати : "))

# pointPC = 0
# pointYOU = 0
# while pointPC or pointYOU <= n:
#     p1 = 0
#     p2 = 0

# input("Кості кидає PC")
#     tryPC1 = randint(1, 6)
#     tryPC2 = randint(1, 6)
#     if tryPC1 == tryPC2:
#         print("Вітаю на костях куш", tryPC1, ":", tryPC2)
#     else:
#         print("На костях", tryPC1, ":", tryPC2)

# input("Кості кидаєш ти")
#     tryYOU1 = randint(1, 6)
#     tryUOU2 = randint(1, 6)
#     if tryYOU1 == tryYOU2:
#         print("Вітаю на костях куш", tryYOU1, ":", tryYOU2)
#     else:
#         print("На костях", tryYOU1, ":", tryYOU2)

# - доробити !!! -

