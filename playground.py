name = 'Zhe Wang'

# Michael: check how many 'a', how many 'e', ...

counter = 0
for vowel in 'aeiou':
    counter += name.count(vowel)

print(counter)


def vowel_counter(s):
    v = 0
    if 'a' in s:
        v += s.count('a')
    if 'e' in s:
        v += s.count('e')
    if 'i' in s:
        v += s.count('i')
    if 'u' in s:
        v += s.count('u')
    if 'o' in s:
        v += s.count('o')
    return v


# print(vowel_counter('James Walters'))


def count_vowels(name, special):
    num_vowels = 0
    # string = 'nian liu'
    for letter in name.lower():
        if letter in special:
            num_vowels = num_vowels + 1
    return num_vowels


# print(count_vowels('Sammi Xu', 'xyz'))
