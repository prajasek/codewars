def likes(names):
    #your code here
    
    if len(names)>3:
       return ", ".join(names[0:2]) +" and " + str(len(names)-2) +" others like this"
    elif len(names)==3:
       return ", ".join(names[0:2]) +" and " + names[-1]+ " like this"
    elif len(names)==2:
       return " and ".join(names) + " like this"
    elif len(names)==1:
       return names[0] + " likes this"
    else:
        return "no one likes this"