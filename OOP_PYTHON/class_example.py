# print("!!! 1.EXAMPLE  !!!")
# print()
# class Student:
#     def __init__(self, fullname, age, add):
#         self.name = fullname
#         self.age = age
#         self.add = add
#         print("Student (CLASS)")

# s1 = Student("Sarthak Joshi", 23, "ngp")
# print("neme :",s1.name)
# print("age :", s1.age)
# print("add :", s1.add)

# print("-" * 20)

# s2 = Student("Harsh Kohale", 19, "del")
# print("neme :", s2.name)
# print("age :", s2.age)
# print("add :", s2.add)

# print()
# print("!!! 2 EXAMPLE !!! ")

# class Second:
#     def __init__(self, name, age, city):
#         self.fullname = name
#         self.sage = age
#         self.scity = city

#         print("name of student is", name)
#         print("age of student is", age)
#         print("city of student is", city)


# vi = Second("vishnu", 23, "Nagpur")
# vi = Second("sarthak", 23, "pune")
# vi = Second("harsh", 19, "hyd")


# Fruits Class Example
class Fruit:
    def __init__(self, name, color, price):
        self.fname = name
        self.fcolor = color
        self.fprice = price

        print("-------")

        print("Name of fruit is  :", name)
        print("Color of fruit is :", color)
        print("Price of fruit is :", price)


f1 = Fruit("Apple", "Red", 120)
f1 = Fruit("Banana", "Yellow", 40)
f1 = Fruit("Mango", "Yellow", 150)
