def is_leap_year(year):
    if year % 400 == 0:
        return "YES"
    if year % 100 == 0:
        return "NO"
    if year % 4 == 0:
        return "YES"
    return "NO"

year = int(input())
print(is_leap_year(year))
