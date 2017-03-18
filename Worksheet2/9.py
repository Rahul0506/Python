num = int(input("Enter a positive integer: "))

def factorial(num):
	if num == 0:
		return 1
	
	res = 1
	for i in range(1, num+1):
		res *= i
	
	return res
	
print(factorial(num))