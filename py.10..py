21/03/2024
Day:10
#!Method of over_riding
ploymorphism in classes using Inheritance
Eg:1
class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i=IOB()
i.ratio()

s=SBI()
s.ratio()

Eg:2
class USA:
      def language(self):
          print("English")

      def capital(self):
          print("Washington DC")


class India(USA):
      def language(self):
          print("None")

      def capital(self):
          print("New delhi")

I=Indian()
I.language()
I.capital()

Eg:3
polymorphism using objects

c1,c2--->c1=print(c1),print(c2)
f1,f2

Eg:4
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
            print("class 2")

obj1=c2()
obj1.f1()

def display(a):
    a.f1()
display(obj1)
display(obj2)

changing the functionality of builtin functions
class shopping:
    def _int_(self,l1):
        self.items=l1
        
    def _len_(self):
        length=len( self.items)
        return length
s=shopping([1,2,3,4,5])
print(len(S))

#!-->Method overloding
Eg:1
class suming:
    def add(self a,b):
        print(a+b)

    def add(self a,b,c):
        print(a+b+c)

s= suming()
s.add(4,3) --->error
s.add(4,5,1)

Eg:2
class summing:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
           print(a+b+c)
        elif a!=None and b!=None:
             print(a+b)
        else:
            print(a)

obj=summing()
obj.add(2)
obj.add(3,4)
obj.ad(1,2,3)

--->Abstraction
The process of hiding the implimentatiom details is abstraction

Eg:1

from abc import ABC,abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print("All shapes have sides except circle")

class triangle:
    def triangle_sides(self):
        print("3 sides")
        
    def name(self):
        print("Iam triangle")
            
    def sides(self):
        pass

class square:
    def square(self):
        print("4 sides")

    def sides(self):
        pass

tr=triangle()
tr.triangle_sides()
tr.name()

#! Rules to define abstract class1
1.)Abstract class cannot be instantiated
2.)from abc import ABC,abstractmethod
3.)subclass the normal class with ABC
4.)convert the normal method inside the abstract class to be abstract method
5.)All the child classes have to be subclassed with abstract class
6.)The abstract method should be present inthe child classes

Eg:2
super()--->used to access the parent class method from child class method
from abc import ABC,abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self):
        pass

class2=c2()
class2.m2()

Eg:3
from abc import ABC,abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd="sidd1994$"
        return pswd

class login(password):
    def validate(self,name,passwrd):
        if super().pwd()==passwrd:
           print("welcome",name,'!!')
           print("Login successfull")
        else:
            print("please check the password")
            
    def pwd(self):
        pass
    
Login=login()
name=input("Enter the name:")
pwd=input("Enter the password:")
Login.validate(name,pwd)

#! Encapsulation
Eg:1
class car:
    _name="BMW" private variable

c1=car()
print(c1.name)
c1.name="Audi"
print(c1.name)

Eg:2
accessing private date outside the class
class c1:
    _phone='9347161677'

    def display(self):
        print(self._phone)

c=c1()
c.display()

Eg:3
declare private method
class class1:
    def _m1(self): private method
        print("Iam private method")

    def_int_(self):
        self._m1()
c=class1()
c._m1()  error

nested class
 class class1:
     class class2:
         name="sidhu"

     def display(self):
         print(self.name)
 obj1=class2()

obj=class1()
obj.obj1.display()

d1={"shirt":1000,"pant":1500,"shoes":900,"handkey":30}
for val in d1:
    if d1[val]==min(d1.values()):
        print(val)
    
for val in d1:
    if d1[val]==max(d1.values()):
        print(val)
         
for val in d1:
    if val.startswith('s') or val.startswith('s'):
        print(val)
    


































































a=9
b=6
print(a+b)
print(a._add_(b)) under method or mafic method

int()
print(a._sub_(b)) 
len()


















