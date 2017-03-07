import sys

sys.setrecursionlimit(100000);

def multiply(multiplier, multiplicand):
	if multiplicand == 0:
		return 0;
	elif multiplier == 0:
		return 0;
		
	if multiplicand < 0 and multiplier < 0:
		multiplier *= -1;
		multiplicand *= -1;
		return multiply(multiplier, multiplicand);
	elif multiplicand < 0:
		print("-", end = "");
		multiplicand *= -1;
		return multiply(multiplier, multiplicand);
	elif multiplier < 0:
		print("-", end = "");
		multiplier *= -1;
		return multiply(multiplier, multiplicand);
	
	return multiplicand + multiply(multiplier - 1, multiplicand);
		
multiplicand = int(input("Enter number to be multiplied: "));
multiplier = int(input("Enter times to be multiplied: "));

print(multiply(multiplier, multiplicand));