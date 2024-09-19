def get_roulette_color(pocket):
    if pocket < 0 or pocket > 36:
        return "Error"
    elif pocket == 0:
        return "Pocket 0 is green."
    elif 1 <= pocket <= 10:
        if pocket % 2 == 0:
            return "Pocket is black."
        else:
            return "Pocket is red."
    elif 11 <= pocket <= 18:
        if pocket % 2 == 0:
            return "Pocket is red."
        else:
            return "Pocket is black."
    elif 19 <= pocket <= 28:
        if pocket % 2 == 0:
            return "Pocket is black."
        else:
            return "Pocket is red."
    elif 29 <= pocket <= 36:
        if pocket % 2 == 0:
            return "Pocket is red."
        else:
            return "Pocket is black."


def main():
    pocket = int(input("Enter a pocket number: "))
    result = get_roulette_color(pocket)
    print(result)


main()
