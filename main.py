from stats import get_num_words, word_occurence, sort_list
import sys


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def print_report(char_dict, word_count):
    print("============ BOOKBOT ============\n")
    print("Analyzing book found at books/frankenstein.txt...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {word_count} total words\n")
    print("--------- Character Count -------")

    for i in char_dict:
        print(f"{i}: {char_dict[i]}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_text = get_book_text(sys.argv[1])
        num_words = get_num_words(book_text)
        # print(f"{num_words} words found in the document")
        # print(word_occurence(book_text))
        char_count = word_occurence(book_text)
        sorted_list = sort_list(char_count)
        print(print_report(sorted_list, num_words))


if __name__ == "__main__":
    main()
