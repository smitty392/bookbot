from stats import get_word_count, get_per_char_count


def main():
    path_to_file = "books/frankenstein.txt"
    text_from_book = get_book_text(path_to_file)
    num_words = get_word_count(text_from_book)
    print(f"{num_words} words found in the document")
    print(get_per_char_count(text_from_book))


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


main()


