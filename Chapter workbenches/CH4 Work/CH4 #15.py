
rows = int(input("Enter the number of rows: "))


for i in range(rows):
    print("#", end="")
    for j in range(i):
        print(" ", end="")
    print("#")
