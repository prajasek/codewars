def find_short(s):
    # Find the shortest length of words in a sentence
    # Example, "What is the time"  will give output 
    # 2 since "is" has the shortest length 2
    
    words = s.split(" ")
    shortest = min([len(word) for word in words])
    return shortest #shortest word length
