def unique_in_order(sequence):
    seq = list(sequence)
    for i in range(len(seq)):
        while i < len(seq)-1 and seq[i+1] == seq[i]:
            seq.pop(i+1)
    return seq