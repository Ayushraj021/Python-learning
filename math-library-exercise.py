def find_number_of_combination(number_of_flavours):
    # Calculate the total number of different ways to have coffee
    total_combination = 2 ** number_of_flavours
    return total_combination

# Provide different values for number_of_flavours and test your program
number_of_flavour = 6
number_of_combination = find_number_of_combination(number_of_flavour)
print(number_of_combination)
