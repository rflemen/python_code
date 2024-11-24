def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    if is_year_leap(year) and month == 2:
        days = 29
        return days
    elif not is_year_leap(year) and month == 2:
        days = 28
        return days
    else:
        days = 31 - ((month - 1) % 7 % 2)
        return days


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
