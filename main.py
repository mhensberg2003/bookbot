def main():
    book = "books/frankenstein.txt"
    with open (book) as f:
        count = 0
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            count += 1
        print(count)
main()