def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_chars(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    
    for item in char_count:
        char = item['char']
        if char.isalpha():
            print(f"The '{char}' character was found {item['num']} times")
    
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def count_chars(text):
    count = {}
    char_list = []
    for char in text:
        lowerchar = char.lower()
        if lowerchar not in count:
            count[lowerchar] = 0
        count[lowerchar] += 1
    for character, number in count.items():
        char_dict = {'char': character, 'num': number}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()