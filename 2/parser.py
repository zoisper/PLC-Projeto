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

def p_declaration_int(p):
	"""
	declaration : INT VAR SEMICOLON 
	"""


def p_declaration_bool(p):
	"""
	declaration : BOOL VAR SEMICOLON 
	"""

def p_declaration_array_int(p):
	"""
	declaration : INT LBRACKET NUM RBRACKET VAR SEMICOLON 

	"""

def p_declaration_biarray_int(p):
	"""
	declaration : INT LBRACKET NUM RBRACKET LBRACKET NUM RBRACKET VAR SEMICOLON 

	"""


def p_declaration_array_bool(p):
	"""
	declaration : BOOL LBRACKET NUM RBRACKET VAR SEMICOLON 
	"""


def p_instructions(p):
	"""
	instructions :
	instructions : instruction  instructions
	"""

def p_instruction_atribution_true(p):
	"""
	instruction : VAR EQUAL TRUE SEMICOLON 
	"""

def p_instruction_atribution_false(p):
	"""
	instruction : VAR EQUAL FALSE SEMICOLON 
	"""


def p_instruction_atribution_expression(p):
	"""
	instruction : VAR EQUAL expression SEMICOLON
	"""

def p_expression_var(p):
	"""
	expression : VAR
	"""

def p_expression_num(p):
	"""
	expression : NUM
	"""

def p_expression_REAL(p):
	"""
	expression : REAL
	"""


def p_expression_between_parenthesis(p):
	"""
	expression : LPAREN expression RPAREN
	"""

def p_expression_plus_expression(p):
	"""
	expression : expression PLUS expression
	"""

def p_expression_minus_expression(p):
	"""
	expression : expression MINUS expression
	"""

def p_expression_mul_expression(p):
	"""
	expression : expression MUL expression
	"""

def p_expression_div_expression(p):
	"""
	expression : expression DIV expression
	"""


def p_instruction_cicle(p):
	"""
	instruction : WHILE LPAREN condition RPAREN LCURLY instructions RCURLY
	"""

def p_instruction_conditional(p):
	"""
	instruction : IF LPAREN condition RPAREN LCURLY instructions RCURLY
	"""


def p_condition_expression_eq_expression(p):
	"""
	condition : expression EQEQ expression
	"""

def p_condition_expression_diff_expression(p):
	"""
	condition : expression DIFF expression
	"""

def p_condition_expression_greater_expression(p):
	"""
	condition : expression GREATER expression
	"""

def p_condition_expression_lesser_expression(p):
	"""
	condition : expression LESSER expression
	"""

def p_condition_expression_greateq_expression(p):
	"""
	condition : expression GREATEQ expression
	"""

def p_condition_expression_lesseq_expression(p):
	"""
	condition : expression LESSEQ expression
	"""


def p_condition_var_eqeq_expression(p):
	"""
	condition : VAR EQEQ expression
	"""

def p_condition_var_diff_expression(p):
	"""
	condition : VAR DIFF expression
	"""


def p_condition_var_eqeq_true(p):
	"""
	condition : VAR EQEQ TRUE
	"""

def p_condition_var_eqeq_false(p):
	"""
	condition : VAR EQEQ FALSE
	"""

def p_condition_var_diff_true(p):
	"""
	condition : VAR DIFF TRUE
	"""
def p_condition_var_diff_false(p):
	"""
	condition : VAR DIFF FALSE
	"""


def p_condition_true(p):
	"""
	condition : TRUE
	"""

def p_condition_false(p):
	"""
	condition : FALSE
	"""

def p_instruction_input(p):
	"""
	instruction : INPUT LPAREN VAR RPAREN SEMICOLON
	"""


def p_instruction_print_var(p):
	"""
	instruction : PRINT LPAREN VAR RPAREN SEMICOLON
	"""

def p_instruction_print_string(p):
	"""
	instruction : PRINT LPAREN STRING RPAREN SEMICOLON
	"""




def p_error(p):
	print("Syntax error!")
	parser.success = False




parser = yacc.yacc()
parser.success = True


if len(sys.argv)==2:
    file = sys.argv[1]
else:
    print('Número de argumentos invalido!')
    sys.exit(0)

if not os.path.exists(file):
    print(f"Ficheiro \"{file}\" não encontrado!")
    sys.exit(0)


fp = open(file, 'r')
source = fp.readlines()
fp.close()


fp = open("a.out","w")

parser.parse("".join(source))


if parser.success:
	print("Parsing successfully completed!")

fp.close()

