def nb_year(p0, percent, aug, p):
    # your code
    year=0
    while p0<p:
        p0 = p0 + p0*percent/100 + aug
        year=year+1
    return int(year)
    