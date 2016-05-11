# class MathDojo(object):
# 	def __init__(self):
# 		self.result = 0

# 	def add(self, *nums):
# 		for x in nums:
# 			self.result += x
# 		return self

# 	def subtract(self, *nums):
# 		for x in nums:
# 			self.result -= x
# 		return self

# 	def result(self):
# 		return result

# print MathDojo().add(2).add(2, 5).subtract(3, 2).result

class MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self, *nums):
		for i in nums:
			if self.is_tuple_or_list(i):
				for j in i:
					self.result += j
			else:
				self.result += i
		return self

	def subtract(self, *nums):
		for i in nums:
			if self.is_tuple_or_list(i):
				for j in i:
					self.result += j
			else:
				self.result += i
		return self

	def result(self):
		return result

	def is_tuple_or_list(self, obj):
		return isinstance(obj,list) or isinstance(obj,tuple)

print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
print MathDojo().add(( 1 ),3,4).add([3, 5, 7, 8], ( 2, 4.3, 1.25 )).subtract(2, ( 2,3 ), [1.1, 2.3]).result

