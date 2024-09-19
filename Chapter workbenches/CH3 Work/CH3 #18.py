def restaurant_selector(vegetarian, vegan, gluten_free):
    print("Here are your restaurant choices:")

    if vegetarian == 0 and vegan == 0 and gluten_free == 0:
        print("Joe's Gourmet Burgers")

    if vegetarian == 1 and vegan == 0 and gluten_free == 1:
        print("Main Street Pizza Company")

    if vegetarian == 1 and vegan == 1 and gluten_free == 1:
        print("Corner Café")
        print("The Chef's Kitchen")

    if vegetarian == 1 and vegan == 0 and gluten_free == 0:
        print("Mama's Fine Italian")

    if vegetarian == 1 and vegan == 1 and gluten_free == 1:
        print("The Chef's Kitchen")

def main():
    vegetarian = int(input("Is anyone in your party a vegetarian? (1 for yes, 0 for no): "))
    vegan = int(input("Is anyone in your party a vegan? (1 for yes, 0 for no): "))
    gluten_free = int(input("Is anyone in your party gluten-free? (1 for yes, 0 for no): "))

    restaurant_selector(vegetarian, vegan, gluten_free)

main()
