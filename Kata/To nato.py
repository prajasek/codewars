def to_nato(words):
    
    # Translate a string to Pilot's alphabet(NATO phonetic alphabet).   
    # Each alphabet in the input string will be the starting alphabet
    # of the NATO code words.
    # 
    # Input: "If you can read"
    # 
    # Output: 
    # "India Foxtrot Yankee Oscar Uniform Charlie Alfa 
    # November Romeo Echo Alfa Delta"
    
     
    nato_string = """Alfa, Bravo, Charlie, Delta, Echo, \
    Foxtrot, Golf, Hotel, India, Juliett, Kilo,\
    Lima, Mike, November, Oscar, Papa, Quebec, Romeo, \
    Sierra, Tango, Uniform, Victor, Whiskey, \
    Xray, Yankee, Zulu"""
    
    # get the words from the string I copied from wikipedia (above), since I am too lazy 
    # to type the whole set of words.
    nato = [word.strip() for word in nato_string.split(", ")]
    
    # nato = ["Alfa", "Bravo", ...., "Zulu"]
	
    output_string = []
    for letter in words:
        unicode= ord(letter.lower())-97                    # 0-25 for a-z
        if 0<=unicode<26:    
            output_string.append(nato[unicode])
        elif ord(letter)!=32:				   # unicode 32 is for whitespace (" ")
            output_string.append(letter)
			
    return " ".join(output_string)
