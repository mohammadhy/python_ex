from abc import ABC, abstractmethod

class food(ABC):

    def __init__(self, name, prise):
        self.prise = prise
        self.name = name
        super().__init__()

    @abstractmethod
    def detail(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @property
    def show(self):
        return f'your food is {self.name} with {self.prise}$'

class fastfood(food):
    payment = 4
    def __init__(self, name, prise, content):
        self.content = content
        super().__init__(name, prise)

    def price(self):
        if self.prise > fastfood.payment:
            pay = self.prise + fastfood.payment
            return f"{str(pay)}$You Want To Pay for {self.name}" 
        else:
            return f'You Dont Need To Pay The Payment For {self.name} {self.prise}$'

    def detail(self):
        return f'this {self.name} contains: {self.content} '


class traditional(food):
    payment = 8
    def __init__(self, name, prise, content):
        self.content = content
        super().__init__(name, prise)

    def price(self):
        if self.prise > traditional.payment:
            pay = self.prise + traditional.payment
            return f"{str(pay)}$You Want To Pay for {self.name}" 
        else:
            pay = (self.prise + traditional.payment) * 0.5
            return f'{str(pay)}$ You Want To Pay For {self.name}'

    def detail(self):
        return f'this {self.name} contains: {self.content} '

pizza = fastfood('water', 2, 'h2o')
print(pizza.price())
print(pizza.detail())

stu = traditional('qorme stu', 7, 'vegtable and  meet')
print(stu.price())


