# Return Second Smallest Element

def second_smallest(array):
	smallest = array[0]
	second = array[0]

	for i in range(1,len(array)):
	    if array[i] < smallest:
	        second = smallest
	        smallest = array[i]
	return second