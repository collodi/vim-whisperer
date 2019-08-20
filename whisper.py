import sys
import vim_whisperer

USAGE = '''\
Usage: vim-whisperer [--help] [<INPUT>]

--help flag shows this message.
If no <INPUT> is given, read a line from stdin.

The translated vim command will be printed to stdout.
If there is an error, the error message is printed to stderr and the program exits with code 1.
'''

if len(sys.argv) > 1 and sys.argv[1] == '--help':
	print(USAGE, end='')
	sys.exit(0)

s = None
if len(sys.argv) > 1:
	s = sys.argv[1]
else:
	s = input()

vcmd = vim_whisperer.whisper(s)
print(vcmd)
