def grapevines():
    R = float(input("Length of the row:"))
    E = float(input("The amount of space used by an end-post assembly: "))
    S = float(input("The amount of space between the vines:"))
    V = (R - 2 * E)// S
    print ("number of grapevinew that will fit in the row: ", V)
    
grapevines()