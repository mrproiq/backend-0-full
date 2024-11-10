# 1.capitalize()
# txt = "men dasturlashni o'rganishga qiziqaman"
# x = txt.capitalize()
# print(x)

# 2.casefold()
# txt = "Dasturlash Juda Qiziq"
# x = txt.casefold()
# print(x)

# 3.center()
# txt = "men markazdaman"
# x = txt.center(21,"#")
# print(x)

# 4.count()
# txt = " Men backend ni o'rganmoqchiman, o'ylaymanki backend ni o'rgansa bo'ladi."
# x = txt.count("backend",4,50)
# print(x)

# 5.endswith()
# txt = "Salom, backend ga xush kelibsiz."
# x = txt.endswith("xush kelibsiz.",17,50)
# print(x)

# 6.expandtabs()
# txt = "H\te\tl\tl\to"
# x = txt.expandtabs(3)
# print(x)

# 7.find()
# txt = "html, css, python, django, sql"
# x = txt.find("t", 3, 15)
# print(x)

# 8.format()
# txt = "Mening ismim {vohid}, men {yigirmaikki} yoshdaman."
# print(txt.format(vohid="Abduvohid", yigirmaikki = 22))
# txt = "Mening ismim {0}, men {1} yoshdaman."
# print(txt.format("Abduvohid", 22))
# txt = "Mening ismim {}, men {} yoshdaman."
# print(txt.format("Abduvohid", 22))
# txt = "Mening ismim {1}, men {0} yoshdaman."
# print(txt.format(22, "Abduvohid"))

# 9.index()
# txt = "Salom, backend ga xush kelibsiz!"
# x = txt.index("end",9, 20)
# print(x)

# 10.isalnum()
# txt = "student1234"
# x = txt.isalnum()
# print(x)
# txt = "student 1234"
# x = txt.isalnum()
# print(x)
# txt = "student!"
# x = txt.isalnum()
# print(x)

# 11.isalpha
# txt = "Onlinedasturlash"
# x = txt.isalpha()
# print(x)
# txt = "Online dasturlash 1"
# x = txt.isalpha()
# print(x)

# 12.isascii()
# txt = "70 A 700 AA"
# x = txt.isascii()
# print(x)
# txt = "70 A 700 AA машина номери"
# x = txt.isascii()
# print(x)

# 13.isdecimal()
# txt = "12345678"
# x = txt.isdecimal()
# print(x)
# txt = "qwerty"
# x = txt.isdecimal()
# print(x)
# txt = "\u0030"
# x = txt.isdecimal()
# print(x)
# txt = "\u0047"
# x = txt.isdecimal()
# print(x)

# 14.isdigit()
# g = "9.81"
# print(g.isdigit())
# x = "30"
# print(x.isdigit())

# 15.isidentifier()
# txt = "maktab"
# x = txt.isidentifier()
# print(x)
# txt = "maktab6"
# x = txt.isidentifier()
# print(x)
# txt = "maktab-"
# x = txt.isidentifier()
# print(x)
# txt = "1-maktab"
# x = txt.isidentifier()
# print(x)
# txt = "1 maktab"
# x = txt.isidentifier()
# print(x)

# 16.islower()
# txt = "salom sinfdoshlarim"
# x = txt.islower()
# print(x)
# txt = "Salom kursdoshlarim"
# x = txt.islower()
# print(x)

# 17.isnumeric()
# txt = "2345"
# x = txt.isnumeric()
# print(x)
# txt = "2345-1234"
# x = txt.isnumeric()
# print(x)
# txt = "1.0"
# x = txt.isnumeric()
# print(x)
# txt = "-2345"
# x = txt.isnumeric()
# print(x)
# txt = "+2345"
# x = txt.isnumeric()
# print(x)
# txt = "5km2"
# x = txt.isnumeric()
# print(x)

# 18.isprintable()
# txt = "Salom & hayr!"
# x = txt.isprintable()
# print(x)
# txt = 'Salom! \ndo\'stim'
# x = txt.isprintable()
# print(x)

# 19.isspace()
# txt = "   "
# x = txt.isspace()
# print(x)
# txt = "  I  "
# x = txt.isspace()
# print(x)
# txt = ""
# x = txt.isspace()
# print(x)

# 20.istitle()
# txt = "I  Love Pizza"
# x = txt.istitle()
# print((x))
# txt = "I  LOVE PIZZA"
# x = txt.istitle()
# print((x))
# txt = "I  love pizza"
# x = txt.istitle()
# print((x))
# txt = "2 Bo'lak"
# x = txt.istitle()
# print((x))
# txt = "Bu Bir 456"
# x = txt.istitle()
# print((x))

# 21.isupper()
# txt = " I LOVE PIZZA!"
# x = txt.isupper()
# print(x)
# txt = " I love pizza!"
# x = txt.isupper()
# print(x)
# txt = "100"
# x = txt.isupper()
# print(x)

# 22.join()
# myTuple = ("Ali","Vali","Soli: aka-ukalar")
# x = "-".join(myTuple)
# print(x)
# myDic = {"Bir", "Ikki", "Uch"}
# x = "-"
# y = x.join(myDic)
# print(y)

# 23.ljust()
# txt = "Kevi"
# x = txt.ljust(15)
# print(x, "- bu men yoqtirgan meva.")
# txt = "Kevi"
# x = txt.ljust(15,"*")
# print(x, "- bu men yoqtirgan meva.")

# 24.lower()
# txt = "Salom Gruppadagilar, YAXSHIMISIZLAR"
# x = txt.lower()
# print(x)

# 25.lstrip()
# txt = "    olma"
# x = txt.lstrip()
# print("Hamma", x, "sveji.")

# 26.rstrip()
# txt = "olma    "
# x = txt.rstrip()
# print("Hamma", x, "sveji.")

# 27.strip()
# txt = "    olma    "
# x = txt.strip()
# print("Hamma", x, "sveji.")

#28.upper()
# txt = "Men dasturlashni o'rganishga qiziqaman."
# x = txt.upper()
# print(x)

# 29.title()
# txt = "olti oyda junior dasturchi bo'laman"
# x = txt.title()
# print(x)

#30. maketrans()
# txt = "Salom Halil"
# x = str.maketrans("H","J")
# print(txt.translate(x))
# txt =  "God night Sam!"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# mytable = str.maketrans(x,y,z)
# print(txt.translate(mytable))

#31.zfill()
# txt = "10"
# x = txt.zfill(4)
# print(x)
# txt = "salom"
# x = txt.zfill(10)
# print(x)
# txt = "Dasturlashga xush kelibsiz!"
# x = txt.zfill(35)
# print(x)

#32.swapcase()
# txt = "Mening Ismim ABDUVOHID"
# x = txt.swapcase()
# print(x)
# txt = "salom"
# x = txt.swapcase()
# print(x)

#33.startswith()
# txt = "Salom, pythonga xush kelibsiz!"
# x = txt.startswith("yth",8,24)
# print(x)

#34.replace()
# txt = "Men shaxmatni yoqtiraman."
# x = txt.replace("shaxmat","futbol")
# print(x)
# txt = "bir bir ikki ikki uch uch bir"
# x = txt.replace("bir", "1")
# print(x)
# txt = "uch bir bir ikki ikki uch uch bir"
# x = txt.replace("uch", "1",2)
# print(x)

#35.partitation()
# txt = "Men 2 ta olma yedim"
# x = txt.partition("olma")
# print(x)
# txt = "Men 2 ta olma yedim"
# x = txt.partition("e")
# print(x)
