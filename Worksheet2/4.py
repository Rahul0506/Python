num = int(input("Enter a positive integer: "))

def num_digits(num):
	count = 0
	for i in str(num):
		count += 1
	
	return count

print(num_digits(num))