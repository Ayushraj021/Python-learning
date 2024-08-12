def sms_encoding(data):
    vowels = 'AEIOUaeiou'

    def encode_word(word):
        # Retain word as is if it contains only vowels
        if all(char in vowels for char in word):
            return word
        # Otherwise, retain only consonants
        return ''.join(char for char in word if char not in vowels)

    # Split the sentence into words
    words = data.split()
    # Encode each word
    encoded_words = [encode_word(word) for word in words]
    # Join the encoded words back into a sentence
    return ' '.join(encoded_words)

# Sample input
data = "I love Python"
print(sms_encoding(data))  # Expected Output: I lv Pythn
