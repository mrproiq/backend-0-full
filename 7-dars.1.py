from copy import deepcopy

# a = [1,2,3]

# a = [1,2,3,[4,5,6]]
# b = a
# b = deepcopy(a)
# b[3].append(7)
# print(a)
# print(b)

# d = {"ism":"Ali","yosh":23}
# d2 = dict(ism="Ali",yosh=23)
# d3 = dict([("ism","Ali"),("yosh",23)])
# d["ball"]=[5,4]
# print(d["ball"])
# print(d2)
# print(d3)

# # Dictionary with duplicate keys
# duplicated_keys = {"key1": "value1", "key1": "value2", "key1": "value3"}
#
# # Access key1
# print(duplicated_keys["key1"])

# harry_potter_dict = {
#     "Harry Potter": "Gryffindor",
#     "Ron Weasley": "Gryffindor",
#     "Hermione Granger": "Gryffindor"
# }
#
# add_characters_1 = {
#     "Albus Dumbledore": "Gryffindor",
#     "Luna Lovegood": "Ravenclaw"
# }
#
# harry_potter_dict.update(add_characters_1)
#
# add_characters_2 = [
#     ["Draco Malfoy", "Slytherin"],
#     ["Cedric Diggory", "Hufflepuff"]
# ]
# harry_potter_dict.update(add_characters_2)
#
# add_characters_3 = [
#     ("Rubeus Hagrid", "Gryffindor"),
#     ("Minerva McGonagall", "Gryffindor")
# ]
# harry_potter_dict.update(add_characters_3)
# from collections import Counter
#
# # Frequency of values
# counter = Counter(harry_potter_dict.values())
# print(counter)


#
# arr = [1,1,1,1,2,2,2,2,2,2,2,2,2,33]
# counter = Counter(arr)
# print(counter)


#
# for key, value in harry_potter_dict.items():
#     print((key, value))

# print(list(harry_potter_dict.values()))

# print("Dictionary without Voldemort.")
# print(harry_potter_dict)
# print()
#
# print("Return the default value of Voldemort.")
# print(harry_potter_dict.setdefault("Voldemort", "Slytherin"))
# print()
#
# print("Voldemort is now in the dictionary!")
# print(harry_potter_dict)


# new = harry_potter_dict.get("RonWeasley",None)
# print(new)

# print(harry_potter_dict)
#
# del harry_potter_dict["Minerva McGonagall"]
#
# print(harry_potter_dict)
#
# del harry_potter_dict["Voldemort"]

# Insert Voldemort
# harry_potter_dict["Voldemort"] = "Slytherin"
#
# print("Dictionary with Voldemort:")
# print(harry_potter_dict)
# print()
#
# # Remove the last inserted item (Voldemort)
# harry_potter_dict.popitem()
#
# print("Dictionary after popping the last inserted item (Voldemort):")
# print(harry_potter_dict)


# harry_potter_dict["Voldemort"] = "Slytherin"
#
# print("Dictionary with Voldemort:")
# print(harry_potter_dict)
# print()
#
# # Remove the last inserted item (Voldemort)
# print("Remove Voldemort and return his house:")
# print(harry_potter_dict.pop("Voldemort"))
# print()
#
# print("Dictionary after popping the last inserted item (Voldemort):")
# print(harry_potter_dict)

# thisset = {"apple", "banana", "cherry", "apple"}
#
# print(thisset)
#
# thisset = {"apple", "banana", "cherry", True, 1, 2}
#
# print(thisset)
#
# thisset = {"apple", "banana", "cherry", False, True, 0}
#
# print(thisset)
#
# thisset = {"apple", "banana", "cherry"}
#
# print("banana" in thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
#
# thisset.update(tropical)
#
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
#
# thisset.discard("banana")
#
# print(thisset)
# thisset = {"apple", "banana", "cherry"}
#
# thisset.clear()
#
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
#
# x = thisset.pop()
#
# print(x)
#
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
#
# thisset.clear()
#
# print(thisset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
#
# set3 = set1.union(set2)
# print(set3)
#
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
#
# set3 = set1 | set2
# print(set3)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
#
# myset = set1.union(set2, set3, set4)
# print(myset)

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
#
# myset = set1 | set2 | set3 |set4
# print(myset)
#
# x = {"a", "b", "c"}
# y = (1, 2, 3)
#
# z = x.union(y)
# print

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
#
# set1.update(set2)
# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1.intersection(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1 & set2
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set1.intersection_update(set2)
#
# print(set1)


# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
#
# set3 = set1.intersection(set2)
#
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1.difference(set2)
#
# print(set3)
#
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1 - set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set1.difference_update(set2)
#
# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1.symmetric_difference(set2)
#
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1 ^ set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set1.symmetric_difference_update(set2)
#
# print(set1)


