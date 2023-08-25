leap_years_dict = {'leap': [], 'not leap': []}

for year in range(1901, 2001):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap_years_dict['leap'].append(year)
    else:
        leap_years_dict['not leap'].append(year)

print(leap_years_dict)

