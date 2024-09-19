#Lab #3 Length Conversion
#Files: ConvertUnits.py
#Student: Eddy
#Date:9/18


def ConvertingUnits():
    inputfeet = int(input("Enter number of feet: "))
    inputinches= int(input("Enter number of inches: "))
    
    inches = (inputfeet * 12)+inputinches
    print ("inches: ", inches)
    
    feet = (inches/12)
    print ("feet: ", feet)
    
    yards = feet/3
    print ("yards ", yards)
    
    miles = feet / 5280
    print ("miles: ", miles)
    
    meters = feet * 0.3048
    print ("meters: ", meters)
    
    centimeters = meters * 100
    print("centimeters: ", centimeters)
    
    millimeters = centimeters * 10
    print("millimeters: " , millimeters)
    
    kilometers = meters / 1000
    print("kilometers: ", kilometers)
    
    
    
ConvertingUnits()