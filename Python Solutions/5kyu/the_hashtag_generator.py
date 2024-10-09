def generate_hashtag(s):
    s = s.split(" ")
    res = ["#"]
    
    for w in s:
        res.append(w.title())
    res = "".join(res)

    if len(res) > 140 or res == "#":
        return False
    return res
