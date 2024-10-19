def expanded_form(num):
    n = len(str(num))
    res = []
    for digit in list(str(num)):
        if digit is not '0':
            res.append(digit + ('0' * (n-1)) + ' + ')
        n -= 1
    return ''.join(res)[:-3]
