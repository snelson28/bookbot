from stats import count_words, count_characters

def get_book_text(filepath):
    """Reads the contents of the file and returns it as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        contents = file.read()
    return contents

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    
    #count_words
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    #Count characters
    char_counts = count_characters(text)
    print(char_counts)

if __name__ == "__main__":
    main()
