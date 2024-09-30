def wtest(s):

	s = s.split(" ")
	s = list(filter(None, s))	
	
	for n in s[1:]:
		print(n)


string = '     65 99 53 22 61 100'

wtest(string)
