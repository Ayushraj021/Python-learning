def find_common_characters(msg1, msg2):
    # Remove blank spaces from both strings
    msg1 = msg1.replace(' ', '')
    msg2 = msg2.replace(' ', '')

    # Convert strings to sets to find unique characters
    set1 = set(msg1)
    set2 = set(msg2)

    # Find common characters
    common_chars = set1.intersection(set2)

    # If there are no common characters, return -1
    if not common_chars:
        return -1

    # Sort common characters and return as a string
    return ''.join(sorted(common_chars))

# Provide different values for msg1 and msg2 and test your program
msg1 = "I like Python"
msg2 = "Java is a very popular language"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
