
tuition = 8000.00
increase_rate = 0.03


print("Year\tProjected Tuition (per semester)")
print("--------------------------------------------------------")


for year in range(1, 6):
    tuition += tuition * increase_rate
    print(f"{year}\t${tuition:.2f}")
