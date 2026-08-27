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



# 2  class create karna hai ()