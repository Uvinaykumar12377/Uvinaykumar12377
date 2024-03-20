20/03/2024
Day:9
1.) Write a Python script to generate and print a dictionary that
 contains a number (between 1 and n) in the form (x, x*x).
 Sample Dictionary ( n = 5) :
 Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

2.)Find the uncommon words from 2 strings


s1 = "Hello how are you"
s2 = "Hello how is"

s1 = "Hello how are you"
s2 = "Hello how is"

s1 =s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

3.)Wrire a code print the 8th fibanochi number
0,1,1,2,3,5,8


n1 = 1
n2 = 2
ans = 1+2-->3

n1 = 2
n2 = 3
ans = 2+3=5
! find the 8th fibanochi number
num = 8
n1= 0
n2 = 1

for val in range(num):
    ans = n1+n2
    n1 = n2
    n2 = ans
print(ans)

! #constructor
eg:2
unparameterised constructor
class profile:
    def__init__(self):
        print("hello world")

obj = profile()
obj.__init__()

eg:3
parametarised constructor
class profile:
    def_init_(self,id,name,age):
        print(id,name,age)

obj = profile(1,"sid",29)

eg:4
class c1:
    email = "sid@gmail.com"
   
    def m1(self):
        name = "sid"
        place = "cbe"
        print("name,place")
        print(self,email)
       

object = c1()
object.m1()

eg:5
class c1:
    def m1(self):
        name = "sid"
        age = 28
        return name,age
    def display(self):
        print(self.m1())

object = c1()
object.display()

eg:6
to use the variable inside the constructor in another methods
class class1:
    email = "sid@gmail.com" or static variable
    def _init_(self):
        self.name = "sid"      #instance variable
        self.email = "sid@gmail.com"
        # return name,email#error-->cannot use return with constructor

    def display(self):  # instance method
        print(self.name,self.email)

c1 = class()
c1.display()



# !----->inheritance
The process of utilising the methods and attributes of parent class
throught the object of child class it is called as inheritance


# 5 type of inheristance
1.single inheristance
2.multilevel inheristance
3.multiple inheristance
4.hybrid inheristance
5.herarichal inheristance



#single inheristance

it has only one parent class and only one child class
Eg:1
class parent:
    def m1(self):
        print("iam parent class")

class child(parent):
    def m2(self):
        print("iam child class")


obj = child()
obj.m1()

Eg:2
class c1:
    def __init__(self):
        print("iam constructor from parent class")

class  child(c1):
    pass

obj = child()

Eg:3
class parent:
    name = "sidhu"

class child(parent):
    name = "name1"

    def display(self):
        print(self.name)

d = child()
d.display()


#! multilevel inheritance
Eg:1
class voice:
    def sound(self):
        print("All the animals have theit own voice")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(dog):
    def cat_voice(self):
        print("Meow")

class parrot(cat):
    def parrot_voice(self):
        print("speak")

all=parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()


# ? Eg:2
class honda_city:
     def honda_city_engine_specs(self, cc, Hp, torque, fuel_type, num_of_piston):
         print(cc, Hp, torque, fuel_type, num_of_piston)
     
     def honda_city_body_specs (self, color, weight, height, length, vehicle_type):
         print(color, weight, height, length, vehicle_type)
     
class amaze (honda_city):
      def amaze_engine_specs(self, cc, Hp, torque, fuel_type, num_of_piston):
          print(cc, Hp, torque, fuel_type, num_of_piston)
     
      def amaze_body_specs(self, color, weight, height, length, vehicle_type):
          print(color, weight, height, length, vehicle_type) clace civic/amaru)

class Honda(civic):
      pass

honda=Honda()
honda.honda_city_engine_specs(1500,230,2979,"petrol",4)
honda.civic_body_specs("white",2000,5.5,8,"Honda")

#| Multiple Inheritance ff? It has multiple parent and 1 child
class while_pertol:
      def function_w(self):
          print("used to Airplans")
          
class Organic_petrol:
      def function_o(self):
          print("used for Bike, cars")
                    
class premium petrol:
      def function_p(self):
          print("spots cars, bikes")
class petrol (while pertol, Organic_petrol, premium_petrol):
      def defanition(self):
          print("Petrols types")
p=petrol()
p.defanition()
p.function_o()

# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
        
calc=division()
calc.add(3,4)
calc.mul(4,2)

Heirarical inheritance
The one parent class will asct as parent for all the child classes

class catagory:
    def cat_name(self):
        print("weight")

class Tomato(catagory):
    def tomato_specs(self):
        taste="neutral taste"
        self.display(color,taste)

class carrot(catagory):
     def carrot_specs(self):
         color="green"
         taste="sweet"
         self.display(color,taste)


c=carrot()
c.carrot_specs()
c.weigth("30grms")

t=Tomato()
c.tomato_specs()
c.weigth("20grms") 

Hybrid inheritance
The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")

class c2(c1):
    def m2(self):
        print("Class2")

class c3(c2):
    def m3(self):
        print("Class3")

class c4(c2):
    def m4(self):
        print("Class4")

class c5(c3):
    def m5(self):
        print("Class4")

    def m3(self):
        print("iam m3 from c4")
        
class c6(c5,c3):
    def m6(self):
        print("Class4")

obj=c6()
obj.m3()

--->polymorphism
poly - many,morph--->from
A function which has the ability to perform more than 1 functionality
then it is considered to be as plioymorphism

ploymorphism in builtin functions
len())--->which is used to find the length osf list,tuple,dict etc...
index()
max()
min()
count()
pop()
and more...

ploymorphism in operators
print(8+8)
print("k"+'1')
print([1,2,3]+[5,6])

print(6*7)
l1={12,3,4,5,6}
print(*l1)
def f1(*args)

l1=[1,2,3,4]
print(l1*10)

polymorphism in classes
We can achieve polymorphism in 2 ways
1.)Method ovreloading--->it is not possible in python
2.)Method overriding






































































































         








          






























































        







        
































