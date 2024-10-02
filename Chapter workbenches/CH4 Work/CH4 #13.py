starting_population = int(input("Enter the starting number of organism: "))
daily_increase_percent = float(input("enter the average daily increase (as a percentage): "))
days = int(input("Enter the number of days the organisms will multiply: "))


daily_increase_rate = daily_increase_percent / 100

print("Day\tApproximate Population")
print("------------------------------------------")

current_population = starting_population


for day in range(1, days + 1):
    print(f"{day}\t{int(current_population)}")
    current_population += current_population * daily_increase_rate
