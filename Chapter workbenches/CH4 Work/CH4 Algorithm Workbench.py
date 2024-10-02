#Algorithm Workbench

#1
product = 0
while product < 100:
    number = float(input("Enter a number: ")) #if the user enter 0 or less than it still carries on the calculation
    product = number * 10
    print("Product: ", product) 

#2
repeat = "yes"
while repeat.lower() == "yes":
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    total = number1 + number2
    print("The sum is: ", total)
    repeat = input("would you like to perform the operation again?: (yes or no) ")

#3
for number in range(1, 101):
    if number % 2 != 0:
        print(number)

#5
total = 0
for numerator in range(1, 31):
    denominator = 31 - numerator
    total += numerator / denominator

print("The total of the series is: " total)
