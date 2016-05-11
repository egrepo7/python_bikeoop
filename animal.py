# Now, create another class called Dragon that also inherits everything from Animal, but 1) have the default health be 170 and 2) add a new method called fly, which when invoked, decreased the health by 10. Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth(). When the Dragon's displayHealth function is called, have it say 'this is a dragon!' before it displays the default information (by calling the parent's displayHealth function).

# Now for the first instance of the animal (instance called 'animal'), try calling fly() or pet() and make sure this doesn't work.  (-:

class animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print 'Name: ' + self.name
		print 'Current Health: ' + str(self.health)
		return self

class dog(animal):
	def __init__(self, name):
		super(dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health+= 5
		return self

class Dragon(animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self):
		self.health -= 10
		return self

	def displayHealth(self):
		print "This is a dragon!"
		super(Dragon, self).displayHealth()

#my piggy cant fly or be pet

animal = animal('Piggy')
animal.walk().walk().walk().run().run().displayHealth()
dog = dog('kiba')
dog.walk().walk().walk().run().run().pet().displayHealth()
dragon = Dragon('Drogon')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()

