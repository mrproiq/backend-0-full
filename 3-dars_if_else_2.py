# 1-masala
# T = float(input("Ob havo haroratini kiriting: "))
# if T<0:
#     print('Sovuq')
# elif T>=0 and T<=20:
#     print('Salqin')
# elif  T>=21 and T<=30:
#     print('Iliq')
# else:
#     print('Issiq')

# 2-masala
# x = float(input("Xarid summangizni kiriting: "))
# if x<=0:
#     print("Qarzga savdo qilinmaydi!!!")
# elif x>0 and x<50000:
#     narx = x
#     print("Sizga chegirma yo'q va to'lovingiz",narx,"so'm.")
# elif x>=50000 and x<100000:
#     narx = x-x*5/100
#     print("Xaridingiz 5% chegirma bilan", narx, "so'm.")
# else:
#     narx = x-x*10/100
#     print("Xaridingiz 10% chegirma bilan", narx, "so'm.")

# 3-masala
# login = input("loginni kiriting: ")
# parol = input("parolni kiriting: ")
# if login=="admin" and parol=="12345":
#     print("Xush kelibsiz,admin!")
# else:
#     print("Login yoki parol xato")

# 4-masala
# yosh = int(input("Yoshingizni kiriting: "))
# if yosh<=0:
#     print("Siz hali tug'ilmagansiz")
# elif yosh<13:
#     print("Sizga ushbu film tavsiya etilmaydi")
# elif yosh>=13 and yosh<=17:
#     print("Siz filmni ota onangiz bilan ko'rishingiz mumkin")
# else:
#     print("Siz filmni tomosha qilishingiz mumkin")

# 5-masala
# taom = input("Menudan yoqtirgan taomingizni tanlang: ")
# if taom=="Osh":
#     narx = 25000
#     t = 5
#     print("Narxi",narx,"tayyorlanish vaqti",t,"min.")
# elif taom=="Mastava":
#     narx = 20000
#     t = 4
#     print("Narxi",narx,"tayyorlanish vaqti",t,"min.")
# elif taom=="Shashlik":
#     narx = 45000
#     t = 10
#     print("Narxi",narx,"tayyorlanish vaqti",t,"min.")

# 6-masala
# pochta = input("Emailingizni kiriting: ")
# if pochta.find("@")==-1:
#     print("Noto'g'ri email manzili")
# elif pochta.find(".")==-1:
#     print("Noto'g'ri email manzili")
# else:
#     print("Email qabul qilindi")

# 7-masala
# ball=int(input("Balingizni kiriting(0 dan 100gacha): "))
# if ball>0 and ball<55:
#     print("2 baho")
# elif ball>=55 and ball<=69:
#     print("3 baho")
# elif ball>=70 and ball<=85:
#     print("4 baho")
# elif ball>=86 and ball<=100:
#     print("5 baho")

# 8-masala
# bor_pul = float(input("Kartangdagi bor pulingizni kiriting: "))
# yechiladigan_pul = float(input("Yechiladigan pulingizni kiriting: "))
# if bor_pul<yechiladigan_pul:
#     print("Hisobda yetarli mablag' mavjud emas")
# elif yechiladigan_pul<5000:
#     print("Minimal yechish summasi 5000 so'm")
# else:
#     print("Pul muvoffaqqiyatli yechildi")
#     qolgan_narx=bor_pul-yechiladigan_pul
#     print("Kartangizdagi qoldiq",qolgan_narx,"so'm.")

# 10-masala
# trafik = float(input("Oylik trafigingizni kiriting: "))
# if trafik<1:
#     print("Sizga 'Mini' ta'rifi mos keladi")
# elif trafik>=1 and trafik<5:
#     print("Sizga 'Standart' ta'rifi mos keladi")
# else:
#     print("Sizga 'Unlimited' ta'rifi mos keladi")
