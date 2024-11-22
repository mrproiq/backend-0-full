# 1-masala
# def user_data(first_name,last_name,age):
#     """Ism, familiya va yoshni chiqaruvchi funksiya"""
#     print(f''' Ism: {first_name} \n Familiya: {last_name} \n Yosh: {age}''')
# user_data('Ali','Olimov',23)

# 2-masala
# def find_max(a,b,c):
#     max_value = max(a,b,c)
#     if a==b==c:
#         print(f"Eng katta son - A va B va C = {max_value}")
#     elif a==b and a== max_value:
#         print(f"Eng katta son - A va B = {max_value}")
#     elif a==c and a== max_value:
#         print(f"Eng katta son - A va C = {max_value}")
#     elif b==c and b==max_value:
#         print(f"Eng katta son - B va C = {max_value}")
#     elif a == max_value:
#         print(f"Eng katta son - A = {max_value}")
#     elif b == max_value:
#         print(f"Eng katta son -  B= {max_value}")
#     else:
#         print(f"Eng katta son - C = {max_value}")
# a = int(input("A-sonni kiriting: "))
# b = int(input("B-sonni kiriting: "))
# c = int(input("C-sonni kiriting: "))
# find_max(a,b,c)

# 3-masala
# def find_letter_count(word,letter):
#     n = word.lower().count(letter.lower())
#     print(f'"{soz}" so\'zida "{harf}" harfidan {n} ta bor.')
# soz = input("So'zni kiriting: ")
# harf = input("Harfni kiriting: ")
# find_letter_count(soz,harf)

# 4-masala
# def list_sum(myList):
    # total = sum(myList) # sum funksiyasi - pythonning sum funksiyasi
#     # ro'yxatdagi barcha elementlarni avtomatik tarzda qo'shib beradi.
#     print(f"Listning elementlari yig'indisi = {total}")
# list_sum([2,4,5,6,8,9,-2])
# 2-usul
# def list_sum(myList):
#     S=0
#     for i in myList:
#         S += i
#     return S
# print(list_sum({12,45,-98,56,23}))
# 5-masala
# def daraja(a,b):
#     pow = a**b
#     print(f"{a} ning {b}-darajasi {pow} ga teng.")
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))
# daraja(a,b)

# 6-masala
# def daraja4(a,b,c,d):
#     print(f"{a} ni {b}-darajasi {a**b} ga,{a} ni {c}-darajasi {a**c} ga,{a} ni {d}-darajasi {a**d} ga teng.")
# a = int(input("a sonini kiriting: "))
# b = int(input("b sonini kiriting: "))
# c = int(input("c sonini kiriting: "))
# # d = int(input("d sonini kiriting: "))
# daraja4(a,b,c,d)

# 7-masala
# 1-usul
# def digit_count_and_sum(word):
#     sanoq = 0
#     yigindi = 0
#     for i in word:
#         if i.isdigit():
#             sanoq += 1
#             yigindi += int(i)
#     return sanoq,yigindi
# print(digit_count_and_sum("12wdfe45ghy7"))

# def digit_count_and_sum(word):
#     raqamlar = []
#     for i in word:
#         if i.isdigit():
#             raqamlar.append(int(i))
#             soni = len(raqamlar)
#             yigindi = sum(raqamlar)
#     print(f"Raqamlar soni: {soni}, Yigindisi {yigindi}")
# digit_count_and_sum("qwer23ty4y5jkk8nbv0")

# 2-usul
# def digit_count_and_sum(word):
#     raqamlar = [int(i) for i in word if i.isdigit()]
#     soni = len(raqamlar)
#     yigindi = sum(raqamlar)
#     print(f"Soni {soni}, yig'indisi {yigindi}")
# digit_count_and_sum('qwer34ty56jki7890kjg')

# 8-masala
# def add_right(a,b):
#     natija = int(f"{a}{b}")
#     print(natija)
# add_right(12,45)

# 9-masala
# def add_left(a,b):
#     natija = int(f"{b}{a}")
#     return natija
# print(add_left(12,45))

# 10-masala
# 1-usul
# def work_with_list(a):
#     min_qiymat = min(a)
#     yangi_royxat = []
#     for i in a:
#         yangi_royxat.append(i*min_qiymat)
#     return yangi_royxat
# print(work_with_list([2,3,4,6]))

# 2-usul
# def work_with_list(a):
#     min_value = min(a)
#     yangi_royxat = [min_value*i for i in a]
#     print(yangi_royxat)
# work_with_list([12,3,4,5,6,7,2])

# 11-masala
# def big_sales(sales):
#     return max(sales, key=sales.get)
#
# sales = {
#         "yanvar":12000,
#         "mart":6000,
#         "aprel":15000,
#         "sentabr":9000,
#         "dekabr":10000
# }
# print(big_sales(sales))

# 12-masala
# 1-usul
# def min_max(numbers,max_num,min_num):
#     eng_kichik = min(numbers)
#     eng_katta = max(numbers)
#     if max_num == eng_katta:
#         print("Maxsimumni to'g'ri topdingiz!")
#     else:
#         print("Maximum xato")
#     if min_num == eng_kichik:
#         print("Minimumni to'g'ri topdingiz!")
#     else:
#         print("Minimum xato")
# min_max([2,3,4,56,78,98],98,98)

# 2-usul
# def min_max(numbers,max_num,min_num):
#     is_max = max_num == max(numbers)
#     is_min = min_num == min(numbers)
#     return is_max,is_min
# print(min_max([2,4,6,7,8],8,2))

# 13-masala
# 1-usul
# def expensive_product(products):
#     max_price = 0
#     max_price_name = {}
#     for product in products:
#         if product["price"] > max_price:
#             max_price = product["price"]
#             max_price_name = product["name"]
#     return max_price_name
# products = [
#       {"name": "Iphone X", "price": 600},
#       {"name": "Iphone 12", "price": 1500},
#       {"name": "Samsung Note 9", "price": 800},
#       {"name": "Samsung S10", "price": 1100}
# ]
# print(expensive_product(products))


# 2-usul
# def expensiveProduct(products):
#     eng_qimmat = max(products, key=lambda product: product["price"])
#     print(eng_qimmat["name"])
# products = [
#     {"name": "Iphone X", "price": 600},
#     {"name": "Iphone 12", "price": 1500},
#     {"name": "Samsung Note 9", "price": 800},
#     {"name": "Samsung S10", "price": 1100}
# ]
# expensiveProduct(products)
