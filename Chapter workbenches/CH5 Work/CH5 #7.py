
A_Price = 20
B_Price = 15
C_Price = 10


def calculate_income(a_tickets, b_tickets, c_tickets):
    income_a = a_tickets * A_Price
    income_b = b_tickets * B_Price
    income_c = c_tickets * C_Price

    total_income = income_a + income_b + income_c
    return total_income


def main():
    a_tickets = int(input("Enter the number of Class A tickets sold: "))
    b_tickets = int(input("Enter the number of Class B tickets sold: "))
    c_tickets = int(input("Enter the number of Class C tickets sold: "))
    
    total_income = calculate_income(a_tickets, b_tickets, c_tickets)
    print(f"Total income generated from ticket sales: ${total_income}")


main()
