class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed

		self.miles = 0

	def displayinfo(self):
		print 'Bike Price: $' + str(self.price)
		print 'Max Speed: ' + str(self.max_speed) + 'mph'
		print 'Total Miles: ' + str(self.miles) + ' miles'
		return self

	def ride(self):
		print 'Riding..'
		self.miles += 10
		return self

	def reverse(self):
		print 'Reversing..'
		self.miles -= 5
		return self

bike1 = Bike(200, 25)
print 'Bike1'
bike1.ride().ride().ride().reverse().displayinfo()


fastbike = Bike(1000,100)
print 'fastbike'
fastbike.ride().ride().reverse().reverse().displayinfo()

bumbike = Bike(1, 1)
print 'bumbike'
bumbike.reverse().reverse().reverse().displayinfo()