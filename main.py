from stats import count_words

def get_book_text(filepath):
    """Reads the contents of the file and returns it as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        contents = file.read()
    return contents

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = count_words(text)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()
