class observable:

    def __init__(self):
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)
            print('ezafe shod.!')

    def deregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
            print('hazf anjam shod! ')

    def update_obs(self, *arg, **kwarg):
        for observer in self.observers:
            observer.update(*arg, **kwarg)


class observer:
    def update(self, *arg, **kwarg):
        pass 


class ABCnews(observer):
    def update(self, *arg, **kwarg):
        print(type(self).__name__,'{0} {1} '.format(arg, kwarg))

class BBCnews(observer):
    def update(self,*arg, **kwarg ):
        print(type(self).__name__,'{0} {1}'.format(arg, kwarg))

news = observable()
BBC = BBCnews()
ABC = ABCnews()
news.register(ABC)
news.register(BBC)
news.update_obs('this is news :', mesg = 'today we hope find new place in planet')
