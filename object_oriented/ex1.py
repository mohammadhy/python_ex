'''
This is Class Example:  
    EX: Online Shopping
'''
class Info:
    def __init__(self, name, password, email, phone=None):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone


class Seller(Info):
    def __init__(self, name, password, email, phone):
        super().__init__(name, password, email, phone)
        
    def __str__(self):
        return (f'This Is Name of seller:{self.name} And His Phone-Number{self.phone}')
    

print('Instance Seller:')
s1 = Seller('ali', 'aliayobi', 'ali@yahoo.com', '9129056738')
print(s1)

class Customer(Info):
    def __init__(self, name, password, email, phone=None):
        super().__init__(name, password, email, phone)

    def __str__(self):
        
        return(f'{self.name} Has {self.password} And Email {self.email}')


print('Instance Customer:')
c1 = Customer('hassan', '1377123', 'hassan.gmail.com')
print(c1)

class Product:
    def __init__(self, code, categori,Seller ,price=None,):
        self.code = code
        self.categori = categori
        self.price = price
        self.Seller = Seller

    def __str__(self):
        return(f'This {self.categori} Categori Has Selling By {self.Seller.name} And This {self.price} $')

print('Instance Product:')
p1 = Product('#325', 'Digital', Seller = s1, price=(15))
print(p1)


