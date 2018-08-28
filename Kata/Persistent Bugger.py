def persistence(n):

    if n<10:
        return 0
    n = str(n)
    count=0; 
    while True:
        value=1
        for digit in n:
            value=value*int(digit)
            print("value=", value)
        count+=1
        if value<10:
            return count
        n = str(value)
            