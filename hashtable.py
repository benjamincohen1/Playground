class hashtable():

	def __init__(self, size):
		self.table = [None] * size
		print self.table
		self.size = size

	def hash(self, key, val):

		z = hash(str(key)) % self.size
		if z in self.table:
			#fuck collisions
			pass
		else:
			self.table[z] = val
		return hash(key) % self.size