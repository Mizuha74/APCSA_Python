#did we go over list?
def main():
    List = []
    num_elements = int(input("How many elements do you want?: "))
    
    for i in range(num_elements):
        value = int(input(f"Enter element {i+1}: "))
        List.append(value)
        
    largest_value = bigg(List)
    print(largest_value)
    
def bigg(list):
    if len(list) == 1:
        return list[0]
    else:
        largest = bigg(list[1:])
        if list[0] > largest :
            return list[0]
        else:
            return largest
    
        


main()
                       