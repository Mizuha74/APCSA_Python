def calculate_grade(test1, test2, exam):
    if test1 < 0 or test1 > 25 or test2 < 0 or test2 > 25 or exam < 0 or exam > 50:
        return "Error."

    total_score = test1 + test2 + exam
    
    if total_score < 50 or exam < 25:
        return "Total Points:" , total_score , "Fail"

    if total_score > 80:
        return "Total Points:" , total_score , "GGrade: Distinction"
    elif total_score > 60:
        return "Total Points:" , total_score , "Grade: Credit"
    elif total_score < 60:
        return "Total Points:" , total_score , "Grade: Pass"


def main():
    test1 = int(input("Enter the score for Test 1: "))
    test2 = int(input("Enter the score for Test 2: "))
    exam = int(input("Enter the score for the main exam: "))

    result = calculate_grade(test1, test2, exam)
    print(result)

main()
