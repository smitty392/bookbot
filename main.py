from stats import get_word_count, get_per_char_count, sort_by_char_count


def main():
    book_path = "books/frankenstein.txt"
    text_from_book = get_book_text(book_path)

    num_words = get_word_count(text_from_book)
    char_count = get_per_char_count(text_from_book)
    sorted_char_count = sort_by_char_count(char_count)

    print(format_results(book_path, num_words, sorted_char_count))


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def format_results(book_path, num_words, sorted_char_count):
    result = f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{"\r\n".join([f"{char["char"]}: {char["num"]}" for char in sorted_char_count if char["char"].isalpha()])}"""

    return result


main()


