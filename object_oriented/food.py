
class food:
    payment = 4

    def __init__(self, price, name):
        self.price = price
        self.name = name
        
    @property
    def show(self):
        return f'your food is {self.name} with {self.price}$'
    
class fastfood(food):

    def __init__(self, price, name, cal):
        super().__init__(price, name)
        self.cal = cal

    @property
    def show(self):
        return f'{self.name} has {self.cal} callories and price:{self.final_pay(self.price)}$'

    @property
    def pay(self):
        return self.final_pay(self.price)

    @staticmethod
    def final_pay(r):
        return r + food.payment

class traditinal(food):

    def __init__(self, price, name, cal=200):
        super().__init__(price, name)
        self.cal = cal 


    @property
    def pay(self):
        return self.final_pay(self.price)

    @staticmethod
    def final_pay(r):
        monye = r + food.payment
        return monye


    @property
    def show(self):
        return f'{self.name} has {self.cal} callories and price:{self.final_pay(self.price)}$'


pizza = fastfood(14,'pizza' ,650 )
print(pizza.show)
print(pizza.pay)

chicken = traditinal(20, 'chicken')
print(chicken.show)
print(chicken.pay)
