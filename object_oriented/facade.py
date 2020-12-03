#facade design pattern is very good for have simple interface an clinet have connection just to facade and do not khonw anythin about complex for class

class cook(object):
    #cook is a instance of type 
    #dec: provide esay interface 
    def preparefood(self):
        self.write_order = write_order()
        self.write_order.write_orders()

        self.cooker = cooker()
        self.cooker.cook_food()

        self.give_order = give_order()
        self.give_order.give_orders()


class write_order(object):
    def write_orders(self):      
        print(input('what whould you like to order:'))



class cooker(object):
    def cook_food(self):
        #b ma type bar migardanad chon class ma ye instance az type ast 
        print('give me the order from:',type(write_order).__name__)


class give_order(object):
    def give_orders(self):
        print('here you are :enjoy your food')

#we need to customer to order 
if __name__ == '__main__':
    customer = cook()
    customer.preparefood()
