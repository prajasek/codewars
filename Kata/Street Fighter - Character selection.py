def street_fighter_selection(fighters, initial_position, moves):
    
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
        