#1 Number Analyser
def Num():
    n = int(input("Enter an integer"))
    if n > 0:
        print ("Positive")
    else:
        if n < 0:
            print ("Negative")
        else:
            print ("Zero")
            
    r = (n % 2)
    if r == 1:
        print ("Odd")
    else:
        print ("Even")
            
Num()