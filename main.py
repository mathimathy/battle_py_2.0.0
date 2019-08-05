#importation des fichier
from module.guerrier import *
from module.sorcier import *
from module.templier import *
from bot import *
from function import *
import pickle

#importation des module
import time
from random import *

#definition des autres variables
e = 1
a = 1
d = 1
db = 0
c = 1
f = 1
g = 1
ddb = 0
	
#definition de la dificultée
try:
	player, dificult, race, attaque1, attaque2 = load()
	if dificult == "0":
		try:
			b + "a"
		except:
			while f == 1:
				clear()
				dificult = input("Choix de la dificultée: facile, moyen ou difficile ? ")
				if dificult == 'facile':
					ddb = 1
					f = 2
					price = 2
				elif dificult == 'moyen':
					ddb = 2
					f = 2
					price = 4
				elif dificult == 'difficile':
					ddb = 3
					f = 2
					price = 5
				else:
					print('cette dificultée n\'existe pas')
					time.sleep(1)
				db = ddb

			#definition de la race du joueur
			while c == 1:
					clear()
					pseudo = input("Quel est votre pseudo ? ")
					#verification du pseudo
					b = verify(pseudo)

					if b == 'true':
						c = 2
					elif b == 'false':
						pass

			while g == 1:
				clear()
				race = input("Que voulez vous etre (guerrier, sorcier, templier) ? ")

				if race == 'guerrier':
					player = guerrier(pseudo)
					attaque1 = "tranche"
					attaque2 = "piquéer"
					g = 2
				elif race == 'sorcier':
					player = sorcier(pseudo)
					attaque1 = "boule de feu"
					attaque2 = "glaciationg"
					g = 2
				elif race == 'templier':
					player = templier(pseudo)
					attaque1 = "coup de bouclier"
					attaque2 = "fendoir"
					g = 2
				else:
					print("ce personnage n'existe pas")
					time.sleep(1)
except:
	while f == 1:
		clear()
		dificult = input("Choix de la dificultée: facile, moyen ou difficile ? ")
		if dificult == 'facile':
			ddb = 1
			f = 2
			price = 2
		elif dificult == 'moyen':
			ddb = 2
			f = 2
			price = 4
		elif dificult == 'difficile':
			ddb = 3
			f = 2
			price = 5
		else:
			print('cette dificultée n\'existe pas')
			time.sleep(1)
		db = ddb

	#definition de la race du joueur
	while c == 1:
			clear()
			pseudo = input("Quel est votre pseudo ? ")
			#verification du pseudo
			b = verify(pseudo)

			if b == 'true':
				c = 2
			elif b == 'false':
				pass

	while g == 1:
		clear()
		race = input("Que voulez vous etre (guerrier, sorcier, templier) ? ")

		if race == 'guerrier':
			player = guerrier(pseudo)
			attaque1 = "tranche"
			attaque2 = "piquéer"
			g = 2
		elif race == 'sorcier':
			player = sorcier(pseudo)
			attaque1 = "boule de feu"
			attaque2 = "glaciationg"
			g = 2
		elif race == 'templier':
			player = templier(pseudo)
			attaque1 = "coup de bouclier"
			attaque2 = "fendoir"
			g = 2
		else:
			print("ce personnage n'existe pas")
			time.sleep(1)
finally:
	if dificult == 'facile':
		ddb = 1
		f = 2
		price = 2
	elif dificult == 'moyen':
		ddb = 2
		f = 2
		price = 4
	elif dificult == 'difficile':
		ddb = 3
		f = 2
		price = 5
	db = ddb
	
	print("Bienvenu", player.get_pseudo())

	time.sleep(2)
	clear()

	while e == 1:
		clear()
	#definition de la race du bot
		raceb = randint(1, 3)

		if raceb == 1:
			bot = guerrier("")
			raceb = 'guerrier'
			attack1b = "tranche"
			attack2b = "piquéer"
		elif raceb == 2:
			bot = sorcier("")
			raceb = 'sorcier'
			attack1b = "boule de feu"
			attack2b = "glaciation"
		elif raceb == 3:
			bot = templier("")
			raceb = 'templier'
			attack1b = "coup de bouclier"
			attack2b = "fendoir"
		
		clear()
		#boucle principale du jeu
		while a == 1:
			commande = input("Que voulez vous faire ? ")

			if commande == 'quitter':
				save(player, dificult, race, attaque1, attaque2)
				quit()
			elif commande == 'stat':
				clear()
				print(race)
				print("vie", player.get_health())
				print("armure", player.get_armure())
				print("or", player.get_gold())
			elif commande == 'statb':
				clear()
				print(raceb)
				print("vie", bot.get_health())
				print("armure", bot.get_armure())
			elif commande == 'attaquer':
				clear()
				attack = input("Quel attaque voulez vous faire (1: {}, 2: {}) ? ". format(attaque1, attaque2))
				if attack == '1':
					attack1_degat = player.get_attack1()
					bot.dammage(attack1_degat)
					print(player.get_pseudo(), "attaque", attaque1)
					db = jeu_b(attack1b, attack2b, bot, player, db)
				elif attack == '2':
					if d != 0: 
						attack2_degat = player.get_attack2()
						bot.dammage(attack2_degat)
						print(player.get_pseudo(), "attaque", attaque2)
						d -= 1
						db = jeu_b(attack1b, attack2b, bot, player, db)
					else:
						print('Vous ne pouvez plus utiliser cette attaque !')
			elif commande == 'blade':
				boolean = player.achat(price)
				if boolean == 'true':
					player.blade()
					print('Achat reussi !!')
				elif boolean == 'false':
					print('Vous n\'avez pas assez d\'argent pour l\'acheter !!')
			elif commande == 'potion':
				price = price + 2
				boolean = player.achat(price)
				if boolean == 'true':
					player.blade_health()
					print('Achat reussi !!')
				elif boolean == 'false':
					print('Vous n\'avez pas assez d\'argent pour l\'acheter !!')
			elif commande == '^[[A^[[A^[[C^[[D^[[B^[[A':
				code = input('Code d\'acsses ')
				if code == '$Root$596247318$Root$':
					print('astuces: il parait que quand on attaque pas avec la 2 pendant l\'armure on a plus de chance de gagner :)')
				else:
					print('code d\'acsses invalide !')

			elif commande == 'help':
				clear()
				print('quitter = permet de quitter le jeu')
				print('attaquer = permet d\'attaquer')
				print('stat = permet d\'afficher vos stat')
				print('statb = permet d\'afficher les stat du bot')
				print('blade = permet de recharger les point d\'armure')
				print('potion = permet de recharger sa vie')
			else:
				print("ce que vous essayez de faire n'est pas possible utiliser \'help\' pour avoir de l'aide")

			health = player.get_health()
			bot_health = bot.get_health() 

			e, a, d, db = game_over(health, bot_health, e, a, d, db, ddb, player, race, raceb, attaque1, attaque2)
			e, a, d, db = win(bot_health, health, e, a, d, db, ddb, player, dificult, race, raceb, attaque1, attaque2)