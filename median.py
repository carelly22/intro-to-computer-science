# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

#def median(a,b,c):
#	if ((a>=b) and (a<=c)) or ((a>=c) and (a<=b)):
#		return a
#	elif ((b>=a) and (b<=c)) or ((b>=c) and (b<=a)):
#		return b
#	elif ((c>=a and c<=b)) or ((c>=b and c<=a)):
#		return c

#median function which tells you the median of three numbers
def median(a,b,c):
	big = biggest(a,b,c)
	if (big == a):
		return (bigger(b,c))
	elif (big == b):
		return (bigger(a,c))
	else:
		return c

print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7

print(median(3,2,1))
#>>> 2