def make_readable(seconds):
    
	# Given time in seconds, convert it to "hh:mm:ss"
	
    time = "{:02}:{:02}:{:02}".format(seconds//3600, seconds/60 %60, seconds%60)
    return time