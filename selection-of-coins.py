#lex_auth_012693780491968512136

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    #Start writing your code here
    five_needed = min(rupees_to_make // 5, no_of_five)
    remaining_amount = rupees_to_make - (five_needed * 5)
    if remaining_amount <= no_of_one:
        one_needed = remaining_amount
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)