19/03/2024
Day:8
Eg:3
def profile(name,age,place):
    txt = "My name is{}. Iam{} years old.Iam from{}."
    print(txt.format(name,age,place))
profile("sid",29,"cbe")

Eg:4
Function with return statement
#!return
1.) A variable declared inside the function can be accessed outside the 1665  using return 1666
2.) return does not prrint anything 1667
3.) we cannot write any code below return statement

def f1():
    z=8
f1()
print(z) error -->cannot use outside the function

def f1(a,b):
    c=a*b
    return c
print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)

def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

Problem:1

def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
       print(n,"Palindrome")
    else:
        print("Not palindrome")
a = int(input("Enter the value: "))
palindrome(a)

Based on the declaration of parameter and args
functions are divided into 5 catagories

positional args
keyword args
default args
variable length args
keyword variable length args

#! positional args
The position of parameter have to be same as position as arguments
Eg:1
def profile(name,phone,mark):
    txt = "My name is {}.My phone number is {}.I got marks {}."
    print(txt.format(name,phone,mark))

profile(9347161677,"sidhu",97) unexpected output

keyword args
To overcome the disadvantage of position args, we use keyword args
It is the process of initialising the paremeter with the args while calling the
function
def profile(name, phone, mark):
    txt "My name is {). My phone number is {}. I got {} marks."
    print(txt.format(name, phone, mark))

profile(name="sid", mark=96, phone=1234567890)

todo---> Exception of keyword args function
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {}marks."
    print(txt.format(name, phone, mark))

profile(name="sid", 123445567, mark=98) error--->positional arsg follow keywords
profile(123445567, name="sid", mark=98) error--->name has multiple values
profile("sid",mark=98,phone=123445567)

Default args
The method of assigning the argument to the parameter while declaring function the 
Eg:1
def profile(name, phone, place="kadapa"):
    txt = "My name is {}. My phone number is {}. I am from{}."
    print(txt.format(name, phone, place))
    
profile("sid",8767676767)

Eg:2
def profile(name, phone, place="kadapa"):
    if place=="kadapa" or place=="KADAPA" or place=="kadapa":
       txt = "My name is {}. My phone number is {}. I am from{}."
       print(txt.format(name, phone, place))
       else:
           print("You are not eligible to signup")
profile("sid",8767676767)

Exception
def profile(name, phone, place="kadapa"): error--->coz default args should not follow positional param
    if place=="kadapa" or place=="KADAPA" or place=="kadapa":
       txt = "My name is {}. My phone number is {}. I am from{}."
       print(txt.format(name, phone, place))
       else:
           print("You are not eligible to signup")
profile("sid",8767676767)

variable length params
Eg:1
To pass more than 1arg to a parameter means we use variable length args
To convert normal parameter to variable length param,add * to their prefix of param

name = "sid",'name2','name3'
def profile(*name):
    print("My name is ",val)
profile("sid",'name2','name3')

Eg:2
def profile(*name,age):
    print("My name is ",val,"My age is",)
profile("sid",'name2','name3',25) error--->age has no args

def profile(age,*name):
    for val in name:
        print("My name is" ,val,"my age is") ,age
profile("sid",'name2','name3',28)

keyword variable length args
kwargs-->which is used to provide the args in the form os key value pair.
Eg:1
def price(**price_list):
    print(price_list)

price(sirt=1000,iphone=80000)

d1={"a":100,"b":200,"c":300}
d1=dict(a=100,b=200,c=300)
print(d1)

n=5
{1:1,2:4,3:9,4:16,5:25}

n=int(input("Enter the number:"))
d1={}
for val in range(1,n+1):
    d1[val]=val**2
    print(d1)
    
def dict1(n):
    d1={}
for val in range(1,n+1):
    d1[val]=val**2
    print(d1)
dict1(5)

--->object oriented programming
The paradigms of objects oriented programming are

class
objects
inheritance
polymorphism
abstraction
encapsulation

#! class is a blue print of an object
l[1,2,3,4,5,6]

Eg:1
class c1:
    name1="sidhu"
    print(name1)

Eg:2
class person:
    name = "sidhu"

c=person() c as object
The process of creation of an object is called as instantiation
print(c.name)

Eg:3
create of a method
when the function is created with a class is called as method

Method without parameter
class person:
    def display(person):It is a method
        print("Hello welcome to class")

p=person()
p.display()

Eg:4
Method with parameter
class person:
    def display(person,name,age):
        print(name,age)

p=person()
p.display("sidhu",28)


Eg:5
class person1:
    fname="sidhu" attribute or static variable
    fname="T"
    
    def first_name(self):
        print(self.fname)
        
    def full_name(self):
        print(self.fname+" "+self.1name)

p = person1()
p.first_name()
p.full_name()

Eg:6
constructors-->_init_()
This is a special method which has the ability to execute itself without
calling it manually thorugh the process of instantiation

class profile:
    def_init_(self): constructor method
       print("hey")

p=profile() execution of constructor through this process 















































        












    














































































































