def shorten(str):
    newStr = ''
    for character in str:
        if character.isupper():
            newStr += character
    return newStr

print(shorten("Universidade de Aveiro"))