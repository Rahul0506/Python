i = int(input("Enter an integer between 1 and 12 (inclusive): "))

print("Multiples of " + str(i) + ": ")
for k in range(1, 13):
	print(i*k)