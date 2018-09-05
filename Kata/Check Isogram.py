def is_isogram(string):
    
    # Check if given string is an Isogram: 
    # If each letter of the string is unique
    # (not repeated)
    #
    lowercase_string = string.lower()    
    count  = [lowercase_string.count(x) for x in lowercase_string]
    if len(count)!=0 and max(count)>1:
        return False
    return True

    # Alternatively
    #--------------------
    # if len(string) == len(string.lower())
    #       return True
    # return False
    
