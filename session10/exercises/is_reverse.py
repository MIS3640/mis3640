def is_reverse(word1, word2):
    """Return True if WORD2 is the reversed WORD1"""
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2)

    while j > 0:
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True


print(is_reverse('pots', 'stop'))
