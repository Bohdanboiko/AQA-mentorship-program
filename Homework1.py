leap_years = [year for year in range(1901, 2001) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
leap_years_tuple = tuple(leap_years)
print(leap_years_tuple)
