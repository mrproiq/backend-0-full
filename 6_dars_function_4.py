# 19-lesson
# range() vs list()
# print(list(range(10)))

# def salom_ber():
#     """ Saloom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# salom_ber()
# salom_ber()

# def salom_ber(ism):
#     """ Foydalanuvchidan ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, xurmatli {ism.title()}!")
# salom_ber("Ali")
# salom_ber("Vali")
# print(salom_ber.__doc__)
#
# print(print.__doc__)

# def toliq_ism(ism,familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}.\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}.")
# toliq_ism("Zarif","Quvonov")

# def yosh_hisobla(ism,tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2024-tugilgan_yil} yoshda.")
# yosh_hisobla("ali",2000)
# yosh_hisobla(tugilgan_yil=2002,ism="ali")

# def yosh_hisobla(tugilgan_yil,joriy_yil=2024):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydigan dastur"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz.")
# yosh_hisobla(2000)
# yosh_hisobla(2000,2023)

# def yosh_hisobla(ism,yosh):
#     """Foydalanuvchidan ismi va yoshini so'rab tug'ilgan yilini aniqlovchi dastur"""
#     print(f"{ism} siz {2024-yosh}-yilda tug'ilgansiz.")
# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
# yosh_hisobla(ism,yosh)

# def kvadrat_va_kub(a):
#     """sonning kvadrati va kubini aniqlovchi funksiya"""
#     kvadrat = a**2
#     kub = a**3
#     print(f"sonning kvadrati {kvadrat} ga kubi esa {kub} ga teng!")
# a = int(input("a sonini kiriting: "))
# kvadrat_va_kub(a)

# def toq_yoki_juft(x):
#     """sonning toq yoki juftligini aniqlovchi funksiya"""
#     if x<0:
#         print("Kiritilgan son manfiy.Musbat son kiriting.")
#     elif x==0:
#         print("Juft son ham toq son ham emas.")
#     elif x % 2 == 0:
#         print("Juft son.")
#     else:
#         print("Toq son")
# x = int(input("x sonini kiriting: "))
# toq_yoki_juft(x)

# def katta_kichik(a,b):
#     """ikki sondan birining katta yoki kichikligini aniqlovchi funksiya"""
#     if a>b:
#         print("a son katta")
#     elif a==b:
#         print("Sonlar teng.")
#     else:
#         print("b son katta")
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))
# katta_kichik(a,b)

# def daraja(x,y):
#     """sonning darajasini aniqlovchi funksiya"""
#     daraja  = x**y
#     print(f"{x} sonning {y} darajasi {daraja} ga teng.")
# x = int(input("x sonini kiriting: "))
# y = int(input("y sonini kiriting: "))
# daraja(x,y)

# def daraja(x,y=2):
#     """sonning darajasini aniqlovchi funksiya"""
#     daraja  = x**y
#     print(f"{x} sonning {y} darajasi {daraja} ga teng.")
# x = int(input("x sonini kiriting: "))
# daraja(x,y=2)

# def qoldiqsiz_bolinish(a):
#     """sonni 2 dan 10 gacha qoldiqsiz bo'linish yokibo'linmasligini aniqlovchi funksiya"""
#     for i in range(2,11):
#         if a%i==0:
#             print(f"{a} {i} ga qoldiqsiz  bo'linadi.")
#         i +=1
# a = int(input("a sonini kiriting: "))
# qoldiqsiz_bolinish(a)

# 20-lesson

# def toliq_ism_yasa(ism,familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# talaba1 = toliq_ism_yasa("Ali","Alijonov")
# talaba2 = toliq_ism_yasa("Vali","Samigjonov")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darsga kechikib keldi.")

# def toliq_ism_yasa(ism,familiya,otasining_ismi = ''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa("Ali","Alijonov","Ismoilovich")
# talaba2 = toliq_ism_yasa("Vali","Samigjonov")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def avto_info(kompaniya, model, rangi, korobka, yili, narxi = None):
#     avto = { 'kompaniya': kompaniya,
#              'model': model,
#              'rang': rangi,
#              'korobka': korobka,
#              'yil': yili,
#              'narx': narxi }
#     return avto
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanik',2020,15000)

# print(avto1)
# print(avto2)
# print(avto1['model'])
# print(avto1['narx'])
# print(avto2['narx'])

# avtolar = [avto1,avto2]
# print(avtolar)
# print(avtolar[0]['model'])

# print("Onlayin bozordagi mavjud avtomashinalar.")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}, Narxi: {narx}")

# def oraliq(min, max,):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(1,10))
# print(oraliq(23,36))
#
# sonlar = oraliq(100,167)
# print(sonlar)

# def oraliq(min, max,qadam):

# def avto_info(kompaniya, model, rangi, korobka, yili, narxi = None):
#     avto = { 'kompaniya': kompaniya,
#              'model': model,
#              'rang': rangi,
#              'korobka': korobka,
#              'yil': yili,
#              'narx': narxi }
#     return avto

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.\n")
# avtolar = []
# while True:
#     print("Quyidagi ma'lumotlarni kiriting.\n",end='')
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narxi = input("Narxi: ")
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
#     javob = input("Yana avto qo'shasizmi? (yes/no)")
#     if javob == 'no':
#         break
# print("Salonimizdagi avtolar:")
# for avto in avtolar:
#     print(f"{avto['rang'].title()} {avto['model'].title()}, {avto['korobka']} korobka. Narxi: {avto['narx']}")
# print(avtolar)

