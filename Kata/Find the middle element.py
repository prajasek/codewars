def gimme(input_array):

	# Given array of 3 elements, find the index
	# of the element whose value is in between 
	# the other two 
	# For example : [2, 1, 3] --> 2 is in between
    # 1 and 3, so return 2's index, which is 1
	# 
    copy = input_array[:]
    input_array.sort()
    return copy.index(input_array[1])
    
    # or you can do 
    # return input_array.index(sorted(input_array)[1]))