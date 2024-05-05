def digital_root(n):
    nlist = list(str(n))
    while len(nlist) > 1:
        sum = 0
        for n in nlist:
            sum += int(n)
        nlist = []
        nlist = list(str(sum))
    return int(nlist[0])