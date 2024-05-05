def duplicate_encode(word):
    word = word.lower()
    dbl = []
    output = ''
    temp = []
    for l in list(word):
        if l in temp:
            dbl.append(l)
        else:
            temp.append(l)
    for l in list(word):
        if l in dbl:
            output = output + ')'
        else:
            output = output + '('
    print(dbl)
    return output