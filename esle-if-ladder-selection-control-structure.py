luggage_weight=30
weight_limit=30  #Weight limit for the airline
extra_luggage_charge=0
if(luggage_weight>0 and luggage_weight<=weight_limit):
    print("Check-in cleared")
elif(luggage_weight<=(weight_limit+10)):
    extra_luggage_charge=300*(luggage_weight-weight_limit)
else:
    extra_luggage_charge=500*(luggage_weight-weight_limit)
if(extra_luggage_charge>0):
    print("Extra luggage charge is Rs.", extra_luggage_charge)
    print("Please make the payment to clear check-in")
