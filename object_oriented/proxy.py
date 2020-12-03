from abc import ABCMeta,abstractmethod

"""
now we must define a common interface for real subject and  proxy 
can be used anywhere a realsubject 
"""
class shopping (metaclass = ABCMeta):
    @abstractmethod
    def buy(self):
        pass
    

""" 
now define realobject that proxy represents
"""
class bank(shopping):

    def __init__(self):
        self.account = None
        self.cart = None

    def _getaccount(self):
            self.account = self.cart
            return self.account


    def status (self):
        print('check mishavad ba ',self._getaccount(),' k mojodi darad ya na ')
        return False

    def setcart(self, cart):
        self.cart = cart
    

    def buy(self):
        if self.status():
            print('hazine pardakht shod')
            return True
        else:
            print('mojodi nadari,sorry')
            return False
    
"""
now we must have proxy and inheritance from interface 
"""

class cart(shopping):

    def __init__(self):
        self.bank = bank()
    
    def buy(self):
        cart = input('enter the cartnumber :')
        return self.bank.buy()



class customer():
    def __init__(self):
        print('dar hale pardakht hazine : ')
        self.cart = cart()
        self.kharid = None

    def  kharidan(self):
        self.kharid = self.cart.buy()  

    def __del__(self):
        if self.kharid:
            print('mn ba movafaghiat kharid kardam')

you = customer()
you.kharidan()