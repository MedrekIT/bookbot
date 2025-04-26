import sys
from stats import get_words_number, count_characters, sort_characters, sort_key

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_words_number(book_text)} total words")
    print("--------- Character Count -------")
    characters_count = count_characters(book_text)
    characters_list = sort_characters(characters_count)
    for char in characters_list:
        print(f"{char["char"]}: {char["num"]}")