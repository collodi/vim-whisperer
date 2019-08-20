import re

GRAMMAR = '''\
_start go _go
_go line _go_line
_go_line NUMBER _go_line_number

_start copy _copy
_copy NUMBER _copy_number
_copy_number lines _copy_number_lines
'''

def parse_grammar():
	transitions = {}
	for ln in GRAMMAR.split('\n'):
		ln = ln.strip()
		if len(ln) == 0:
			continue

		s1, token, s2 = ln.split()
		transitions[(s1, token)] = s2

	return transitions

def parse_tokens(tokens):
	transitions = parse_grammar()

	state = '_start'
	values = []
	for token in tokens:
		t = None
		if re.fullmatch(r'[0-9]+', token) != None:
			t = (state, 'NUMBER')
		else:
			t = (state, token)

		if t in transitions:
			state = transitions[t]
			values.append(token)

	return state, values

def translate(state, values):
	if state == '_go_line_number':
		return f'{values[2]}gg'
	elif state == '_copy_number_lines':
		return f'{values[1]}yy'
