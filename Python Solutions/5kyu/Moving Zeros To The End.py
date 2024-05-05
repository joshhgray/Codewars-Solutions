def move_zeros(lst):
    res = [x for x in lst if x != 0]
    for i in range(len(lst) - len(res)):
        res.append(0)
    return res