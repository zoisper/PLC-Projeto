import ply.yacc as yacc
import sys
import os.path
from lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
)


def p_program(p):
	"""
	program : MAIN LCURLY body RCURLY
	"""
	fp.write(p[3])
	print(p[3])

def p_body(p):
	""" 
	body : declarations instructions
	"""
	p[0] = p[1] + 'START\n' + p[2] + 'STOP'

def p_declarations_empty(p):
	"""
	declarations : 
	"""
	p[0] = ""

def p_declarations(p):
	"""
	declarations : declaration  declarations
	"""
	p[0] = p[1] + p[2]


def p_declaration_int(p):
	"""
	declaration : INT VAR SEMICOLON 
	"""
	parser.tab_id[p[2]] = ('int',parser.prox_add,1)
	parser.prox_add +=1
	p[0] = 'PUSHI 0\n'



def p_declaration_float(p):
	"""
	declaration : FLOAT VAR SEMICOLON 
	"""
	parser.tab_id[p[2]] = ('float',parser.prox_add,1)
	parser.prox_add += 1
	p[0] = 'PUSHI 0\n'



def p_declaration_array_int(p):
	"""
	declaration : INT LBRACKET NUM RBRACKET VAR SEMICOLON 

	"""
	parser.tab_id[p[5]] = ('int',parser.prox_add,p[3])
	parser.prox_add += p[3]
	p[0] = f'PUSHN {p[3]}\n'
	

def p_declaration_biarray_int(p):
	"""
	declaration : INT LBRACKET NUM RBRACKET LBRACKET NUM RBRACKET VAR SEMICOLON 

	"""
	parser.tab_id[p[8]] = ('int',parser.prox_add,(p[3],p[6]))
	parser.prox_add += p[3]*p[6]
	p[0] = f'PUSHN {p[3]*p[6]}\n'


def p_declaration_array_float(p):
	"""
	declaration : FLOAT LBRACKET NUM RBRACKET VAR SEMICOLON 
	"""
	parser.tab_id[p[5]] = ('float',parser.prox_add,p[3])
	parser.prox_add += p[3]
	p[0] = f'PUSHN {p[3]}\n'
	

def p_declaration_biarray_float(p):
	"""
	declaration : FLOAT LBRACKET NUM RBRACKET LBRACKET NUM RBRACKET VAR SEMICOLON 

	"""
	parser.tab_id[p[8]] = ('float',parser.prox_add,(p[3],p[6]))
	parser.prox_add += p[3]*p[6]
	p[0] = f'PUSHN {p[3]*p[6]}\n'
	






def p_variable_single(p):
	"""
	variable : VAR
	"""
	p[0] = (parser.tab_id[p[1]][0],parser.tab_id[p[1]][1])
	

def p_variable_index_num(p):
	"""
	variable : VAR LBRACKET NUM RBRACKET
	"""
	p[0] = (parser.tab_id[p[1]][0],parser.tab_id[p[1]][1] + p[3])

def p_variable_index_index_num(p):
	"""
	variable : VAR LBRACKET NUM RBRACKET LBRACKET NUM RBRACKET
	"""
	p[0] = (parser.tab_id[p[1]][0],parser.tab_id[p[1]][1] + p[3]*parser.tab_id[p[1]][2][1] + p[6])


#def p_variable_index_var(p):
#	"""
#	variable : VAR LBRACKET VAR RBRACKET
#	"""
#	p[0] = (parser.tab_id[p[1]][0],parser.tab_id[p[1]][1] + p[3])

#def p_variable_index_index_var(p):
#	"""
#	variable : VAR LBRACKET VAR RBRACKET LBRACKET VAR RBRACKET
#	"""
#	p[0] = (parser.tab_id[p[1]][0],parser.tab_id[p[1]][1] + p[3]*parser.tab_id[p[1]][2][1] + p[6])
#



def p_instructions_empty(p):
	"""
	instructions :
	"""
	p[0] = ""


def p_instructions(p):
	"""
	instructions : instruction  instructions
	"""
	p[0] = p[1] + p[2]




def p_instruction_atribution_expression(p):
	"""
	instruction : variable EQUAL expression SEMICOLON
	"""
	if isinstance (p[1],tuple):
		p[0] = p[3] + f'STOREG {p[1][1]}\n'
	#else:
	#	p[0] = 
	


def p_expression_var(p):
	"""
	expression : variable
	"""
	p[0] = f'PUSHG {p[1][1]}\n'


def p_expression_num(p):
	"""
	expression : NUM
	"""
	p[0] = f'PUSHI {p[1]}\n'

def p_expression_float(p):
	"""
	expression : REAL
	"""
	p[0] = f'PUSHF {p[1]}\n'


def p_expression_between_parenthesis(p):
	"""
	expression : LPAREN expression RPAREN
	"""
	p[0] = p[2]





def p_expression_plus_expression(p):
	"""
	expression : expression PLUS expression
	"""
	p[0] = p[1] + p[3] + 'ADD\n'

