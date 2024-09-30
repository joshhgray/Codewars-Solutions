def order_weight(s):
    s = s.split(" ")
    s = list(filter(None, s))
    
    for i, n in enumerate(s[1:]):
        idx = i
        while idx >= 0:
            if get_weight(int(n)) <= get_weight(s[idx]):
                if get_weight(int(n)) == get_weight(s[idx]):
                    if sorted([str(int(n)), str(s[idx])]) == [str(int(n)), str(s[idx])]:
                        swap(s, idx+1, idx)
                    else: 
                        idx -= 1
                        break
                    idx -= 1
                else:
                    swap(s, idx+1, idx)
                    idx -= 1
            else: break
            
    return " ".join(s)
          
def get_weight(num):
    sum = 0
    lnum = list(str(num))
    for n in lnum:
        sum += int(n)
    return sum

def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp

