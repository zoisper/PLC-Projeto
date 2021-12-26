import ply.yacc as yacc
import sys

from lexer import tokens



def p_program(p):
	"""
	program : MAIN LCURLY body RCURLY
	"""

def p_body(p):
	"""
	body : 
	body : declarations instructions
	"""

	
def p_declarations(p):
	"""
	declarations : 
	declarations : declaration  declarations
	"""

def p_declaration(p):
	"""
	declaration : type declare SEMICOLON 
	"""

def p_delcare(p):
	"""
	declare : VAR 
	declare : VAR COMA declare
	"""


def p_type(p):
	"""
	type : BOOL
	type : INT
	"""

def p_instructions(p):
	"""
	instructions :
	instructions : instruction  instructions
	"""

def p_instruction(p):
	"""
	instruction : cicle
	instruction : conditional
	instruction : atribution 
	"""
def p_cicle(p):
	"""
	cicle : WHILE LBRACE condition RBRACE LCURLY instructions RCURLY
	"""

def p_conditional(p):
	"""
	conditional : IF LBRACE condition RBRACE LCURLY instructions RCURLY
	"""

def p_atribution(p):
	"""
	atribution : VAR EQUAL TRUE SEMICOLON
	atribution : VAR EQUAL FALSE SEMICOLON
	atribution : VAR EQUAL expression SEMICOLON
	"""


def p_condition(p):
	"""
	condition : expression EQEQ expression
	condition : VAR EQEQ expression
	condition : VAR DIFF expression
	condition : VAR EQEQ TRUE
	condition : VAR EQEQ FALSE
	condition : VAR DIFF TRUE
	condition : VAR DIFF FALSE
	condition : expression GREATER expression
	condition : expression LESSER expression
	condition : expression GREAEQ expression
	condition : expression LESSEQ expression
	condition : expression DIFF expression
	condition : TRUE
	condition : FALSE
	"""
def p_expression(p):
	"""
	expression : VAR
	expression : REAL
	expression : NUM
	expression : LBRACE expression RBRACE
	expression : expression PLUS expression
	expression : expression MINUS expression
	expression : expression MUL expression
	expression : expression DIV expression
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
