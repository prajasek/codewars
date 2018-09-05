def street_fighter_selection(fighters, initial_position, moves):
    
    # Given a grid of characters in the Street Fighter game 
    #  ________________________
    #  | A | B | C | D......   |
    #  | A1| B1| C1| D1 .....  |
    #  -------------------------
    # in the form of a list, fighters =[[A,B,C...], [A1, B1,C1..]]
    # The 'initial_position' is (0,0) corresponding to 
    # fighters[0][0]. Given a list of key strokes ["Up","Down"..]
    # output all the characters hovered over by the keystrokes.
    # 
    # Left and Right movements are circular (loops back to 1st element
    # if you go right from the last element and vice-versa if you go
    # left).
    #
    # Up and Down movements are not circular. If you go up from the 
    # first row, you stay at the same place, and same for the bottom 
    # row.
    
    selected_fighters= []
    position  = list(initial_position)
    
    for move in moves:
        if "up" in move and position[1]==1:            
                position[1]=0
        elif "down" in move and position[1]==0:
                position[1]=1     
        elif "left" in move:
                position[0] = (position[0]-1) % len(fighters[0])
        elif "right" in move:
                position[0] = (position[0]+1) % len(fighters[0])
    
        x, y = position[0], position[1]
        
        fighter = fighters[y][x]
        selected_fighters.append(fighter)
    return selected_fighters
        
