def get_word_count(text_from_book):
    text_split = text_from_book.split()
    num_words = len(text_split)
    return num_words


def get_per_char_count(text_from_book):
    char_dict = {}
    for char in text_from_book:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    return char_dict
