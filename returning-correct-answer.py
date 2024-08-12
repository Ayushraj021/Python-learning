def find_correct(word_dict):
    def compute_error_count(correct, given):
        # If lengths differ, return an error count based on length mismatch
        if len(correct) != len(given):
            return max(len(correct), len(given))
        
        # Count the number of incorrect letters
        return sum(1 for c, g in zip(correct, given) if c != g)
    
    correct_count = 0
    almost_correct_count = 0
    wrong_count = 0

    for correct, given in word_dict.items():
        error_count = compute_error_count(correct, given)
        
        if error_count == 0:
            correct_count += 1
        elif error_count <= 2:
            almost_correct_count += 1
        else:
            wrong_count += 1
    
    return [correct_count, almost_correct_count, wrong_count]

# Sample input
word_dict = {"THEIR": "THEIR", "BUSINESS": "BISINESS", "WINDOWS": "WINDMILL", "WERE": "WEAR", "SAMPLE": "SAMPLE"}
# Find and print the results
print(find_correct(word_dict))
