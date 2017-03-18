num = int(input("Enter a positive integer: "))

def sum_all(num):
	added = 0
	
	for i in range(1, num+1):
		added += i
	
	return added

print(sum_all(num))