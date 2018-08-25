def find_short(s):

    words = s.split(" ")
    smallest = min([len(word) for word in words if len(word)<=len(words[0])])
    return smallest #shortest word length
