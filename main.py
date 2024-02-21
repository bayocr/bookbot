import string


def main():
    book_path = "books/frankenstein.txt"
    file_content = get_file_string(book_path)
    num_words = get_words_num(file_content)
    num_letters = get_letters_num((file_content))
    orderd_letters = get_ordered_list(num_letters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the book")
    print()
    for letter_info in orderd_letters:
        print(
            f"The {letter_info['letter']} character was found {letter_info['count']} times")
    print("--- End report ---")


def get_file_string(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def get_words_num(raw_words):
    words = raw_words.split()

    return len(words)


def get_letters_num(raw_words):
    lower_words = raw_words.lower()
    words = lower_words.split()
    lower_alphabet = list(string.ascii_lowercase)
    result = {}

    for letter in lower_alphabet:
        result[letter] = 0

    for word in words:
        for letter in word:
            if letter in lower_alphabet:
                result[letter] += 1

    return result


def sort_on(dict):
    return dict["count"]


def get_ordered_list(unorder_list):
    result_list = []
    # letters_counts = unorder_list
    # for i in letters_counts:
    for i in unorder_list:
        result_list.append({"letter": i, "count": unorder_list[i]})

    result_list.sort(reverse=True, key=sort_on)
    return result_list


main()
