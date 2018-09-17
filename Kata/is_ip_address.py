def ipv4_address(address):

    #  Implement String#ipv4_address?, which should return true if  given 
    #  object is an IPv4 address - four numbers (0-255) separated by dots.
    #  It should only accept addresses in canonical representation, 
    #  so no leading 0s, spaces etc.
	#
	# 1.2.3.4    True
	# 01.2.3.4   False
	# 1222.2.3.4 False
	# x.1.2.3    False
	# .2.3.4     False

    ip_nums = address.split(".")

    if not 3<len(ip_nums)<5 : return False 

    for number in ip_nums:
        try:
            if (not 0<=int(number)<=255) or (len(str(int(number)))!= len(number)):
                return False
        except:   
            return False    
    return True