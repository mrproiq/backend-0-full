# def str_counter(strs):
# 	result = {}
# 	for s in strs:
# 		length = len(s)
# 		if length in result:
# 			result[length].append(s)
# 		else:
# 			result[length] = [s]
# 	return result
# strs = ["shaftoli","olma","nok"]
# print(str_counter(strs))

# contacts = {"Nodir":"+998901111111","Umar":"+998942222222"}
# contacts["Aziz"] = "+998973333333"
# while True:
# 	print("Yangi raqam qo'shish uchun 1 ni bosing.\nRaqamni tahrirlash uchun 2 ni bosing.\nRo'yxatni ko'rish uchun 3 ni bosing.\nChiqish uchun 0 ni bosing.")
# 	amal = input("Tanlangan raqam: ")
# 	if amal=="1":
# 		ism = input("Raqam egasini kiriting: ")
# 		raqam = input("Yangi raqam kiriting: ")
# 		contacts[ism] = raqam
# 	elif amal=="2":
# 		ism = input("O'zgartirmoqchi bo'lgan raqam egasini kiriting: ")
# 		raqam = input("O'zgartirmoqchi bo'lgan raqamni kiriting: ")
# 		contacts[ism]=raqam
# 	elif amal=="3":
# 		print(contacts)
# 	elif amal==0:
# 		break

# list comprehention

# l = [1,2,3,4,5,6,7,8,9]
# toqlar = []
# for i in l:
# 	if i%2==1:
# 		toqlar.append(i)
# print(toqlar)
#
# toqlar = [i for i in l if i%2==1]
# print(toqlar)

# regions = [["Toshkent","Qarshi",],["Farg'ona","Surxondaryo"],["Navoiy","Toshkent"],["Samarqand","Buxoro"]]
# ketuvchilar = [i[1] for i in regions]
# print(ketuvchilar)

# lst = ["Alice",1,2,3,"Alice","Alice"]

# first = lst.index("Alice")
# print(first)
# first = [i for i in range(len(lst)) if lst[i]=="Alice"]
# print(first)

# people = [("John",1_200_000),("Joe",200_000),("Johnson",2_200_000),("Johnatan",800_000),("Jasmin",1_800_000)]
#
# millioners = [name for name,money in people if money>=1_000_000]
# print(millioners)
#
# def find_millioner(people):
# 	return [name for name,money in people.items() if money>=1_000_000]
# people_data1 = {'Alice':1_000_000,'Ali':800_000,'Asila':1_500_000,'Alimardon':900_000}
# people_data2 = {'Begali':1_070_000,'Xusniyor':810_000,'Jahongir':1_600_000,'Humoyun':950_000}
#
# def test():
# 	assert find_millioner(people_data1)==['Alice','Asila']
# 	assert find_millioner(people_data2)==['Begali','Jahongir']
# test()

# l = []
# for x in range(3):
# 	for y in range(3):
# 		l.append((x,y))
# print(l)
# print([(x,y) for x in range(3) for y in range(4)])


# matn = """Lorem ipsum dolor, sit amet consectetur adipisicing elit.
#  Ratione aut ea soluta accusantium! Veniam saepe, corporis unde
#   tempora nisi reprehenderit! Optio id aut totam libero quisquam
#    accusamus sequi porro dolore?"""
# print([[i for i in line.split() if len(i)>=8] for line in matn.split('\n')])

lst1 = ['Ism','Familiya','Yosh']
lst2 = ['Ali','Odilov',20]
zipped = zip(lst1,lst2)
# print(dict(zipped))
# print(list(zipped))

# unziplash
# lst1_new,lst2_new = zip(*zipped)
# print(lst1_new)
# print(lst2_new)

# ustun_nomlari = ['name','salary','job']
# qatorlar = [('Ali',90_000,'teacher'),
#             ('John',80_000,  'artist'),
#             ('Anton',100_000,'barber')]
# db = [dict(zip(ustun_nomlari, row)) for row in qatorlar]
# print(db)

# lambda
# summa = lambda a,b,c: a+b+c
# print(summa(1,2,3))
# print((lambda a,b,c:a+b+c)(1,2,3))

# print((lambda x:x+9)(1))

# map()

# str_num = ["1","12","14","31","71","19","17","154","51","187","100"]
# int_num = map(int,str_num)
# print(list(int_num))

# numbers = [1,2,3,4,5,6]
# print(list(map(lambda a: a**2,numbers)))

# print(list(map(lambda x,y:x-y,[4,7,9],[1,2,3])))

# string = ['ali','vali','soli']
# print(list(map(str.upper,string)))

# reduce()
# n = 5
# from functools import reduce
# print(reduce(lambda x,y:x*y,range(1,n+1)))