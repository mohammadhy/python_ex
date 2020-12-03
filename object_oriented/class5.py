from abc import ABC, abstractmethod
import cv2
class account(ABC):   
    def __init__(self, name, password, email, photo):
        self.name = name
        self.password= str(password)
        self.email = email
        self.photo = photo
        super().__init__()
    
    @abstractmethod    
    def n(self):
       pass
   
    def p(self):
       pass

    
class setting(account):
    def n(self):
        return 'firstname:'+' '+ self.name 
    
    def p(self, path):
         img= cv2.imread(path)
         return cv2.imshow('a',img)

    def newname(self, nam):
        self.name = nam
        
    @staticmethod
    def checkage(age):
        if age < 18 :
            return 'You Can Make Acoount Sorry'
        else:
            return 'Welcome'
    

ob = setting('hassan', 15, 'yahoo@.com', 'aaa')    
print(ob.n())
#for picture:
#path = 'C:/Users/Asus/OneDrive/Pictures/Saved pictures/a.jpg'
#ob.p(path)

#for check age:   
print(ob.checkage(20))

#rename:
ob.newname('ahmad')
print(ob.n())



