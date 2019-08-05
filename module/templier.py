class templier:

	def __init__(self, pseudo):
		self.pseudo = pseudo
		self.health = 22
		self.armure = 5
		self.attack1 = 4
		self.attack2 = 8
		self.gold = 10

	def get_pseudo(self):
		return self.pseudo

	def get_health(self):
		return self.health

	def get_armure(self):
		return self.armure

	def get_attack1(self):
		return self.attack1

	def get_attack2(self):
		return self.attack2

	def get_gold(self):
		return self.gold

	def dammage(self, dammage):
		if self.armure > 0:
			self.armure -= 1
			dammage = 0
		self.health -= dammage

	def attack1(self, target_player):
		dammage = self.attack1
		target_player.dammage(dammage)

	def attack2(self, target_player):
		dammage = self.attack2
		target_player.dammage(dammage)

	def blade(self):
		self.armure = 5

	def blade_health(self):
		self.health = 22

	def achat(self, price):
		if self.gold > price:
			self.gold -= price
			return "true"
		else:
			return "false"

	def pay(self, price):
		self.gold += price