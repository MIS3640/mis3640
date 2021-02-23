def rotate(word, n):
    """
    Take a string, WORD, and an integer, N as parameters, and return a new string that contains the letters from the original string, WORD, rotated by the given amount, N.
    """
    new_string = ''
    for letter in word:
        new_string += chr(ord(letter) + n)
    return new_string


def main():
    print(rotate('abc', 2))


if __name__ == '__main__':
    main()
