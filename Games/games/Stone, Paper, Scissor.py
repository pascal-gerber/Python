import random

wins = 0
aich = ("")

while 1:
	numb = 0
	ai = random.randint(1, 3)
	player = input("Stone, Paper, Scissor :")
	if (player == "Stone"):
		numb = 1	
	elif(player == "Paper"):
		numb = 2
	elif(player == "Scissor"):
		numb = 3
	else:
		print("invalid input")
	if int(ai) == 1:
		aich = str("Stone")
	elif  int(ai) == 2:
		aich = str("Paper")
	elif  int(ai) == 3:
		aich = str("Scissor")
	if int(numb) == int(ai):
		print("\ndraw\nyou both got " + str(player))
	elif int(numb) + 1 == int(ai):
		print("\nyou lost\nai got " + aich + " and you got " + player )
		wins -= 1
	elif int(numb) - 1 == int(ai):
		print("\nyou won\nai got " + aich + " and you got " + player )
		wins += 1
	elif int(numb) - 2 == int(ai):
		print("\nyou lost\nai got " + aich + " and you got " + player )
		wins -= 1
	elif int(numb) + 2 == int(ai):
		print("\nyou won\nai got " + aich + " and you got " + player )
		wins += 1
	print("\nwins = " + str(wins))