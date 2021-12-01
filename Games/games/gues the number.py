import random

gues = input("how big should the max number be? : ")

print("gues the number")

while 1 :
	number = random.randint(1, int(gues))
	score = 0
	found = 0
	while (int(found) == 0):
		player = input("write a number : ")
		if int(player) == int(number):
			print("well done you found it, it was " + str(number) + " \nyour score was " + str(score))
			found = 1
		elif int(player) < int(number):
			print("too small")
			score += 1
		elif int(player) > int(number):
			print("too big")
			score += 1
		else:
			print("not a number")