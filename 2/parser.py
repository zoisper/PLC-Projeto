import ply.yacc as yacc
import sys

from lexer import tokens



def p_program(p):
	"""
	program : MAIN LCURLY RCURLY
	program : MAIN LCURLY instructions RCURLY
	"""
	






def p_error(p):
	print("Syntax error!")
	parser.success = False




parser = yacc.yacc()
parser.success = True




source = ""

for line in sys.stdin:
	source += line
print(source)

parser.parse(source)

if parser.success:
	print("Parsing successfully completed!")
