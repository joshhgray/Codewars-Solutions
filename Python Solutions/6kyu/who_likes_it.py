def likes(names):
    
    res = "no one likes this"
    n = len(names)
    
    if n == 1:
        res = f"{names[0]} likes this"
    
    elif n == 2:
        res = f"{names[0]} and {names[1]} like this"
    
    elif n == 3:
        res = f"{names[0]}, {names[1]} and {names[2]} like this"

    elif n >= 4:
        res = f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
        
    return res
    
