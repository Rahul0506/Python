number = int(input("Please enter a positive integer: "));

a = 2;
def checkPrimeRec(number, current):
	if current > (number**0.5 + 1):
		return True;
	elif number == 1:
		return False;
	elif (number % current) == 0:
		return False;
	else:
		current += 1;
		return checkPrimeRec(number, current);
		
def checkPrimeIter(number):
	if number == 1:
		return False;
	for i in range(2,round( number**0.5)+1):
		if i == number:
			return False;	
		elif (number % i) == 0:
			return False;
	return True;
		
print(checkPrimeRec(number, a));
print(checkPrimeIter(number));