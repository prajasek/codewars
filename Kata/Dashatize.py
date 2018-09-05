def dashatize(num):
    
    # Given a number, return a string with dash'-'marks before
    # and after each odd integer, but do not begin or end 
    # the string with a dash mark.
    # Example:
    # 12434 should return "1-24-3-4"  
    #
    
   
    if "None" in str(num):
        return "None"
    
    output = []
    for digit in str(num).strip("-"):      # if number is negative (ex : -1), remove the '-' sign
        if int(digit)%2 != 0:              # odd number    
            to_append = "-{}-".format(digit)
            output.append(to_append)
        else: 
            output.append(digit)
            
    output_string = ''.join(output)
    output_string = output_string.strip("-")
    if "--" in output_string: 
        return output_string.replace("--", "-")
    return output_string
