def is_isogram(string):

    count  = [string.lower().count(x) for x in string.lower()]
    if len(count)!=0 and max(count)>1:
        return False
    return True