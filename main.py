import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    """Reads the contents of the file and returns it as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        contents = file.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    
    num_words = count_words(text)
    char_counts = count_characters(text)
    sorted_chars = sort_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item["char"]
        count = item["num"]
                     
        if not char.isalpha():
            continue

        print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
