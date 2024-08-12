def encode(message):
    if not message:
        return ""
    
    encoded_message = ""
    count = 1
    length = len(message)
    
    for i in range(1, length):
        if message[i] == message[i - 1]:
            count += 1
        else:
            encoded_message += message[i - 1] + str(count)
            count = 1
    
    # Append the last character and its count
    encoded_message += message[-1] + str(count)
    
    return encoded_message

# Provide different values for message and test your program
encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)
