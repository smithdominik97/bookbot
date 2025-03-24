def get_num_words(text):
    split_text = text.split()
    count = len(split_text)
    return count


def word_occurence(text):
    text = text.lower()
    split_text = text.split()
    char_count = {}

    for word in split_text:
        char_list = list(word)

        for char in char_list:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count


def sort_list(char_dict):
    sorted_list = {}

    for key in sorted(char_dict, key=char_dict.get, reverse=True):
        sorted_list[key] = char_dict[key]

    return sorted_list
