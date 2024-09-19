def Software_sales():
    price = 99
    discount = 0
    quantity = int(input("Enter Quantity: "))
    if 10 <= quantity <= 19:
        discount = 0.10
    elif 20 <= quantity <= 49:
        discount = 0.20
    elif 50 <= quantity <= 99:
        discount = 0.30
    elif quantity >= 100:
        discount = 0.40
        
    discount_amount = quantity * price * discount
    total_cost = quantity * price - discount_amount
    print("total cost is", total_cost)
        
Software_sales()