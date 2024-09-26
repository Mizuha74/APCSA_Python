#File:Compute Taxes.py
#Student: Eddy
#
#9/25
import math as math

def main():
    print("Welcome to our friendly tax computing program.")
    print("Please Follow the directions")
    print(" ")
    s = "s"
    m = 'm'
    status = 0
    martial_status = input("Enter your marital status(s or m):")
    if (martial_status == s )or (martial_status == m):
        tax = float(input("Enter your taxable income: "))
        if tax >= 0:
            if martial_status == s:
                status = 1
            else:
                status = 2
            taxcalculation(tax,status)
        else:
            print("Negative income reported! Try again later.")
    else:
        print("Wrong marital status! Try again later")

def taxcalculation(t,s):
    print (" ")
    if s == 1:
        if t <= 8000:
            taxed= t * 0.1
        if t <= 32000:
            taxed = (t-8000)*0.15+800
        if t > 32000:
            taxed = (t-32000)*0.25+4400
        print("Marital status:Single")
        print("Taxable income: $", format(t,".2f"))
        print("Taxes owned: $",format(taxed,".2f"))
    else:
        if t <= 16000:
            taxed= t * 0.1
        if t <= 64000:
            taxed = (t-16000)*0.15+1600
        if t > 64000:
            taxed = (t-64000)*0.25+8800
        print("Marital status:Married")
        print("Taxable income: $", format(t,".2f"))
        print("Taxes owned: $",format(taxed,".2f"))
main()