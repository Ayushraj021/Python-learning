#lex_auth_01273338869591244855
count=0
i=1
for baggage_weight in 29, 30, 31, 32, 28:
    if( baggage_weight <=30):
        print("Passenger",i,": Proceed for baggage check.")
    else:
        count+=1
        print("Passenger",i,": Maximum baggage weight allowed is 30kg.")
    i+=1

print("No. of passengers who cleared baggage check:", count)