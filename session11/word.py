# import os

# print(os.getcwd())


# Assume words.txt is under data folder
# f = open('data/words.txt')
# line = f.readline()
# print(line)


# f = open('data/words.txt')

# number_of_words = 0

# for line in f:
#     word = line.strip()
#     number_of_words += 1

# print(number_of_words)


def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    f = open('data/words.txt')  # Assume words.txt is under data folder

    for line in f:
        word = line.strip()
        if len(word) > 18:
            print(word, len(word))


# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter "e" in it
    """
    # for letter in word:
    #     if letter == 'e' or letter == 'E':
    #         return False
    # return True
    return 'e' not in word and 'E' not in word


# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA sports'))


def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """
    f = open('data/words.txt')
    # create a var to count the total number of words
    num_total = 0
    # create a var to count the words has-no-e
    num_words_no_e = 0

    for line in f:
        word = line.strip()
        # increment total number
        num_total += 1
        # if the word has no e, increment number-no-e
        if has_no_e(word):
            num_words_no_e += 1

    # return number-no-e/total
    return num_words_no_e / num_total


perc_no_e = find_words_no_e()
print(f'The percentage of the words with no "e" is {perc_no_e*100:.2f}%.')


def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    """
    pass


# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'e'))
# print(avoids('Boston', 'xyz'))


def find_words_no_vowels():
    """
    returns the percentage of the words that don't have vowel letters
    """
    pass


# perc_no_vowel = find_words_no_vowels()
# print(f'The percentage of the words without vowel letters is {perc_no_vowel*100:.2f}%.')


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the string available.
    """
    pass


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def find_words_only_use_planet():
    """"""
    pass


# print('Number of words that use only letters from "planets" is', find_words_only_use_planet())


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    pass


# please write test cases


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    pass


# print('The number of words that use all the vowels:', find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


def find_abecedarian_words():
    """
    returns the number of abecedarian words
    """
    pass


# print(find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian_using_recursion('abcdef'))


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


# print(is_abecedarian_using_while('abcdef'))
