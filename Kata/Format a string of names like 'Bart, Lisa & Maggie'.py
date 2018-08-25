def namelist(names):
    name = []

    if len(names)>2:
        for items in range(0,len(names)-1):
            name.append(names[items]["name"])
        a = ", ".join(name)
        return a + " & " + names[len(names)-1]["name"]
    
    elif len(names)==2:
        for items in names:
            name.append(items["name"])
        return " & ".join(name)
    
    elif len(names)==1:
        return names[0]["name"]
    
    else:
        return ''
        
