#lex_auth_012693795044450304151

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
     # Create a dictionary for gem prices for quick lookup
    gem_price_dict = dict(zip(gems_list, price_list))
    bill_amount=0
    #Write your logic here
     # Check if all requested gems are available and calculate the total bill
    for gem, quantity in zip(reqd_gems, reqd_quantity):
        if gem not in gem_price_dict:
            return -1  # Gem not available, return -1
        
        bill_amount += gem_price_dict[gem] * quantity
    
    # Apply a 5% discount if the total bill amount is greater than Rs. 30,000
    if bill_amount > 30000:
        bill_amount *= 0.95
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)