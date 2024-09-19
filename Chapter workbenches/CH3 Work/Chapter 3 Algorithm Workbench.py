#Chapter 3 Algorithm Workbench: 1, 3, 4, 5
#Chapter 3 Programming Exercises: 1, 4, 6, 7, 18
#Chapter 3 Programming Exercises: 8, 9, 12, 15, 16

#Algrotihm Workbench:
#1
def if_statement():
    if x > 100:
        y = 20
        z = 40

#3
def if_else_statement():
    if a < 10:
        b = 0
    else:
        b = 99
        
#4
def score_fix_statement():
    if score >= A_score:
        print('Your grade is A.')
    else:
        if score >= B_score:
            print('Your grade is B.')
        else:
            if score >= C_score:
                print('Your grade is C.')
            else:
                if score >= D_score:
                    print('Your grade is D.')
                else:
                    print('Your grade is F.')
    
#5
def nested_decision_structures():
    if (amount1 > 10 & amount2 <100):
        if amount1>amount2:
            print(amount1)
        elif amount2>amount1:
            print(amount2)