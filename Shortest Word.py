def find_short(s):
    # your code here
    words = s.split(" ")
    smallest = min([len(word) for word in words if len(word)<=len(words[0])])
    return smallest # l: shortest word length