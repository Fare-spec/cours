def is_palindrom(word)->bool:
    word = list(word)
    if len(word) < 2:
        return True
    if word[0] == word[-1]:
        word.pop(0)
        word.pop(-1)
        return is_palindrom(word)
    else:
        return False

print(is_palindrom("do geese see god".replace(' ', '')))
