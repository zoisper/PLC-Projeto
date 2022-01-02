import ply.yacc as yacc
import sys
import os.path
from lexer import tokens



def p_program(p):
	"""
	program : MAIN LCURLY body RCURLY
	"""

def p_body(p):
	""" 
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


def p_type_int(p):
	"""
	type : INT
	"""

def p_type_array_int(p):
	"""
	type : INT LBRACKET NUM RBRACKET
	"""

def p_type_bool(p):
	"""
	type : BOOL
	"""

def p_type_array_bool(p):
	"""
	type : BOOL LBRACKET NUM RBRACKET
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


if len(sys.argv)==2:
    text_source = sys.argv[1]
else:
    print('Número de argumentos invalido!')
    sys.exit(0)

if not os.path.exists(text_source):
    print(f"Ficheiro \"{text_source}\" não encontrado!")
    sys.exit(0)

#source = ""


fp = open(text_source, 'r')
text = fp.readlines()
fp.close()

#for line in text:
#	source += line
#print(source)


fp = open("a.out","w")

parser.parse("".join(text))


if parser.success:
	print("Parsing successfully completed!")

fp.close()

