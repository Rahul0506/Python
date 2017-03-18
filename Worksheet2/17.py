pairs = int(input("Enter the number of pairs of brackets: "))

def brac_perm(out, open, close, pairs):
	if open == pairs and close == pairs:
		print(out)
	else:
		if open < pairs:
			brac_perm(out + "(", open + 1, close, pairs)
		if close < open:
			brac_perm(out + ")", open, close + 1, pairs)
				
brac_perm("", 0, 0, pairs)