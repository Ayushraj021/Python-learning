#lex_auth_01269441913243238467
from functools import cmp_to_key

def compare(x, y):
    # Custom comparator function to decide the order
    if x + y > y + x:
        return -1
    elif x + y < y + x:
        return 1
    else:
        return 0
        
def create_largest_number(number_list):
   # Convert all numbers to strings
    number_list_str = list(map(str, number_list))
    
    # Sort the numbers based on the custom comparator
    sorted_numbers = sorted(number_list_str, key=cmp_to_key(compare))
    
    # Join the sorted list into a single string
    largest_number = ''.join(sorted_numbers)
    
    # Convert the result to an integer and return
    return int(largest_number)

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)