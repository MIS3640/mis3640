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
        if len(word) > 20:
            print(word, len(word))


# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter "e" in it
    """
    for letter in word:
        if letter == "e" or letter == "E":
            return False
    return True


# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA sports'))


def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """
    f = open("data/words.txt")
    num_words_no_e = 0
    num_of_words = 0
    num_words_with_e = 0
    for line in f:
        num_of_words += 1
        word = line.strip()
        if has_no_e(word):
            # print(word)
            num_words_no_e += 1
        else:
            num_words_with_e += 1
    return num_words_no_e / num_of_words


perc_no_e = find_words_no_e()
print(f'The percentage of the words with no "e" is {perc_no_e*100:.2f}%.')


def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    """
    for letter in word:
        if letter in forbidden:
            return False
    return True


# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'e'))
# print(avoids('Boston', 'xyz'))


def find_words_no_vowels():
    """
    returns the percentage of the words that don't have vowel letters
    """
    f = open("data/words.txt")
    num_words_no_vowel = 0
    num_of_words = 0
    for line in f:
        num_of_words += 1
        word = line.strip()
        if avoids(word, 'aeiou'):
            # print(word)
            num_words_no_vowel += 1
    return num_words_no_vowel / num_of_words


# perc_no_vowel = find_words_no_vowels()
# print(f'The percentage of the words without vowel letters is {perc_no_vowel*100:.2f}%.')


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the string available.
    """
    for letter in word:
        if letter not in available:
            return False
    return True


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def find_words_only_use_planet():
    """"""
    f = open('data/words.txt')
    num_words_only_use_planet = 0
    for line in f:
        word = line.strip()
        if uses_only(word, 'planet'):
            num_words_only_use_planet += 1
            print(word)
    return num_words_only_use_planet


print(
    'Number of words that use only letters from "planets" is',
    find_words_only_use_planet(),
)


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    # for letter in required:
    #     if letter not in word:
    #         return False
    # return True
    return uses_only(required, word)


# please write test cases

# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))
# print(uses_all('Babson', 'aeoiu'))
# print(uses_all('Babesonious', 'aeoiu'))


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    f = open('data/words.txt')
    num_words_use_all_vowels = 0
    for line in f:
        word = line.strip()
        if uses_all(word, 'aeiou'):
            num_words_use_all_vowels += 1
            print(word)
    return num_words_use_all_vowels


# print('The number of words that use all the vowels:', find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    left = word[0]
    for letter in word:
        if left > letter:
            return False
        left = letter
    return True


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


def find_abecedarian_words():
    """
    returns the number of abecedarian words
    """
    fin = open('data/words.txt')
    counter = 0
    current_longest_word = ''
    for line in fin:
        word = line.strip()
        if is_abecedarian(word):
            # print(word)
            counter += 1
            if len(word) > len(current_longest_word):
                current_longest_word = word

    return counter, current_longest_word


# print(find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    # print('now checking, ', word[1:])
    return is_abecedarian_using_recursion(word[1:])


# print(is_abecedarian_using_recursion('abcdef'))


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    i = 0
    while i < len(word) - 1:
        if word[i + 1] < word[i:]:
            return False
        i = i + 1
    return True


# print(is_abecedarian_using_while('abcdef'))
