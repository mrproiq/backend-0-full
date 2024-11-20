# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr? ")
# height = float(height)

# while

# son = 1
# while son<=10:
#     print(son)
#     son += 2
# print("Dastur tugadi")

# print("Sonning kvadratini hisoblovchi dastur.")
# son = "Istalgan sonni kiriting "
# son += "(dasturni to'xtatish uchun exit deb yozing.): "
#
# while True:
#     qiymat = input(son)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi.')

# sonlar = list(range(1,11))
# for i in sonlar:
#     if i==7:
#         continue
#     print(f"{i} sonining kvadrati {i ** 2} ga teng.")

# son = 0
# while son<10:
#     son +=1
#     if son%2 != 0:
#         continue
#     else:
#         print(son)

# print("Yaqin do'stlaringizni ro'yxatini tuzamiz.")
# friends = []
# n = 1
# while True:
#     savol = f"{n}-do'stingizni ismini kiriting."
#     name = input(savol)
#     friends.append(name)
#     takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n += 1
#     if takrorlash != "ha":
#         break
# print("Yaqin do'stlaringiz ro'yxati")
# for name in friends:
#     print(name)

# print("Do'stlaringizni yoshini saqlaymiz.")
# friends_information = {}
#
# key = True
# while key:
#     name = input("Do'stingizni ismini kiriting? ")
#     yosh = input(f"{name.title()}ning yoshi nechida? ")
#     friends_information[name] = int(yosh)
#     extra_information = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if extra_information == "yo'q":
#         key = False
# for name,yosh in friends_information.items():
#     print(f"{name.title()} {yosh} yoshda")
# print(friends_information)

# cars = ["nexia","cobalt","gentra","nexia","spark","matiz","damas","tico","nexia"]
# car = "cobalt"
# while car in cars:
#     cars.remove(car)
# print(cars)

# talabalar = ["akbarshoh","baxtiyor","nilufar","xurshida"]
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi.")
#     baholangan_talabalar[talaba] = int(baho)
# print(baholangan_talabalar)

# n = 1
# sum = 0
# while n<=100:
#     sum += n
#     n +=1
# print(f"1 dan 100 gacha bo'lgan sonlarning yig'indisi {sum} ga teng.")
# n = -1
# while n <= 0:
#     n = input("Musbat son kiriting: ")
#     n = int(n)
#     if n<=0:
#         print("Bu musbat son emas.")
# print("E bo'larkanu")


# son = 1
# while son<=31:
#     print(son)
#     son+=1
#
# from random import randint
# yangi_kod = randint(130,135)
# kodlar = [130,131,134,135]
# i = 0
# while yangi_kod in kodlar:
#     i += 1
#     yangi_kod = randint(130,135)
# print("Takrorlanishlar soni", i)
# print(yangi_kod)

# Dastur sizdan malumot kiritishini soraydi kiritilgan malumot
# int tipiga mansub bolsa dastur oz ishini tugatadi.
# Agar int tipiga mansub bolmasa yana qayta kiritishini soraydi
# toki int tipidagi malumot kiritilmagunga qadar togri qiymat kiritishi soraladi.

# while True:
#     son = input("Butun son kiriting: ")
#     if son.isdigit():
#         print("Rahmat")
#         break
#     else:
#         print("Xatolik")

#
# satr = input("So'z kiriting: ")
# for s in satr:
#     if s.isdigit():
#         continue
#         # print("Sinish jarayoni", s)
#         # break
#     print(s,end='')

# from turtle import Turtle,Screen
# oyna = Screen()
# oyna.title("Mening oynam")
# chiziq = Turtle()
# chiziq.color("red")
# chiziq.pensize(5)
# chiziq.speed(0)
# chiziq.hideturtle()
# chiziq.up()
# chiziq.goto(250,250)
# chiziq.down()
# chiziq.goto(250,-250)
# chiziq.goto(-250,-250)
# chiziq.goto(-250,250)
# chiziq.goto(250,250)
#
#
# koptok = Turtle()
# koptok.shape('circle')
# koptok.color('blue')
# koptok.up()
# koptok.goto(0,0)
#
# step_x = 3
# step_y = 2
# while True:
#     x,y = koptok.position()
#     if x+step_x >= 250 or x+step_x <= -250:
#         step_x = -step_x
#     if y+step_y >= 250 or y+step_y <= -250:
#         step_y = -step_y
#     koptok.goto(x+step_x,y+step_y)
#
# oyna.mainloop()
