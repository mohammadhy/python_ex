"""
Created on Sun Mar 14 23:36:54 2021

# EX2
Section 5

"""
class Apartment:
    def __init__(self, floor, elavator, *args):
        self.floor = floor
        self.elavator = elavator
        super().__init__(*args)
        

class House:
    def __init__(self, old):
        self.old = old 
        
    def __str__(self):
        return f'This House Has Bulit in {self.old} Years Ago'        


class Sale:
    def __init__(self, price):
        self.price = price
        

class Rent:
    def __init__(self, rent_per_month, constans_money):
        self.rent_per_month = rent_per_month
        self.constans_money = constans_money



class RentApartment(Apartment, Rent):
    
    def __str__(self):
        return f'This Apartment At {self.floor} Floor And Elavator: {self.elavator} First Payment {self.constans_money} And Per Month {self.rent_per_month}'


class SaleApartment(Apartment, Sale):
    
  
    def __str__(self):
        return f'This Apartment At {self.floor} Floor And Elavator:{self.elavator} On Sale {self.price}$'
        
        

ra  = RentApartment(2, True, 50000, 1000)
print(ra)

sa = SaleApartment(4, 'yes', 75000000)
print(sa)




