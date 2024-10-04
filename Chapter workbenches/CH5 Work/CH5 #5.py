def assessment_value(actual_value):
    return actual_value * 0.60

def tax(value):
    return (value / 100) * 0.72


def main():
    actual_value = float(input("Enter the actual value of the property: "))
    assess_value = assessment_value(actual_value)
    property_tax = tax(assess_value)
    
    print(f"Assessment value: ${assess_value}")
    print(f"Property tax: ${property_tax}")

main()
