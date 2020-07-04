class Player:
	def __init__(self):
		self.health = 100
		self.speed = 1
		self.size = 1
		self.distance = 0
		self.level = 1
		self.x_position = (0,0)
		self.y_position = (10,10)

	def movement(self):
		pass
	def health(self):
		pass
	def size(self):
		pass
	def speed(self):
		pass
	def distance(self):
		pass

class Enemy:
	pass	


class Mario(Player):
	def __init__(self):
		super().__init__()
		self.character = 'Mario'

	def hit_enemy(self):
		return True	
	def play(self):
		if self.hit_enemy:
			self.health -= 5




m = Mario()
print(m.character)
print(m.health)
m.play()
print(m.health)
