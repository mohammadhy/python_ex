from abc import abstractmethod,ABCMeta
class icar (metaclass = ABCMeta):
#this is interface of this factor 
#in this pattern client use the factory to creat product

    @abstractmethod
    def get_dim(self):
        """tihs is interface"""

class mercedes(icar):
    def __init__(self):
        self.model = 's500'
        self.classcar = 'luxury'
    def get_dim(self):
        return {'model':self.model,'classcar': self.classcar}

class ford(icar):
    def __init__(self):
        self.model = 'mustang'
        self.classcar = 'musle'
        self.engine = '5000CC'
    def get_dim(self):
        return {'model': self.model, 'clascar': self.classcar, 'engine': self.engine}


#dar inja bayd ye factory tarif kunim hala
class carfactory():

    @abstractmethod
    def get_car(cartype):
        try:
            if cartype == 'mercedes':
                return mercedes()
            #raise AssertionError('car not found,sorry try agin')
            else :
                  if  cartype == 'ford':
                        return ford()
            raise AssertionError('car not found,try later')


        except AssertionError as _a :
            print(_a)

if __name__ =='__main__':
    car = carfactory.get_car('mercedes')
    car1 = carfactory.get_car('ford')

    print(car.get_dim())
    print(car1.get_dim())