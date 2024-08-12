def max_frequency_word_counter(data):
    import string
    from collections import Counter

    # Normalize the text to lowercase
    data = data.lower()
    
    # Remove punctuation (for simplicity, only commas are considered as per the sample input)
    data = data.translate(str.maketrans('', '', string.punctuation))
    
    # Split the text into words
    words = data.split()
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Initialize variables to track the word with the highest frequency
    word = ""
    frequency = 0
    
    # Iterate over the word count dictionary to find the desired word
    for w, freq in word_count.items():
        # Update the word and frequency based on the conditions
        if (freq > frequency) or (freq == frequency and len(w) > len(word)):
            word = w
            frequency = freq

    # Print the result (do not modify this line for verification purposes)
    print(word, frequency)

# Test the function with different values for data
data = "Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)  # Expected Output: like 3
