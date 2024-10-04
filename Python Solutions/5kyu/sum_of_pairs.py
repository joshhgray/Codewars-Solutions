def sum_pairs(ints, s):
    # need to refactor nested loop to get through tests
    pair_idxs = []
    for i, int in enumerate(ints):
        for j, next_int in enumerate(ints[i+1:]):
            if int + next_int == s:
                pair_idxs.append([i, j+1+i])
    
    res = None
    if len(pair_idxs) >= 1:
        res = [ints[pair_idxs[0][0]], ints[pair_idxs[0][1]]] 
    
    if len(pair_idxs) > 1:
        for pair in pair_idxs:
            if pair[1] < res[1]:
                res = [ints[pair[0]], ints[pair[1]]]
        
    return res
    
