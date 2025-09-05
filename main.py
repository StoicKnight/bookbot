import sys

from stats import count_chars, count_words, sort_dict


def parse_args():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return args[1]


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    file_path = parse_args()
    file_content = get_book_text(file_path)

    num_words = count_words(file_content)
    count_dict = count_chars(file_content)
    sorted_chars = sort_dict(count_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_count in sorted_chars:
        print(f"{char_count["char"]}: {char_count["num"]}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
