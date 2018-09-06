def two_sum(numbers, target):
   	
	# Find two numbers (not same index/position) in the array 'numbers', whose sum is equal 
	# to target. Return indices of the 2 numbers from the array : [index_1, index_2]
	#
	# Example: 
	# numbers = [2,3,3,2], target = 6
	# returns [1,2] 
	
    for index_1, first in enumerate(numbers):
        for index_2, second in enumerate(numbers):
           if (first+second == target) and (index_1!=index_2): 
                return [index_1, index_2]
