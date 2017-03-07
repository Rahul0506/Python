import operator
import math

#Initialize dictionary mappings for operators, math functions, and constants
oprDict = {

			"+" : operator.add,
			"-" : operator.sub,
			"*" : operator.mul,
			"/" : operator.truediv,
			"//" : operator.floordiv,
			"%" : operator.mod,
			"**" : operator.pow,
			"!" : math.factorial,
			
			}

mathDict = {

			"sin" : math.sin,
			"cos" : math.cos,
			"tan" : math.tan,
			"floor" : math.floor,
			"ceil" : math.ceil,
			"abs" : abs,
			"max" : max,
			"min" : min
			
			}
			
consts = {"e" : math.e, "pi" : math.pi}

#The Lexer
import sys
import re

token_specification = [
        ('NUMBER',  r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',  r':='),           # Assignment operator
        ('ID',      r'[A-Za-z]+'),    # Identifiers
        ('OP',      r'[+\-*/%!]'),		
        ('NEWLINE', r'\n'),           # Line endings
        ('SKIP',    r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH',r'.'),            # Any other character
    ]
	
def tokenize(code, tokens, token_specification):
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        elif kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise RuntimeError('%r unexpected on line %d' % (value, line_num))
        else:
            column = mo.start() - line_start
            tokens.append((kind, value))

statements = '''
    c := a + b
'''

tokens = []
tokenize(statements, tokens, token_specification)
for token in tokens:
    print(token)
	
