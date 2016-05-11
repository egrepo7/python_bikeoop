class car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		
		if self.mileage > 10000:
			self.tax = '15%'
		else:
			self.tax = '12%'

		self.display_all()

	def display_all(self):
		print 'Price: $' + str(self.price)
		print 'Speed: ' + str(self.speed) + ' mph'
		print 'Fuel: ' + self.fuel
		print 'Mileage: ' + str(self.mileage) + ' miles'
		print 'Tax: ' + self.tax

pinto = car(1, 45, 'empty', 60000)
Honda = car(15000, 150, 'Full', 2000)
BMW = car(65000, 200, 'Full', 0)
Mercedes = car(80000, 200, 'Half Full', 20000)
Jeep = car(70000, 140, 'Half Empty', 40000)