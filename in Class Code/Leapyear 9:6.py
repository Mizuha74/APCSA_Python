def leapyear():
    i = int(input("Do you want to play a game? \n (0=yes,1-no!)"))
    
    while i!=0 and i!=1:
        i = int(input("Do you want to play a game? \n (0=yes,1-no!"))
        
    while i!=1:
        print("Type in a year and the program will determine")
        yr = int(input("if the year is a leap year:"))
        
        if (yr % 400 ==0) or (yr % 4 == 0 and yr % 100 !=0):
            print("LEAP YEAR!")
            print("YOU DID NOT LOSE THE GAME")
            
        else:
            print ("Not a leap year")
            
        i = int(input("Again? \n (0=yes,1-no!)"))
        
        
leapyear()
