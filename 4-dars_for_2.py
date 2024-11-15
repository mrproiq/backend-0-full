# Ustoz dars davomida bergan 1-masala
# interest = input("Nimaga qiziqasiz? ")
#
# if interest.find("kitob") >=0 or interest.find("kutubxona") >=0:
#     like = input("Sizga qanday kitoblar yoqadi? ")
#     if like.find("detektiv") >= 0:
#         book = input("Shaytanat kitobi qanday? ")
#         if book.find("zo'r") >=0:
#             print("Siz kalit so'zdan foydalandingiz.Shuning uchun sizga bu kitobni sovg'a qilamiz.")
#         else:
#             print("Sizga bu kitobni o'qishingizni maslahat beraman.")
#     elif like.find("diniy") >=0:
#         print('Sizga "Hadis va hayot kitoblar to\'plamini sovg\'a qilamiz.')
#     else:
#         print("Hozir detektiv va diniy kitoblarimiz bor.Yaqinda boshqa kitoblar ham olib kelamiz.")
# elif interest.find("sport") >=0:
#     sport_type = input("Qaysi sport turiga qiziqasiz? ")
#     if sport_type.find("futbol") >=0:
#         team = input("Qaysi clubni yoqtirasiz? ")
#         if team.find("real")>=0 or team.find("barca")>=0:
#             print("Sizga el-classicoga chipta sovg'a qilamiz.")
#         else:
#             print("Siz sovg'a yuta olmadingiz.")
#     else:
#         print("Yaxshi, ammo futbolga qiziqganingizda sovg'a yutishingiz mumkin edi.")
# else:
#     print("Kechirasiz menda sizning qiziqishingiz haqida ma'lumot yo'q.")

# Dars davomida yechilgan masalalar
# a = -6.7
# b = -8.8
# a1 = abs(a)-int(abs(a))
# b1 = abs(b)-int(abs(b))
# print(a1,b1)
# if a1>b1:
#     print("a sonining qoldiq qismi katta")
# else:
#     print("b sonining qoldiq qismi katta")

# mevalar = ["Olma","Anor","Nok","Banan"]
# for meva in mevalar:
#     print(meva, "mevasi")
#     if meva == "Nok":
#         break
#
# mevalar = ["Olma","Anor","Nok","Banan"]
# for meva in mevalar:
#     if meva == "Nok":
#         continue
#     print(meva, "mevasi")
#
# mevalar = ["Olma","Anor","Nok","Banan"]
# for meva in mevalar:
#
#     if mevalar.index(meva)%2==0:
#         continue
#     print(meva, "mevasi")


# mevalar = ["Olma","Anor","Nok","Banan"]
# for meva in mevalar:
#     if mevalar.index(meva)%2==1:
#         continue
#     print(meva, "mevasi")

# mevalar = ["Olma","Anor","Nok","Banan"]
# for meva in mevalar:
#     if mevalar.index(meva)%3==2:
#         continue
#     print(meva, "mevasi")
# pythontutor.com kodni tushuntirib beradi.
# m = ["a","b","c","d","e","f","a","b","c","d","e","f"]
# natija = []
# for i in m:
#     if i not in natija:
#         natija.append(i)
# print(natija)

# n = int(input("1-son"))
# m = int(input("2-son"))
# for i in range(m):
#     print(n)

# kg = 15_000
# for i in range(1,11):
#     print(f"{i} kg olmaning narxi {i*kg}")

# son = int(input("Sonni kiriting. "))
# natija = 1
# for i in range(1,son+1):
#     natija = natija * i
# print(natija)

# import math
# son = int(input("Sonni kiriting: "))
# chegara = int(math.sqrt(son))
# for i in range(2,chegara+1):
#     if i % 2==0 and i!=2:
#         continue
#     elif son%i==0:
#         print("Tub son emas.")
#         break
# else:
#     print("Tub son")









# Uyga vazifa
# 1-masala
# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for i in pochtalar:
#     if i.find("@")>=0:
#         print("Emailingiz to'g'ri")
#     else:
#         print("Noto'g'ri email: email_manzi")

# 2-masala
# parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]
# for i in parollar:
#     if len(i)<8:
#         print("Juda qisqa")
#     elif i.isalnum()==-1:
#         print("Kuchsiz parol")
#     else:
#         print("Kuchli parol")

# 3-masala
# kundalik_harorat = [20,22, 19, 24, 25, 23, 21]
# sum = 0
# for i in kundalik_harorat:
#     sum = sum + i
#     sum_ortacha = sum / len(kundalik_harorat)
# print(f"O'rtacha harorat {sum_ortacha} ga teng.")
# for i in kundalik_harorat:
#     if i >22:
#         print("Iliq kun")
#     else:
#         print("Salqin")

# 4-masala
# taomlar = ["Osh", "Shashlik", "Manti","Lag’mon"]
# buyurtma = input("Buyurtmangizni kiriting: ")
# for i in taomlar:
#     if i==buyurtma:
#         print("Buyurtmangiz qabul qilindi")
#         break
# else:
#     print("Kechirasiz, bunday taom yo'q")

# 5-masala
# yoshlar = [16, 21, 17,30, 25]
# for i in yoshlar:
#     if i < 18:
#         print("Yosh chegarasiga yetmagan")
#     else:
#         print("Xush kelibsiz")

# 6-masala
# xabarlar = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
# for i in xabarlar:
#     if i =="Batareya past":
#         print("Telefoningizni quvvatlang")

# 7-masala
# fayllar = ["kitob.jpg","ko'k_jiguli.mp3","tabiat.jpg","malohat.mp3","iphone16.jpg"]
# musiqalar=[]
# rasmlar=[]
# for i in fayllar:
#     if i.find(".jpg")>=0:
#         rasmlar.append(i)
#     else:
#         musiqalar.append(i)
# print(musiqalar)
# print(rasmlar)
