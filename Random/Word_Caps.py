word = input()

if word[0] == word[0].upper() and word[1:] == word[1:].upper():
    print(word[0].swapcase() + word[1:].swapcase())
if word[0] == word[0].upper() and word[1:] != word[1:].upper():
    print(word[0] + word[1:])
if word[0] == word[0].lower() and word[1:] == word[1:].upper():
    print(word[0].swapcase() + word[1:].swapcase())
if word[0] == word[0].lower() and word[1:] != word[1:].upper():
    print(word[0] + word[1:])
else:
    False
