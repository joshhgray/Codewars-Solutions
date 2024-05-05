def tribonacci(signature, n):
    new_sig = []
    if n == 0:
        return new_sig
    for i in range(n):
        if i < 3:
            new_sig.append(signature[i])
        else:
            new_sig.append(new_sig[i-1] + new_sig[i-2] + new_sig[i-3])
    return new_sig
        