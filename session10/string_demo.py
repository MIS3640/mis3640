prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    # if letter == 'O' or letter == 'Q':
    # if letter in 'OQ':
    if letter in ['O', 'Q']:
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)
