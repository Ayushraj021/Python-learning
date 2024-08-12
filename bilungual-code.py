def translate(bilingual_dict, english_words_list):
    # Translate each word in the list using the bilingual dictionary
    swedish_words_list = [bilingual_dict.get(word, word) for word in english_words_list]
    return swedish_words_list

# Define the bilingual dictionary
bilingual_dict = {
    "merry": "god",
    "christmas": "jul",
    "and": "och",
    "happy": "gott",
    "new": "nytt",
    "year": "ar"
}

# Define the list of English words to translate
english_words_list = ["merry", "christmas"]

print("The bilingual dict is:", bilingual_dict)
print("The English words are:", english_words_list)

# Get the Swedish translation
swedish_words_list = translate(bilingual_dict, english_words_list)
print("The equivalent Swedish words are:", swedish_words_list)
