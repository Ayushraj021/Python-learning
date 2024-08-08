#lex_auth_012693810762121216155

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
    if legs % 2 != 0 or heads > legs // 2 or heads * 4 < legs:
        print(error_msg)
        return
    
    
    # Calculate the number of rabbits
    rabbit_count = (legs - 2 * heads) // 2
    # Calculate the number of chickens
    chicken_count = heads - rabbit_count

    # Check if the solution is valid
    if chicken_count < 0 or rabbit_count < 0:
        print(error_msg)
    else:
        print(chicken_count, rabbit_count)


#Provide different values for heads and legs and test your program
solve(38,131)