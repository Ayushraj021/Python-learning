#lex_auth_012693813706604544157
def is_sum_of_digits_multiple_of_3(num):
    """Check if the sum of digits of num is a multiple of 3."""
    return sum(int(digit) for digit in str(num)) % 3 == 0
    
def find_max(num1, num2):
    max_num=-1
    
    valid_numbers = []

    for number in range(num1, num2 + 1):
        if 10 <= number <= 99 and number % 5 == 0 and is_sum_of_digits_multiple_of_3(number):
            valid_numbers.append(number)

    if valid_numbers:
        return max(valid_numbers)
    else:
        return -1  # No valid numbers found
    # Write your logic here
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)

