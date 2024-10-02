years = int(input("Enter the number of years: "))


total_rainfall = 0.0

for year in range(1, years + 1):
    print(f"\nYear {year}")
    
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
        
        total_rainfall += rainfall

average_rainfall = total_rainfall / 12


print("Total months: 12 " )
print("Total inches of rainfall:", total_rainfall)
print(f"Average rainfall per month: {average_rainfall} inches")
