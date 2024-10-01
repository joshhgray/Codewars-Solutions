def count(s):
    res = {}
    for l in s:
        if l not in res:
            res[l] = 1
        elif l in res:
            res[l] += 1
    return res
