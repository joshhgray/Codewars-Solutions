def vaporcode(s):
	s = list(s)
	s = [l.upper()+"  " for l in s if l !=" "]
	res = " ".join(s)
	return res[:-1]
