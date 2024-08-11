#lex_auth_012693763253788672132

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    start_number = 101
    
    for i in range(no_of_passengers):
        ticket_number = f"{airline}:{source[:3]}:{destination[:3]}:{start_number + i}"
        ticket_number_list.append(ticket_number)

    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))