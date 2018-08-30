def series_sum(n):
    
	# Find sum of series S: 1+1/3 + 1/7 + 1/10 + ..... upto 'n' terms
	
    sum1 = sum([1/(1+3*_) for _ in range(0,n)])
    return "{:.2f}".format(sum1)
    
    # or you can do 
    #
    # sum  = 0
    # for _ in range(0,n):
    #     sum+=1/(1+3*_)
    # return "{:.2f}".format(sum) 
	
	
	
	