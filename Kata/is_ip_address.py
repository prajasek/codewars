def ipv4_address(address):

    	#  Implement ipv4_address?, which should return true if  given 
    	#  object is an IPv4 address - four numbers (0-255) separated by dots.
    	#  It should only accept addresses in canonical representation, 
    	#  so no leading 0s, spaces etc.
	#
	# 1.2.3.4    True
	# 01.2.3.4   False - leading zeros
	# 1222.2.3.4 False - number > 255
	# x.1.2.3    False - non-integer 
	# .2.3.4     False - no spaces/None values 	
	
	
    # IP a.b.c.d -> [a,b,c,d] 
    ip_nums = address.split(".")
    
    # IP has only 4 numbers separated by "."
    if len(ip_nums)!=4 : return False 
    
    
    for number in ip_nums:
        try:
            if (not 0<=int(number)<=255) or (len(str(int(number)))!= len(number)):  # check if number is b/w (0,255) and no leading zeros
                return False
        except:  								    # if non-numeric
            return False    
    return True
