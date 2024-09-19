import math

def cookout_calculator(people, hot_dogs_per_person):
    
    HOT_DOGS_PER_PACKAGE = 10
    BUNS_PER_PACKAGE = 8

    total_hot_dogs_needed = people * hot_dogs_per_person

    hot_dog_packages = math.ceil(total_hot_dogs_needed / HOT_DOGS_PER_PACKAGE)
    bun_packages = math.ceil(total_hot_dogs_needed / BUNS_PER_PACKAGE)


    hot_dogs_leftover = (hot_dog_packages * HOT_DOGS_PER_PACKAGE) - total_hot_dogs_needed
    buns_leftover = (bun_packages * BUNS_PER_PACKAGE) - total_hot_dogs_needed


    print("Minimum number of hot dog packages required: ", hot_dog_packages)
    print(f"Minimum number of hot dog bun packages required: ", bun_packages)
    print(f"Hot dogs left over: " , hot_dogs_leftover)
    print(f"Buns left over: " , buns_leftover)


def main():
    people = int(input("Enter the number of people attending the cookout: "))
    hot_dogs_per_person = int(input("Enter the number of hot dogs each person will get: "))
    cookout_calculator(people, hot_dogs_per_person)


main()
