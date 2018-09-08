def domain_name(url):

    if "https" in url: 
        link =url.strip("https://")
    else:
        link = url.strip("http://")
    dots = link.count(".")
    
    print(link)
    if dots==1:
        return link.split(".")[0]
    return link.split(".")[1]


#def domain_name(url):
#  
#   try:
#       return url.split("www.")[1].split(".")[0]
#   except:
#       return url.split("//")[1].split(".")[0]
