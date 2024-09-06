#Calculate BMI which means ask for height and weight to calculate
#8/30/2024

def bmi():
    
    a=1
    
    while a > 0:
        print('This program will compute BMI.')
    
        height = float(input('Please enter your height in meters: '))
        mass = float(input('Please enter your weight in kilogrames: '))
    
        #compute and display BMI
        BMI = (mass/ height **2)
        BMI = int(BMI *100)/ 100 #keep only two decimal
        print('Your BMI is', BMI, 'with a weight of',mass, 'kg, and a height of',height, 'm')
    
    
        if BMI >=30:
            print('obese')
        else:
            if BMI >=25:
                print('overweight')
            else:
                if BMI >=18.5:
                    print('healthy')
                else:
                    print('underweight')
                    
        a = int(input('Continue? Press 0 for NO, and 1 for yes'))

    
 

bmi()
