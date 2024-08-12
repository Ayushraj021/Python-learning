#lex_auth_012693819159732224162

def check_palindrome(word):
     # Convert the word to lowercase to ensure case-insensitive comparison
    cleaned_word = word.lower()
      # Compare the cleaned word with its reverse
    return cleaned_word == cleaned_word[::-1]

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")