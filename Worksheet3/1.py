n = int(input("Enter upper limit: "))

upper_limit = round(n**0.5)
f = open("c:/Users/Rahul/Desktop/perfect_squares.txt", "w")

for i in range(upper_limit):
	f.write(str(i**2) + "\n")
	
f.close()

m = int(input("Enter m: "))

f = open("c:/Users/Rahul/Desktop/perfect_squares.txt", "a")

for i in range(n + 1, n + m + 1):
	f.write(str(i) + "\n")
	
f.close()