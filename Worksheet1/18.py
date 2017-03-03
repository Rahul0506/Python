cent10In = int(input("Enter number of 10-cent coins inserted: "))
cent20In = int(input("Enter number of 20-cent coins inserted: "))
cent50In = int(input("Enter number of 50-cent coins inserted: "))
cent100In = int(input("Enter number of 1-dollar coins inserted: "))
drinkPrice = float(input("Enter price of drink (0.8 or 1.2): "))

money = (0.1 * cent10In) + (0.2 * cent20In) + (0.5 * cent50In) + (1 * cent100In)
money -= drinkPrice
money *= 100
money = int(money)

cent100Out = cent10Out = cent20Out = cent50Out = 0
print("Change to be returned = $", money/100)

while money >= 100:
	cent100Out += 1
	money -= 100
	
while money >= 50:
	cent50Out += 1
	money -= 50

while money >= 20:
	cent20Out += 1
	money -= 20
	
while money >= 10:
	cent10Out += 1
	money -= 10

print(cent100Out, " x 1-dollar coin(s)")
print(cent50Out, " x 50-cent coin(s)")
print(cent20Out, " x 20-cent coin(s)")
print(cent10Out, " x 10-cent coin(s)")