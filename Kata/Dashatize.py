def dashatize(num):
    
    # Given a number, return a string with dash'-'marks before
    # and after each odd integer, but do not begin or end 
    # the string with a dash mark.
    #
    
    output = []
    if "None" in str(num):
        return "None"
    
    for digit in str(num).strip("-"):
        if int(digit)%2 != 0:   #odd number    
            to_append = "-{}-".format(digit)
            output.append(to_append)
        else: 
            output.append(digit)
            
    output_string = ''.join(output)
    output_string = output_string.strip("-")
    if "--" in output_string: 
        return output_string.replace("--", "-")
    return output_string