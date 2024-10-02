
speed = float(input("What is the speed of the vehicle in mph? "))
hours = int(input("How many hours has it traveled? "))


print("\nHour\tDistance Traveled")    
print("-------------------------")


for hour in range(1, hours + 1):   
    distance = speed * hour
    print(f"{hour}\t\t{distance:.2f}")    #couldn't figure out how to do formate properly D:
                                          # \n is enter/new line
                                          # \t is tab
                                          # {} is variable inside expression
                                          # :.2f is the number of decimals which in this case is two