def p_expression_minus_expression(p):
	"""
	expression : expression MINUS expression
	"""
	p[0] = p[1] + p[3] + 'SUB\n'

def p_expression_mul_expression(p):
	"""
	expression : expression MUL expression
	"""
	p[0] = p[1] + p[3] + 'MUL\n'


def p_expression_div_expression(p):
	"""
	expression : expression DIV expression
	"""
	p[0] = p[1] + p[3] + 'DIV\n'

def p_expression_div_expression(p):
	"""
	expression : expression MOD expression
	"""
	p[0] = p[1] + p[3] + 'MOD\n'


def p_instruction_cicle(p):
	"""
	instruction : WHILE LPAREN condition RPAREN LCURLY instructions RCURLY
	"""
	p[0] = f'B{parser.labels}:\n' + p[3] + f'E{parser.labels}\n' + p[6] + f'JUMP B{parser.labels}\n' + f'E{parser.labels}:\n' 
	parser.labels +=1


def p_instruction_conditional(p):
	"""
	instruction : IF LPAREN condition RPAREN LCURLY instructions RCURLY
	"""
	p[0] = p[3] + f'E{parser.labels}\n' + p[6] + f'E{parser.labels}:\n' 
	parser.labels +=1
	


def p_condition_expression_eqeq_expression(p):
	"""
	condition : expression EQEQ expression
	"""
	p[0] = p[1] + p[3] + 'EQUAL\nJZ '


def p_condition_expression_diff_expression(p):
	"""
	condition : expression DIFF expression
	"""
	p[0] = p[1] + p[3] + 'SUB\nJZ '

def p_condition_expression_greater_expression(p):
	"""
	condition : expression GREATER expression
	"""
	p[0] = p[1] + p[3] + 'SUP\nJZ '

def p_condition_expression_lesser_expression(p):
	"""
	condition : expression LESSER expression
	"""
	p[0] = p[1] + p[3] + 'INF\nJZ '

def p_condition_expression_greateq_expression(p):
	"""
	condition : expression GREATEQ expression
	"""
	p[0] = p[1] + p[3] + 'SUPEQ\nJZ '

def p_condition_expression_lesseq_expression(p):
	"""
	condition : expression LESSEQ expression
	"""
	p[0] = p[1] + p[3] + 'INFEQ\nJZ '





def p_condition_num(p):
	"""
	condition : NUM
	"""
	p[0] = f'PUSHI {p[1]}\nJZ '

def p_condition_var(p):
	"""
	condition : variable
	"""
	p[0] = f'PUSHG {p[1][1]}\nJZ '

def p_instruction_input(p):
	"""
	instruction : INPUT LPAREN variable RPAREN SEMICOLON
	"""
	p[0] = 'READ\n'
	if p[3][0] == 'int':
		p[0] += 'ATOI\n'
	else:
		p[0] += 'ATOF\n'

	p[0] += f'STOREG {p[3][1]}\n' 


def p_instruction_print_var(p):
	"""
	instruction : PRINT LPAREN variable RPAREN SEMICOLON
	"""
	p[0] = f'PUSHG {p[3][1]}\n'

	if p[3][0] == 'int':
		p[0] += 'WRITEI\n'
	else:
		p[0] += 'WRITEF\n'


def p_instruction_println_var(p):
	"""
	instruction : PRINTLN LPAREN variable RPAREN SEMICOLON
	"""
	p[0] = f'PUSHG {p[3][1]}\n'

	if p[3][0] == 'int':
		p[0] += 'WRITEI\n'
	else:
		p[0] += 'WRITEF\n'

	p[0] += 'PUSHS\"\\n\"\nWRITES\n'




def p_instruction_print_string(p):
	"""
	instruction : PRINT LPAREN STRING RPAREN SEMICOLON
	"""
	p[0] = f'PUSHS {p[3]}\nWRITES\n'


def p_instruction_println_string(p):
	"""
	instruction : PRINTLN LPAREN STRING RPAREN SEMICOLON
	"""
	p[0] = f'PUSHS {p[3]}\nWRITES\nPUSHS\"\\n\"\nWRITES\n'




def p_error(p):
	print("Syntax error!")
	parser.success = False




parser = yacc.yacc()
parser.success = True

parser.prox_add = 0
parser.tab_id = {}
parser.labels = 0


if len(sys.argv)!=2 and len(sys.argv)!=3:
    print('Número de argumentos invalido!')
    sys.exit(0)
else:
    file_input = sys.argv[1]

if not os.path.exists(file_input):
	print(f"Ficheiro \"{file_input}\" não encontrado!")
	sys.exit(0)


fp = open(file_input, 'r')
source = fp.readlines()
fp.close()


if len(sys.argv)==3:
    file_output = sys.argv[2]
else:
	file_output = "a.out"

fp = open(file_output,"w")

parser.parse("".join(source))


if parser.success:
	print("Parsing successfully completed!")

fp.close()

