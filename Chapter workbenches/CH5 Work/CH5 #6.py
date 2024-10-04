def calories_from_fat(fat_grams):
    return fat_grams * 9

def calories_from_carbs(carb_grams):
    return carb_grams * 4


def main():
    fat_grams = float(input("Enter the number of fat grams consumed: "))
    carb_grams = float(input("Enter the number of carbohydrate grams consumed: "))
    

    fat_calories = calories_from_fat(fat_grams)
    carb_calories = calories_from_carbs(carb_grams)
    
    print(f"Calories from Fat: {fat_calories}")
    print(f"Calories from Carbohydrates: {carb_calories}")


main()
