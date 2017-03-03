import math

n = int(input("Enter the prime number you want: "))

print("Prime number" , n , ": ", end = "")

upperLimit = 10000

sievedList = [x for x in range(3, upperLimit + 1, 2)]

for i in sievedList:
	if i <= sievedList[n]:
		for j in sievedList:
			if j == i:
				continue
			elif j % i == 0:
				sievedList.remove(j)

if n == 1:
	print(2)
else:
	print(sievedList[n-2])