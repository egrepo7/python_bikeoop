# Create an instance of the animal called 'animal' and have this animal walk three times, run twice, and have it display its health.

# Now, create another class called Dog that inherits everything that the Animal does and have, but 1) have the default health be 150 and 2) add a new method called pet, which when invoked, increase the health by 5. Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().

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

animal = animal('Piggy')
animal.walk().walk().walk().run().run().displayHealth()

class dog(animal):
	def __init__(self):
		super(dog, self).__init__()
		self.health = 150

	def pet(self):
		self.health+= 5
		return self

dog = dog(kiba)
dog.walk().walk().walk().run().run().pet().displayHealth()

