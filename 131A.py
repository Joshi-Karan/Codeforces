# Caps Lock

word = input()
if len(word) > 1:
    if word.isupper():
        print(word.lower())
    elif word[1:].isupper():
        print('{}{}'.format(word[0].upper(), word[1:].lower()))
    else:
        print(word)
else:
    print(word.swapcase())
