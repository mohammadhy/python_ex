class veichle:
	"""docstring for Car"""

	def __init__(self, manufacture, model, year, category):
		
		self.manufacture = manufacture
		self.model = model
		self.year = year
		self.category = category


	def get_info(self):
		info = f"{self.manufacture} {self.model} {self.year} {self.category}"
		return info.title()

class car(veichle):

	def __init__(self, manufacture, model, year, category, capacityoil):
		super().__init__(manufacture, model, year, category)
		self.capacityoil = capacityoil

	def set_capacityoil(self, capacityoil):
		self.capacityoil = capacityoil

	def info_car(self):
		full_info = f'this {self.model} from {self.manufacture} and creat on {self.year} and has {self.capacityoil} capacity oil'
		return full_info.title()

class elctronic_car(veichle):

	def __init__(self,manufacture, model, year, category, battery_size):
		super().__init__(manufacture, model, year, category)
		self.battery_size = int(input(f'enter battery_size of {self.model}: '))

	def info_elctronic_car(self):
		full_info = f'this {self.model} from {self.manufacture} and creat on {self.year} and has {self.battery_size} kw'
		return full_info.title()

	def set_battery_size(self, battery_size):
		self.battery_size = battery_size
		return self.battery_size
  
"this is instance of our class"

my_veichle = veichle('audi', 'a9', 2018, 'coupe')
print(my_veichle.get_info())

my_car = car('toyota', 'yaris', 2020, 'sedan', 20)
my_car.set_capacityoil('30')
print(my_car.info_car())

my_car1 = elctronic_car('tesla', 's3', 2015, 'sedan', 450)
#if you have default value and after that change it the new value is new defination not default value
#my_car1.set_battery_size()
print(my_car1.info_elctronic_car())