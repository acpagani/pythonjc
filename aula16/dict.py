
def contar_chars(frase):
    chars = dict()

    for c in range(len(frase)):
        if not frase[c] in chars:
            chars[frase[c]] = 1
        else:
            chars[frase[c]] += 1

    return chars

