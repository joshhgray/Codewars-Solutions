def solution(s):
    return ''.join([l if l == l.lower() else f' {l}' for l in s])