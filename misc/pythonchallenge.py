encrypted = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


# for each letter in the encrypted message, apply something like chr(ord('E') + 2), get new message


def decipher(encrypted):
    decrpyted = ""
    for letter in encrypted:
        if letter.isalpha():
            if letter == 'y':
                new_letter = 'a'
            elif letter == 'z':
                new_letter = 'b'
            else:
                new_letter = chr(ord(letter) + 2)
        else:
            new_letter = letter
        decrpyted += new_letter

    return decrpyted


print(decipher(encrypted))
print(decipher('map'))
