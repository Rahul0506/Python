listNum = [19, 209, 38];
listNum.sort()

listFactors = [];

def getFactor(num, listFactors):
	for i in range(1, num + 1):
		if num % i == 0:
			listFactors.append(i)
			
getFactor(listNum[-1], listFactors)

gcf = 0

for y in listNum:
	for x in listFactors:
		if y % x == 0:
			if gcf < x:
				gcf = x
		else:
			listFactors.remove(x)

print(gcf)