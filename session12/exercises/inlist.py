def make_word_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    word_list = []
    fin = open("data/words.txt")
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    pass


def main():
    word_list = make_word_list()

    for word in ["aa", "alien", "allen", "zymurgy"]:
        print(word, "in list", in_bisect(word_list, word))


if __name__ == "__main__":
    main()
