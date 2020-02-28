def nb_year(p0, percent, aug, p):
    # nb_year returns the number of years needed to reach population 'p' 
    # starting from population 'p0'
    # 
    # 'p0'      - Initial population
    # 'percent' - percentage growth in population per year
    # 'aug'     - increase/decrease in population per year (added or subtracted) 
    # 'p'       - Threshold of population to reach
    
    number_of_years = 0            
    while p0<p:
        p0 = p0 + p0*percent/100 + aug
        number_of_years = number_of_years + 1
    return int(number_of_years)
    
