def alphabet_position(text):
    
    return_string = 
	[str(ord(letter.lower())-96) for letter in text if 1<=ord(letter.lower())-96<=26]
    
    return " ".join(return_string)