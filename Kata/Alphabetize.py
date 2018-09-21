def alphabet_position(text):
    
    # Replace each letter with their position in the alphabet
    # if not an alphabet, then ignore
    # 
    # Input    : "abcdz"
    # Output   :  "1 2 3 4 26"
	
    return_string = [str(ord(letter.lower())-96) for letter in text if 1<=ord(letter.lower())-96<=26]
    
    return " ".join(return_string)
