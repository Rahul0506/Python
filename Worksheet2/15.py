n = int(input("Enter your number: "));
a = 1;
x = 0;
y = 1;

def getFibo(x, y, a, n):
	z = 0
	if a <= n:
		z = x + y;
		a += 1;
		return getFibo(y, z, a, n);
	else:
		return x;
		
print(getFibo(x, y, a, n));