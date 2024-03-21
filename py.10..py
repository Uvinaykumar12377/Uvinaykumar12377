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




























a=9
b=6
print(a+b)
print(a._add_(b)) under method or mafic method

int()
print(a._sub_(b)) 
len()


















