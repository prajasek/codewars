def race(v1, v2, g):
    
    # Two tortoises named A and B must run a race. 
    # A starts with an average speed of 720 feet per hour. 
    # B knows she runs faster than A. When she starts, 
    # she can see that A has a 70 feet lead but B's speed 
    # is 850 feet per hour. How long will it take B to catch A?
    #
    # v1 = speed of A (slower)
    # v2 = speed of B (faster)
    # g  = B's lead on A
    #
    # Equation:
    # d/v1 = (d+g)/v2
    # d*v2 = x*v1 + g*v1
    # d = g*v1 / v2-v1
    # time = x/v1    
    
    if v1>=v2 : return None
   
    distance = g*v1 / (v2-v1)
    time = distance / v1        # in hours

    hours = int(distance // v1)
    mins = int(time*60%60)
    secs = int(time*3600%60)

    return [hours,mins,secs]

    # 0.50000 returns [0, 30, 0]
