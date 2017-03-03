bDay = input("Enter your birthdate (dd/mm/yyyy): ").split("/")

b = int(bDay[0])
a = int(bDay[1])
c = int(bDay[2]) % 100
d = int(bDay[2]) // 100

if a <= 10:
	a -= 2
else:
	a += 10
	c -= 1

w = (13 * a - 1)//5
x = c // 4
y = d // 4
z = w + x + y + b + c - 2 * d
r = z % 7

dayList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if r < 0:
	r += 7
	
print(dayList[r])