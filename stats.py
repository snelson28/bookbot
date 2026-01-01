def count_words(text):
    """Returns the number of words in a given text string."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Returns a dictionary mapping each character to the number of times it appears (case-insensitive)."""
    text = text.lower() #Normalize to lowercase
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts