class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed

		self.miles = 0

	def displayinfo(self):
		print 'Bike Price: $' + str(self.price)
		print 'Max Speed: ' + str(self.max_speed) + 'mph'
		print 'Total Miles: ' + str(self.miles) + ' miles'

	def ride(self):
		print 'Riding..'
		self.miles += 10

	def reverse(self):
		print 'Reversing..'
		self.miles -= 5

bike1 = Bike(200, 25)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
print bike1.displayinfo()

fastbike = Bike(1000,100)
fastbike.ride()
fastbike.ride()
fastbike.reverse()
fastbike.reverse()
print fastbike.displayinfo()

bumbike = Bike(1, 1)
bumbike.reverse()
bumbike.reverse()
bumbike.reverse()
print bumbike.displayinfo()
