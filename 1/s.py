cdevfbrb
def bigger(a,b):
	if a>b:
		return a
	else:
		return b

def biggest (a,b,c):
	return bigger(bigger(a,b),c)

def median (a,b,c):
	f = biggest(a,b,c)
	if f == a:
		if c>=b:
			return c
		else:
			return b
	if f == b:
		if a>=c:
			return a
		else:
			return c
	if f == c:
		if a>=b:
			return a
		else:
			return b




print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7
			


