from .tokenize import tokenize
from .grammar import parse_tokens, translate

def whisper(s):
	tokens = tokenize(s)
	state, values = parse_tokens(tokens)
	return translate(state, values)
