def solve(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    longest_chain = 0
    res = 0
    for char in list(s):
        if char in vowels:
            longest_chain += 1
            if longest_chain > res:
                    res = longest_chain
        else:
            longest_chain = 0
    return res
