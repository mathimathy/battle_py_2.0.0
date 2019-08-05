from random import *
from module.guerrier import *
from module.sorcier import *
from module.templier import *

def jeu_b(attack1b, attack2b, bot, player, d):
	attack = randint(1, 2)
	if attack == 1:
			attack1_degat = bot.get_attack1()
			player.dammage(attack1_degat)
			print("bot attaque", attack1b)
	elif attack == 2:
		if d == 1:
			attack2_degat = bot.get_attack2()
			player.dammage(attack2_degat)
			print("bot attaque", attack2b)
			d -= 1
			return d
		elif d == 2:
			attack2_degat = bot.get_attack2()
			player.dammage(attack2_degat)
			print("bot attaque", attack2b)
			d -= 1
			return d
		elif d == 3:
			attack2_degat = bot.get_attack2()
			player.dammage(attack2_degat)
			print("bot attaque", attack2b)
			d -= 1
			return d
		else:
			attack1_degat = bot.get_attack1()
			player.dammage(attack1_degat)
			print("bot attaque", attack1b)