# def data(ism,familiya,t_yil,t_joy,e_manzil,tel_raqam):
#     """foydalanuvchidan ma'lumot olish funksiyasi"""
#     information = {
#             'Ism': ism,
#             'Familiya': familiya,
#             'Tugilgan_yili': t_yil,
#             'Tugilgan_joyi': t_joy,
#             'Email_manzili': e_manzil,
#             'Telefon_raqami': tel_raqam,
#             'Yosh': 2024-t_yil
#     }
#     return information
# tel_raqam = int(input("Telefon raqamingizni kiriting: "))
# e_manzil = input("Elektron manzilingizni kiriting: ")
# data1 = data('Ali','Valiyev',2000,'Qarshi',e_manzili,tel_raqami)
# print(data1)
# print("Mijozlar ro'yxatini shakllantiramiz.")
# mijozlar = []
# while True:
#     print("Quyidagi ma'lumotlarni kiriting. ")
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyangizni kiriting: ")
#     t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#     t_joy = input("Tug'ilgan joyingizni kiriting: ")
#     e_manzil = input("Elektron manzilingizni kiriting: ")
#     tel_raqam = int(input("Telefon raqamingizni kiriting: "))
#     mijozlar.append(data(ism,familiya,t_yil,t_joy,e_manzil,tel_raqam))
#     qoshimcha_malumot = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if qoshimcha_malumot=="yo'q":
#         break
# print("Mijozlar haqida ma'lumotlar")
# print(mijozlar)


# def eng_katta(a,b,c):
#     if a>b and a>c:
#         print(f"{a} soni {b} va {c} sonlardan katta.")
#     elif b>a and b>c:
#         print(f"{b} soni {a} va {b} sonlardan katta.")
#     else:
#         print(f"{c} soni {a} va {b} sonlardan katta.")
# a = float(input("a sonini kiriting: "))
# b = float(input("b sonini kiriting: "))
# c = float(input("c sonini kiriting: "))
# eng_katta(a,b,c)
# import math
# def aylana_radiusi(r):
#     """Aylananing radiusidan uning radiusini,diametrini,
#     peremetrini va yuzasini lug'at ko'rinishida qaytaruvchi
#      funksiya"""
#     aylana_olchamlari = {
#         'radiusi': r,
#         'diametri': 2*r,
#         'uzunligi': 2*math.pi*r,
#         'yuzasi': math.pi*r*r
#     }
#     print(aylana_olchamlari)
# r = float(input("Aylananing radiusini kiriting: "))
# aylana_radiusi(r)


# def tub_sonmi(a,b):
#     tub_sonlar = []
#     for i in range(a,b+1):
#         tub = True
#         if i==1:
#             tub=False
#         elif i==2:
#             tub=True
#         else:
#             for x in range(2,i):
#                 if i%x == 0:
#                     tub=False
#         if tub:
#             tub_sonlar.append(i)
#     return tub_sonlar
# print(tub_sonmi(12,45))


# def fibonacci(n):
#     sonlar = []
#     for i in range(n):
#         if i == 0 or i == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[i-1]+sonlar[i-2])
#     return sonlar
# print(fibonacci(10))

# 21-lesson

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar
# talabalar = ['ali','vali','tohir','zokir']
# baholar = bahola(talabalar [:])
# print(baholar)
# print(talabalar)


# def katta_harf(matnlar):
# 	for i in range(len(matnlar)):
# 		matnlar[i]=matnlar[i].title()
# ismlar = ['ali','vali','tohir','zokir']
# katta_harf(ismlar)
# print(ismlar)

# def katta_harf(matnlar):
# 	matnlar = matnlar[:]
# 	for i in range(len(matnlar)):
# 		matnlar[i]=matnlar[i].title()
# 	return matnlar
# matnlar = ['ali','vali','tohir','zokir']
# yangi_ismlar = katta_harf(matnlar)
# print(matnlar)
# print(yangi_ismlar)

# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar
# talabalar = ['ali','vali','tohir','zokir']
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)

# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))
#
# def summa(x,y,*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return x+y+yigindi
# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))

# def avto_info(kompaniya,model,**malumotlar):
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1 = avto_info("GM","Malibu",rang="qora",yil=2018)
# avto2= avto_info("Kia","K5",rang="qizil",narx=35000,yil=2020,korobka="avtomat ")
# print(avto1)
# print(avto2)

# def kopaytma(*sonlar):
# 	son = 1
# 	for i in sonlar:
# 		son *=i
# 	return son
# print(kopaytma(1,2,3,4,))
# print(kopaytma(1,23,45,12))

# def malumotlar(ism,familiya,**qoshimcha_malumotlar):
# 	qoshimcha_malumotlar['ism']=ism
# 	qoshimcha_malumotlar['familiya']=familiya
# 	return qoshimcha_malumotlar
# talaba1 = malumotlar('Ali','Jalilov',kursi='4-kurs',yonalishi='AX')
# print(talaba1)


















