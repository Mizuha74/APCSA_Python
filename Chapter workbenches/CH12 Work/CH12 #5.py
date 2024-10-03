List = []
num_elements = int(input("How many elements do you want?: "))

for i in range(num_elements):
    value = int(input(f"Enter element {i+1}: "))
    List.append(value)


def sum(lst):
    if len(lst) == 0: 
        return 0
    else:
        return lst[0] + sum(lst[1:]) 


total_sum = sum(List)
print(f"The sum of the elements in the list is: {total_sum}")
