#Funksiyalar

# def print_5_message():
#
#     for _ in range(5):
#         print("Hello world!")
#
# print_5_message()
#
# print("----------")
#
# print_5_message()
# def sanoq():
#     for i in range(1,40):
#         if i % 2 == 0 and i % 3 == 0:
#             print(i)
# sanoq()

# def bir():
#     pass
# def ikki():
#     return 2
# def uch():
#     return 3
# def tort():
#     return 4
# son = bir()
# print(son)

# def add(a,b):
#     return a*b
# yigindi = add(a=3,b=5)
# print(yigindi)


# first_name = input("Ismingizni kiriting: ")
# last_name = input("Familiyaingizni kiriting: ")
# age = int(input("Yoshingizni kiriting: "))
# def user_data(first_name,last_name,age):
#     print(f"Ism: {first_name}")
#     print(f"Familiya: {last_name}")
#     print(f"Yosh: {age}")
# user_data(first_name,last_name,age)
# sales = {"Yanvar:12000",
#          "Mart:6000",
#          "Aprel:15000",
#          "Sentyabr:9000",
#          "dekabr:10000"}
# def big_sales(sales):
#     return max(sales.i)
#
#
# big_sales(sales)

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# salom_ber()

# def salom_ber(ism):
#     '''Foydalanuvchi ismini qabul qilib,
#     unga salom beruvchi fumksiya'''
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")

# salom_ber("hasan")
# print((salom_ber.__doc__))

# def full_name(name,surname):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {name.title()}\n"
#           f"Foydalanuvchi familiyasi: {surname.title()}")
# full_name("Ali","odilov")
# full_name("hojakbarov","vali") # argumentni notogri ketma-ketlikda berdik

# def yosh_hisobla(ism,tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2024-tugilgan_yil} yoshda.")
# yosh_hisobla("soli",2004)
# yosh_hisobla(2003,'zokir') #argumentlarni almawtirib yozganimiz uchun xatolik chiqardi.

# def yosh_hisobla(ism,tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2024-tugilgan_yil} yoshda.")
# yosh_hisobla("soli",2004)
# yosh_hisobla(tugilgan_yil=2003,ism='zokir') #Agar parametr nomi bilan qiymatlarni bersak almashtirib yozganimizdagi xatolikni oldini olgan bo'lamiz.

# def full_name(name,surname):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {name.title()}\n"
#           f"Foydalanuvchi familiyasi: {surname.title()}")
# full_name("Ali","odilov")
# full_name(surname='yaxshiyev',name='salim')

# def yosh_hisobla(tugilgan_yil, joriy_yil=2024): #joriy_yil uchun st.qiymat berildi.
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi."""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz.")
# yosh_hisobla(2000,2024)
# yosh_hisobla(2000) #bergan standart qiymatni qabul qildi.

# from datetime import datetime
# def yosh_hisobla(tugilgan_yil, joriy_yil=datetime.now().year): #joriy_yil uchun st.qiymat berildi.
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi."""
#     # if joriy_yil is None: # joriy_yil = None qiymatda ishlaydi
#     #     joriy_yil = datetime.now().year
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz.")
# tyil = int(input("Tug'ilgan yilingizni kiriting."))
# yosh_hisobla(tyil)

# def toliq_ism_yasa(ism,familya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism.title()} {familya.title() }"
#     return toliq_ism
# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def toliq_ism_yasa(ism,familya,otasining_ismi=''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familya}"
#     else:
#         toliq_ism = f"{ism} {familya}"
#     return toliq_ism.title()
# talaba1 = toliq_ism_yasa('olim','duranov',)
# talaba2 = toliq_ism_yasa('duran','olimov','aliyevich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def oraliq(min, max,):
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(1,10))
# print(oraliq(23,36))

# def avto_info(kompaniya, model, rangi, korobka, yili, narxi = None):
#     avto = { 'kompaniya': kompaniya,
#              'model': model,
#              'rang': rangi,
#              'korobka': korobka,
#              'yil': yili,
#              'narx': narxi }
#     return avto
#
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


son = input("Ixtiyoriy butun son kiriting: ")
if son.isalpha():
    print("Butun son kiriting.")
if son<0:
    print(int(son))
elif son==0:
    print(f"{son} musbat ham manfiy ham emas")
else:
    print(int(son)+1)



