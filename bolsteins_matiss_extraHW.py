def get_city_year(p0, perc, delta, p):
    years = 0 # initial year counter
    # loop until the population (p0) reaches the target population(p)
    while p0 < p:
        # calculation including perc converted to a decimal number
        p0 += p0 * (perc / 100) + delta
        years += 1 
        # need to specify when to stop thw loop – when population cannot reach the target
        if years > 9999: 
            return -1
    return years

print(get_city_year (1000, 2, -50, 5000))
print(get_city_year (1500, 5, 100, 5000))
print(get_city_year (1500000, 2.5, 10000, 2000000))