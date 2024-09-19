#APCSA LAB #2 Karatsuba Multiplication
#File: Karatsuba.py
#Student: Eddy Z.
#
#Date:9/16
#Description of Program: To calculate four digit number multiply four digit number

def multiply():
    n1 = int(input("Enter a 4-digit numebr: "))
    n2 = int(input("Enter another 4-digit numebr: "))
    a = n1 // 100
    b = n1 % 100
    c = n2 // 100
    d = n2 % 100
    e = a * c
    f = b * d
    g = (a + b) * (c + d)
    h = g - (e + f)
    i = e * (10 ** 4)
    j = h * (10 ** 2)
    k = i + j + f
    ans = n1 * n2
    print ("Computed product: ", k)
    print ("Expected product: ", ans)
    
    

multiply()