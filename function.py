import pickle
def clear():
	print("\n" * 50)

def verify(pseudo):
	len_pseudo = len(pseudo)
	if len_pseudo == 0:
		return 'false'
	else:
		return 'true'

def game_over(health, bot_health, e, a, d, db, ddb, player, race, raceb, attaque1, attaque2):
	if health == 0 and bot_health != 0 and bot_health > 0 or health < 0 and bot_health != 0 and bot_health > 0:
		print('Game Over')
		responce = input('Voulez vous recommancer ? (oui, non) ')
		if responce == 'oui':
			return 1, 1, 1, ddb
		elif responce == 'non':
			save(player, "0", race, attaque1, attaque2)
			quit()
	else:
		return 2, 1, d, db

def win(bot_health, health, e, a, d, db, ddb, player, dificult, race, raceb, attaque1, attaque2):
	if bot_health == 0 and health != 0 and health > 0 or bot_health < 0 and health != 0 and health > 0:
		print('You Win')
		if raceb == 'sorcier':
			player.pay(2)
		elif raceb == 'templier':
			player.pay(4)
		elif raceb == 'guerrier':
			player.pay(5)

		responce = input('Voulez vous recommancer ? (oui, non) ')
		if responce == 'oui':
			return 1, 1, 1, ddb
		elif responce == 'non':
			save(player, dificult, race, attaque1, attaque2)
			quit()
	else:
		return 2, 1, d, db

def save(player, dificult, race, attaque1, attaque2):
	attaque2 = "\n" + attaque2
	with open("save/player.save", "wb") as fic:
		record = pickle.Pickler(fic)
		record.dump(player)

	with open("save/dificult.save", "w") as fic:
		fic.write(dificult)

	with open("save/race.save", "w") as fic:
		fic.write(race)

	with open("save/attaque.save", "w") as fic:
		fic.write(attaque1)
		fic.write(attaque2)

def load():
	with open("save/player.save", "rb") as fic:
		get_record = pickle.Unpickler(fic)
		player = get_record.load()

	with open("save/dificult.save", "r") as fic:
		dificult = fic.read()

	with open("save/race.save", "r") as fic:
		race = fic.read()

	with open("save/attaque.save", "r") as fic:
		attaque1 = fic.readline()
		attaque2 = fic.readline()

	return player, dificult, race, attaque1, attaque2