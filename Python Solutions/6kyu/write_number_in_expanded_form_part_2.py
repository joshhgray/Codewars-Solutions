def expanded_form(num):
    s = str(num).split('.')
    res1 = []
    res2 = []
    n1 = len(s[0])
    for digit in s[0]:
        if digit is not '0':
            res1.append(digit + ('0' * (n1-1)) + ' + ')
        n1 -=1
    for i, digit in enumerate(s[1]):
        if digit is not '0':
            res2.append(digit + '/' + '1' + ('0' * (i+1)) + ' + ')
        
    return ''.join(res1) + ''.join(res2)[:-3]
