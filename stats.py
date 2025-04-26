def get_words_number(book_text):
    return len(book_text.split())

def count_characters(book_text):
    book_text = book_text.lower()
    characters = {}

    for char in book_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    
    return characters

def sort_key(dict):
    return dict["num"]

def sort_characters(characters):
    characters_list = []
    
    for char in characters:
        if char.isalpha():
            characters_list.append({
                "char": char,
                "num": characters[char]
            })

    characters_list.sort(key=sort_key, reverse=True)
    return characters_list