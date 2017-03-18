base = int(input("Enter an integer: "))
exp = int(input("Enter the exponent: "))

def power_to(base, exp):
	if exp == 1:
		return base
	elif exp == 0:
		return 1
	elif exp < 0:
		return 1 / power_to(base, exp * -1)
		
	return base * power_to(base, exp - 1)

print(power_to(base, exp))