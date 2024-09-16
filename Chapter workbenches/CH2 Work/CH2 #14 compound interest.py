#14
def compound():
    P = float(input("The amount of principal originally deposited into the account:"))
    r = float(input("The annual interest rate paid by the account: "))
    n = float(input("The number of times per year that the interest is compounded: "))
    t = float(input("The number of years the account will be left to earn interest: "))
    A = P * ((1 + r//n) ** (n*t))
    print ("amount of money is ", A)
    
compound();
