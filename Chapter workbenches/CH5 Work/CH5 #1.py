def kilometer_to_miles(km):
    miles = km * 0.6214
    return miles

def main():
    km = float(input("Enter distance in kilometers: "))
    miles = kilometer_to_miles(km)
    print(f"{km} kilometers is equal to {miles} miles.")

main()
