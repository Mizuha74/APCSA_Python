days = int(input("Enter the number of days: "))


total_pay_pennies = 0
current_day_pay_pennies = 1  

print("\nDay\tSalary (Dollars)")
print("-------------------------")


for day in range(1, days + 1):
    current_day_pay_dollars = current_day_pay_pennies / 100
    print(f"{day}\t{current_day_pay_dollars:.2f}")
    

    total_pay_pennies += current_day_pay_pennies
    current_day_pay_pennies *= 2


total_pay_dollars = total_pay_pennies / 100

print(f"\nTotal pay over {days} days: ${total_pay_dollars:.2f}")
