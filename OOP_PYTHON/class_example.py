print("!!! 1.EXAMPLE  !!!")
print()
class Student:
    def __init__(self, fullname, age, add):
        self.name = fullname
        self.age = age
        self.add = add
        print("Student (CLASS)")
s1 = Student("Sarthak Joshi", 23, "ngp")
print("neme :",s1.name)
print("age :", s1.age)
print("add :", s1.add)

print("-" * 20)

s2 = Student("Harsh Kohale", 19, "del")
print("neme :", s2.name)
print("age :", s2.age)
print("add :", s2.add)

print()
print()
print("!!! 2.EXAMPLE  !!!")
print()

class Animal:
    def __init__(self, A_name, A_color):
        self.A_name = A_name
        self.A_color = A_color
        print("ANIMAL (CLASS)")

b1 = Animal("Horse","Brown")
print("Animal Name :",b1.A_name)
print("Animal color :",b1.A_color)
print("-" * 20)
b2 = Animal("Dog", "White")
print("Animal Name :",b2.A_name)
print("Animal color :",b2.A_color)
