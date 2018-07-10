# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element (my_list, value):
	i = 0
	while i < len(my_list):
		if (my_list[i] == value):
			return i
		i = i + 1
	return -1
#Test cases
print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1

print find_element(['flower', 'petal', 'tree', 'grass'], 'petal')
#>>> 1