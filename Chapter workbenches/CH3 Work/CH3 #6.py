#CH3 #6Magic Date
def is_magic_date(month, day, year):
    if month * day == year:
        return True
    else:
        return False


def main():
    month = int(input("Enter the month as of numbers: "))
    day = int(input("Enter the day: "))
    year = int(input("Enter the two digit year: "))

    if is_magic_date(month, day, year):
        print("The date is magic!")
    else:
        print("The date is not magic.")

main()
