#lex_auth_012693788748742656146

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    #Start writing your code here
      # Validate account number
    if len(str(account_number)) != 4 or str(account_number)[0] != '1':
        print("Invalid account number")
        return

    # Validate account balance
    if account_balance < 100000:
        print("Insufficient account balance")
        return
    
    #Populate the variables: eligible_loan_amount and bank_emi_expected
    if salary > 75000 and loan_type == "Business":
        eligible_loan_amount = 7500000
        bank_emi_expected = 84
    elif salary > 50000 and loan_type == "House":
        eligible_loan_amount = 6000000
        bank_emi_expected = 60
    elif salary > 25000 and loan_type == "Car":
        eligible_loan_amount = 500000
        bank_emi_expected = 36
    else:
        print("Invalid loan type or salary")
        return


    if loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= bank_emi_expected:
        print("Account number:", account_number)
        print("The customer can avail the amount of Rs.", eligible_loan_amount)
        print("Eligible EMIs :", bank_emi_expected)
        print("Requested loan amount:", loan_amount_expected)
        print("Requested EMI's:", customer_emi_expected)
    else:
        print("The customer is not eligible for the loan")
       
     
        
#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)