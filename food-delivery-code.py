#lex_auth_012693782475948032141

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if (food_type not in ['V', 'N']) or (quantity_ordered < 1) or (distance_in_kms <= 0):
        return -1
        
    if food_type == 'V':
        cost_per_plate = 120
    elif food_type == 'N':
        cost_per_plate = 150

    # Calculate food cost
    food_cost = cost_per_plate * quantity_ordered

    # Calculate delivery charge
    if distance_in_kms <= 3:
        delivery_charge = 0
    elif distance_in_kms <= 6:
        delivery_charge = (distance_in_kms - 3) * 3
    else:
        delivery_charge = 3 * 3 + (distance_in_kms - 6) * 6
         # Calculate total bill amount
    bill_amount = food_cost + delivery_charge
   
  
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)