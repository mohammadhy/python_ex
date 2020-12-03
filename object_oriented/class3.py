from abc import ABC, abstractmethod

class veichle(ABC):   
    def __init__(self, model, typee):
        self.model = model
        self.typee = typee
        super().__init__()
    
    @abstractmethod    
    def typee(self):
        return self.model
        return self.typee
    

class benz(veichle):
     def typee(self):
        return f'{self.model} {self.typee}' 

     def engine(): 
        pass

class volvo(veichle):

     def typee(self):
        return f'{self.model} {self.typee}' 

c1 =benz('G', 'suv')     
print(c1.typee)   

c2 = volvo('xc', 'sedan')

print(c2.typee)  
#--------------------------------------------------------------
class D :
    def __init__(self, x):
        self.x = x
    
    @classmethod
    def h(cls, t):
        print(t + 2)   
        return cls(t)
        
ob = D(0)
ob.h(2)
D.h(2)
#--------------------------------------------------------------
from datetime import date
class C:
    def __init__(self,name, age):
        self.name = name
        self.age = age
  
    @classmethod        
    def f(cls,name, year):
        y = date.today().year - year
        return cls(name, y)
     
    @staticmethod
    def s(age):
        return age < 50
   
ob = C.f('farshid',1972)

print(ob.age)       

print(ob.name)               

print(ob.s(48)) 
#------------------------------------------------------------------
class  Numbers:
    a = 3
    
    def __init__(self,x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y
    
    @classmethod
    def mul(cls, b):
        return cls.a * b
    
    @staticmethod
    def sub(b, c):
        return b - c
    
    @property
    def value(self):
       return(self.x, self.y)
       
    @value.setter
    def value(self, t):
        self.x, self.y = t
        
    @value.deleter
    def value(self):
        del self.x
        del self.y
        
    
ob = Numbers(2, 3)    
print(ob.add())      # 5
print(ob.mul(4))     # 12
print(ob.sub(2,3))   # -1

print(ob.value)     # (2, 3)
ob.value = (6, 8)
print(ob.value)     # (6, 8)
print(ob.x)
print(ob.y)
print(ob.mul(5))

print('--------------------------------------------------------------------')