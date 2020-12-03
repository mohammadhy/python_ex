class animal:
 	def __init__(self, name, typee):
 		self.name = name
 		self.typee = typee

 	def info(self):
 		full_info = f'name of animal is  {self.name} and type is {self.typee} '
 		return full_info	

## this is for change type of animal
 	def set_type(self, typee):
 		self.typee = typee 
##this is for change name of animal
 	def set_name(self, name):
 		self.name = name

class wild_animal:
	
	def __init__(self, name, food):
		self.name = name 
		self.food = food

	def info_wild(self):
		full_info = f'this {self.name} eat {self.food} and his name is {self.name}'
		return full_info

class domestic_animal(wild_animal):

	def __init__(self, name, food, placelive):
		super().__init__(name, food)
		self.placelive = placelive

	def info_domestic(self):
		full_info = f'this {self.name} eat {self.food} and live in {self.placelive}'
		return full_info

	def set_name(self, name):
		self.name = name	

##create instance of class
dog = animal('wiliam', 'wild')
print(dog.info())
dog.set_type('homi')
print(dog.info())

dog1 = wild_animal('wiliam', 'meet')
print(dog1.info_wild())

cat = domestic_animal('ion', 'fish', 'apartment')
cat.set_name('jolian')
print(cat.info_domestic())