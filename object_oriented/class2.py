"""
Created on Wed Aug 26 14:05:55 2020

@author: Asus
"""

class veichle:
    def __init__(self, company, type, power):
        self.company = company
        self.type = type
        self.power = power

class car(veichle):
    def __init__(self, company, type, power, energy):
        super().__init__(company, type, power)
        self.energy = input('This Car Use (Gas/Electronic):')
        
class sport_car(car):
    def __init__(self, company, type, power, energy, luxuary):
        super().__init__(company, type, power, energy)
        self.luxuary = 'yes'
        
    def shhow_info(self):
        return f'{self.company} has {self.power}cc and fill by {self.energy} type:{self.type} {self.luxuary}'
    
    def __str__(self):
        return f'{self.company} has {self.power}cc and fill by {self.energy} type:{self.type} {self.luxuary}'

sport = sport_car('lamborgini', 'coupe', 4500,'', '')

print(sport.shhow_info())
print(sport)






