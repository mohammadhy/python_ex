class D:
	def __init__(self, x, y):
		self._x = x 	#protect(can access on class that inherit by class D)
		self.__y = y 	#private(just access on class D but you want to access that 
									#object_of_class(d)._main_class(D)__y))
	def multi(self, x):
		return self.__y * x

	def func(self, a, b):
		if a < b:
			return self.multi(a)
		else:
			return self.multi(b)

class B(D):
	@property
	def h(self):
		return self._x
		return self.__y

class C(B):
	def __init__(self, x, y):
		super().__init__(x ,y)
	def h(self):
		return self._x * 2
		return self.__y * 5
print('---------------')
d = B(1, 4)
d.h
print(d._x)
print(d._D__y)
print('----------')
d1 =C(2, 6)
d1.h()
print(d1.h())	#x = 2, y = 6
print(d1._D__y)
print(C.__mro__)	#inherintance series 
print('----------')
c =D(4, 8)
print(c._x)
print(c._D__y)
print(c.func(5, 2))
print('--------------')
import re
class person:

    def __init__(self, age =15 , name = None, mail = None):
        self.age = age
        self.name = name
        self.mail = mail

    def info(self):
        return f'{self.name} is {self.age} years old and email is {self.mail}'
    @property
    def checkname(self):
        if self.name == None :
            return 'Fill The Name'
            self.setname()
        else:
            self.info()

            
    @property
    def checkmail(self):
        if self.mail == None:
            return 'fill the mail'
        else:
            self.info()
            
    @checkname.setter
    def setname(self, a):
        self.name = a
        
    @checkmail.setter
    def setmail(self, m):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, m)):
            print('valid')
            self.mail = m
        else:
            print('Not Valid')
    

p1 = person()
print(p1.name)
print(p1.info())
print(p1.checkname)
p1.setname = 'ali'
print(p1.info())
p1.setmail = 'hassan.uosefi158@gmail.com'
print(p1.info())

