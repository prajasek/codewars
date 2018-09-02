def likes(names):
    # Simulating the names next to Facebook like button. 
    #
    # One person :   "A likes this"
    # 2 people   :   "A and B like this"
    # 3 people   :   "A, B and C like this"
    # >3 people  :   "A,B and others like this"
    
    
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
