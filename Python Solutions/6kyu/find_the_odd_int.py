def find_it(seq):
    d = {}
    for digit in seq:
        if digit in d:
            d[digit] += 1
        elif digit not in d:
            d[digit] = 1
    return list(filter(lambda x: d[x] % 2 != 0, d))[0]
