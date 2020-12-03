class book:
    _shared_state ={}

    def __init__(self):
        self.__dict__ = self._shared_state
    
class singlebook(book):
    
    def __init__(self, **kwargs):
        book.__init__(self)
        self._shared_state.update(kwargs)


    def __str__(self):

        return str(self._shared_state)

x = singlebook(linuxbook = 'unix and linux5th')
y = singlebook(pythonbook = 'python crash course')
print(y)
