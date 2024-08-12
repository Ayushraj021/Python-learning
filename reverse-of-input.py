def encrypt_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Helper function to rearrange consonants and vowels
    def rearrange_word(word):
        consonants = ''.join([ch for ch in word if ch not in 'aeiouAEIOU'])
        vowels = ''.join([ch for ch in word if ch in 'aeiouAEIOU'])
        return consonants + vowels

    # Process each word based on its position
    encrypted_words = [
        rearrange_word(words[i]) if (i + 1) % 2 == 0 else words[i][::-1]
        for i in range(len(words))
    ]

    # Join the encrypted words into a single string
    return ' '.join(encrypted_words)

# Sample input
sentence = "The sun rises in the east"
# Encrypt and print the result
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)
