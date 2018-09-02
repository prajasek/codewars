def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    root = sq**0.5
    if int(root)**2 == sq:
        return (root+1)**2
    
    return -1