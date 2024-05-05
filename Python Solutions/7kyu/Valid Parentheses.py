def valid_parentheses(paren_str):
    count_open = 0
    count_close = 0
    for paren in list(paren_str):
        if paren == '(':
            count_open += 1
        if paren == ')':
            count_close += 1
        if count_close > count_open:
            return False
    if count_open != count_close:
        return False
    return True