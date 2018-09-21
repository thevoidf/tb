class Item:
	def __init__(self, value, length, ch):
		self.value = value
		self.length = length
		self.ch = ch
	
	def __str__(self):
		return self.ch + ' {} '.format(self.value).ljust(self.length + 2)

