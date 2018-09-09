def diamond(n):

	# creating diamond pattern (n = rows)
	# n = 3 
	# 
	#  *
	# ***
	#  *

    if n%2==0 or n<=0: return None

    numbers_pattern = [i for i in range(n+1) if i%2==1]        				# [1,3,5,7...]
    reverse_pattern = [items for items in reversed(numbers_pattern[:-1])]		
    numbers_pattern = numbers_pattern + reverse_pattern
    max_no = max(numbers_pattern)
    pattern = [" "*((max_no-i)/2) + "*"*i + "\n" for i in numbers_pattern]
    return "".join(pattern)

