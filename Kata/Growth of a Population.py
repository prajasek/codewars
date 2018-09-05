def nb_year(p0, percent, aug, p):
    # nb_year returns the number of years needed to reach population 'p' 
    # starting from population 'p0'
    # 
    # 'p0'      - Initial population
    # 'percent' - percentage growth in population per year
    # 'aug'     - increase/decrease in population per year (added or subtracted) 
    # 'p'       - Threshold of population to reach
    
    year=0            # keep count of number of years
    while p0<p:
        p0 = p0 + p0*percent/100 + aug
        year=year+1
    return int(year)
    
