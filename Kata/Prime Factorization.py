def primeFactors(n):
	
	# Return (p1**n1)(p2**n2)(p3)(p4)(p5**n5)...
	# px - prime factor
	# nx - powers of the prime
	# Arrange the factorization from smallest to largest 
	# Input:  20
	# Output :  (2**2)(5)

    prime = 2; largest = 2 ; num = n 

    while num >= prime:   
        if num % prime == 0 :
            largest = prime
            num = num/prime
        else:   
            prime = prime+1

    prime_count = {}
    for number in range(2, largest+1):
        count = 0
        while n%number ==0:
            count +=1
            n=n/number
        if count>0:
            prime_count[number] = count 
    
    print(prime_count)
    

    primes_with_powers = ["({})".format(str(v) + "**" + str(pwr)) if pwr>1 else 
    "({})".format(str(v)) for v, pwr in sorted(prime_count.items())]

    return "".join(primes_with_powers)