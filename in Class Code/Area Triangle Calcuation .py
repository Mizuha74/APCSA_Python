
def triangle_area(a,b,c):
    # area of triangle calculation
    print ("Triangle Area Calculator")



    s = (a+b+c)/2

    A = (s*(s-a)*(s-b)*(s-c))**0.5

    print (A)

def main():
    a = float (input('Value of side a:'))
    b = float (input('Value of side b:'))
    c = float (input('Value of side c:'))
    triangle_area(a,b,c)
    triangle_area(5,12,13)
    
main()
