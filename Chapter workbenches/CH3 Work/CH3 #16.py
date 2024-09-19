def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0

def main():
    year = int(input("Enter a year: "))

    if is_leap_year(year):
        print("In", year, "February has 29 days.")
    else:
        print("In", year, "February has 28 days.")

main()
