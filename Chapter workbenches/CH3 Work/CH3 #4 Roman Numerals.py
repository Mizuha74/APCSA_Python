#4 Roman Numerals
def RomanNum():
    n = int(input("Enter a number from 1 to 10: "))
    if n == 1:
        print("I")
    else:
        if n == 2:
            print("II")
        else:
            if n == 3:
                print("III")
            else:
                if n == 4:
                    print("IV")
                else:
                    if n == 5:
                        print("V")
                    else:
                        if n == 6:
                            print("VI")
                        else:
                            if n == 7:
                                print("VII")
                            else:    
                                if n == 8:
                                    print("VIII")
                                else:
                                    if n == 9:
                                        print("IX")
                                    else:
                                        if n == 10:
                                            print("X")
                                        else:
                                            print ("Error")
                        
RomanNum()