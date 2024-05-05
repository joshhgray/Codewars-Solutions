def longest(a1, a2):
    ls = sorted(list(set(list(a1+a2))))
    res = ''
    for i in range(len(ls)):
        res = res + ls[i]
    return res
    