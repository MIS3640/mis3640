def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.

    word: string

    returns: bool
    """
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('data/words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


def main():
    print(
        'Here are all the words in the list that have three consecutive double letters:'
    )
    find_triple_double()


if __name__ == "__main__":
    main()
