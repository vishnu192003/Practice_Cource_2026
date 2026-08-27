class first:  #iterative statement(transfer condition ) break,pass ,continue 
    #constructor --> invisible default function constructor
    #init method 
    name='vishnu'
    age= 23
    add= 'nagpur'

    print("name of student is",name)
    print("name of student is",age)
    print("name of student is",add)
obharsh = first()
#print(obharsh)


#class
#cl is the collection of object it is not a real world entity 
#it just a templet or blueprint or prototype.

# object
# object is an isinstance of a class  
# it occupied a memory

# function ---> method


# example of class by int
class first:
    
        name = "srushti"
        age = 23
        add = "Nagpur"
        print("name of student is :",name)
        print("age of student is :", age)

obvishun = first()


# 

# __init__ -- constructor, automatically called when object is created
# self -- reference variable that points to the current object instance

# 1
class Second:
    def __init__(self, name, age, city):
        self.fullname = name
        self.sage = age
        self.scity = city
        
        print("name of student is", self.fullname)
        print("age of student is", self.sage)
        print("city of student is", self.scity)

# Example instantiation:
vi = Second("vishnu", 23, "Nagpur")
vi =Second('sarthak',23,'pune')
vi =Second("harsh",19,"hyd")





# 2
class Second:
    def __init__(self, name, age, city):
        self.fullname = name
        self.sage = age
        self.scity = city
        
        print("name of student is", name)
        print("age of student is", age)
        print("city of student is", city)

# Example instantiation:
vi = Second("vishnu", 23, "Nagpur")
vi =Second('sarthak',23,'pune')
vi =Second("harsh",19,"hyd")



# 2 Classes create karne ka example:

# Class 1: Student
class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def display_details(self):
        print("----- Student Details -----")
        print("Name   :", self.name)
        print("Roll No:", self.roll_no)
        print("Course :", self.course)

# Objects create karna:
# 1. Student class ke objects
student1 = Student("Vishnu", 101, "Python Full Stack")
student2 = Student("Sarthak", 102, "Data Science")

print()

# Class 2: Teacher
class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self.subject = subject
        self.salary = salary

    def display_details(self):
        print("----- Teacher Details -----")
        print("Name   :", self.name)
        print("Subject:", self.subject)
        print("Salary :", self.salary)




# 2. Teacher class ke objects
teacher1 = Teacher("Dr. Sharma", "Computer Science", 50000)

# Methods call karna:
student1.display_details()
student2.display_details()
teacher1.display_details()
