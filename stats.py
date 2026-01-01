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

def sort_characters(char_dict):
    chars_list = []

    for char, count in char_dict.items():
        chars_list.append({"char": char, "num": count})

    def sort_on(d):
        return d["num"]

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list