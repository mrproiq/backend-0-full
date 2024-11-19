# 1-masala
# while True:
#     rang = input("Svetafor qaysi rangda? ")
#     if rang == "qizil" or rang == "sariq" or rang == "yashil":
#         print("Rahmat,to'g'ri keladi.")
#         break
#     else:
#         print("Bu xato rang.")

# 2-masala
# urinishlar = 0
# import random
# tasodifiy_son = random.randint(1,10)
# while True:
#     son = int(input("Sonni kiriting: "))
#     urinishlar +=1
#     print("Urinishlar soni",urinishlar,"marta")
#     if son==tasodifiy_son:
#         print("Tabriklaymiz, siz topdingiz!")
#         break
#     else:
#         print("Noto'g'ri, qayta urinib ko'ring.")

# 3-masala
# friends = []
# while True:
#     name = input("Do'stingizni ismini kiriting: ")
#     if name != "stop":
#         friends.append(name.title())
#     else:
#         break
# print("Do'stlaringiz ro'yxatida",friends,"lar bor.")

# 4-masala
# print("Bizda faqat dollar bor.")
# USD=12_600
# while True:
#     valyuta = input("Valyutani tanlang: ")
#     if valyuta != "exit" :
#         pul = float(input("Pulingizni kiriting: "))
#         sum = pul / USD
#         print(f"Sizning pulingiz {sum} $ ga teng.")
#     else:
#         print("Amalyot bajarildi.")
#         break

# 5-masala
# a = 1
# while a<6:
#     print(str(a)*a)
#     a +=1

# 6-masala


# sum = 0
# while True:
#     son = int(input("Sonni kiriting: "))
#     if son>=0 and son<10:
#         sum = son
#         print("Kiritilgan son raqam va yig'indi o'ziga teng.")
#         False
#     elif son>=10 and son<100:
#         sum = son // 10+son % 10
#         print("Kiritilgan sonning raqamlari yig'indisi",sum,"ga teng.")
#         False
#     elif son>=100 and son<1000:
#         sum = son // 100+(son % 100) // 10+son % 10
#         print("Kiritilgan sonning raqamlari yig'indisi",sum,"ga teng.")
#         False
#     elif son >= 1000 and son < 10000:
#         sum = son // 1000 + ((son % 1000) // 100) + (son % 100)//10+son%10
#         print("Kiritilgan sonning raqamlari yig'indisi", sum, "ga teng.")
#         False
#     else:
#         print("4 xonagacha son kiritishingiz mumkin")
#         False

# 7-masala
# a=1
# sum = 0
# while a<100:
#     if a%2!=0:
#         sum +=a
#     a+=1
# print(sum)

# 8-masala
# import random
# son = random.randint(1,100)
# while True:
#     tahmin = int(input("Tahminigizni kiriting: "))
#     if tahmin<0:
#         print("Juda past")
#     elif tahmin>100:
#         print(("Juda yuqori"))
#     else:
#         print("To'g'ri tahmin qildingiz")
#         break11-dars.py


