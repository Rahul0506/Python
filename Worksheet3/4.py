while True:
	num = int(input("Enter your integer: "))
	
	if num **0.5 > 998537:
		print("Number entered is out of range (max is 9900000000000)") #Actually limit can be higher but eh...
	else:
		break

f = open("primes1000000.txt", "r")
primes = f.read().split()
f.close()

def checkPrime(num, primes):
	if str(num) in primes:
		return True
	
	for i in primes:
		if num % int(i) == 0:
			return False
			
	return True
	
print(checkPrime(num, primes))