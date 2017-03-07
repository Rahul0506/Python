exitString = "lol"
f = open("rationals.txt", "w")
f.close()
while True:
	a = input("Enter your input: ")
	try:
		b = float(a)
	except:
		if a == exitString:
			print("Exiting now...")
			break
		else:
			pass
	else:
		f = open("rationals.txt", "a")
		f.write(a + "\n")
		f.close()