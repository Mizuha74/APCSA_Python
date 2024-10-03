def multiply(x, y):
    if x == 1:
        return y
    else:
        return y + multiply(x - 1, y)


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
result = multiply(x, y)
print(f"The result of {x} times {y} is: {result}")
