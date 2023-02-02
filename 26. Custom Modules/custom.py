import random as r

myName = "Netsu"
friends = ["Josh", "Bak", "Lucas", "Caleb"]

def convertToCm(meter):
	return meter * 100

def flipCoin():
	side = r.randint(1, 2)
	if side == 1:
		return "Heads"
	else:
		return "Tails"