
class dog(animal):
	def __init__(self):
		super(dog, self).__init__()
		self.health = 150

	def pet(self):
		self.health+= 5
		return self

dog = dog(kiba)
dog.walk().walk().walk().run().run().pet().displayHealth()
