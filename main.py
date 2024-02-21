def main():
    book_path = "books/frankenstein.txt"
    file_content = get_file_string(book_path)
    num_words = get_words_num(file_content)

    print(f"{num_words} words found in the book")


def get_file_string(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def get_words_num(raw_words):
    words = raw_words.split()

    return len(words)


main()
