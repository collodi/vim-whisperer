import re

def tokenize(s):
	s = re.sub(r'[^a-z0-9 ]', '', s.lower())
	return s.split()
