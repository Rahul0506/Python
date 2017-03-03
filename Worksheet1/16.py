p1 = input("Player 1, enter your move: ").lower()
p2 = input("Player 2, enter your move: ").lower()

win = 1

if p1 == p2:
	print("Its a draw!")
else:
	l = ["rock", "paper", "scissors", "lizard", "spock"]
	if p1 == l[0]:
		if p2 == l[1] or p2 == l[4]:
			win = 2
	elif p1 == l[1]:
		if p2 == l[2] or p2 == l[3]:
			win = 2
	elif p1 == l[2]:
		if p2 == l[0] or p2 == l[4]:
			win = 2
	elif p1 == l[3]:
		if p2 == l[0] or p2 == l[2]:
			win = 2
	else:
		if p2 == l[1] or p2 == l[3]:
			win = 2

	print("Player " + str(win) + " wins!")