from inlist import make_word_list, in_bisect


def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.

    word_list: list of strings
    word: string
    """
    pass


def interlock_general(word_list, word, n=3):
    """Checks whether a word contains n interleaved words.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    pass


def main()
    word_list = make_word_list()

    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])


if __name__ == "__main__":
    main()
