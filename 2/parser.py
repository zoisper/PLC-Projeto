import ply.yacc as yacc
import sys
import os.path
from lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIV'),
)


def var_new(v):
	if v[0] in parser.tab_id or v[1] == 0 or v[2] == 0:
		return -1
	else:
		parser.tab_id[v[0]] = (parser.prox_address,v[1],v[2],v[3])
		parser.prox_address += v[1]*v[2]
		return 0

def var_address_base(v):
	if v in parser.tab_id:
		return parser.tab_id[v][0]
	else:
		return -1

def var_address_colum_line(v,colum,line):
	if var_adress_exists(v,colum,line):
		return var_address_base(v) + var_num_colums(v)*line + colum 
	else:
		return -1

def var_num_colums(v):
	if v in parser.tab_id:
		return parser.tab_id[v][1]
	else:
		return -1


def var_num_lines(v):
	if v in parser.tab_id:
		return parser.tab_id[v][2]
	else:
		return -1

def var_size(v):
	if v in parser.tab_id:
		return parser.tab_id[v][1] * parser.tab_id[v][2]
	else:
		return 0


def var_type(v):
	if v in parser.tab_id:
		return parser.tab_id[v][3]
	else:
		return None


def var_adress_exists(name,colum,line):
	if not name in parser.tab_id:
		return False
	elif colum >= var_num_colums(name) or line >= var_num_lines(name):
		return False
	else:
		return True



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


def p_declaration_single(p):
	"""
	declaration : type VAR SEMICOLON 
	"""

	status = var_new((p[2],1,1,p[1]))
	if status == -1:
		p[0] = f'ERR \"multipla declaração da variavel {p[2]}\"\nSTOP'
	else:
		p[0] = 'PUSHI 0\n'
	






def p_declaration_array(p):
	"""
	declaration : type LBRACKET NUM RBRACKET VAR SEMICOLON 

	"""
	status = var_new((p[5],p[3],1,p[1]))
	if status == -1:
		p[0] = f'ERR \"multipla declaração da variavel {p[2]}\"\nSTOP'
	else:
		p[0] = f'PUSHN {var_size(p[5])}\n'


	

def p_declaration_biarray(p):
	"""
	declaration : type LBRACKET NUM RBRACKET LBRACKET NUM RBRACKET VAR SEMICOLON 

	"""
	status = var_new((p[8],p[6],p[3],p[1]))
	if status == -1:
		p[0] = f'ERR \"multipla declaração da variavel {p[2]}\"\nSTOP\n'
	else:
		p[0] = f'PUSHN {var_size(p[8])}\n'




def p_type_int(p):
	"""
	type : INT
	"""
	p[0] = f'{p[1]}'

def p_type_float(p):
	"""
	type : FLOAT
	"""
	p[0] = f'{p[1]}'




def p_variable_single(p):
	"""
	variable : VAR
	"""
	#p[0] = (p[1],var_address_base(p[1]),var_type(p[1]))
	p[0] = ('PUSHGP\n' + f'PUSHI {var_address_base(p[1])}\n',var_type(p[1]),var_size(p[1]))  
	



def p_variable_index_expression(p):
	"""
	variable : VAR LBRACKET expression RBRACKET
	"""
	#p[0] = (p[1],var_address_colum_line(p[1],p[3],0),var_type(p[1]))

	p[0] = ('PUSHGP\n' + f'PUSHI {var_address_base(p[1])}\n' + p[3][0] + 'ADD\n',var_type(p[1]),var_size(p[1])) 
	


def p_variable_index_expression_expression(p):
	"""
	variable : VAR LBRACKET expression RBRACKET LBRACKET expression RBRACKET
	"""
	#p[0] = (p[1],var_address_colum_line(p[1],p[3],0),var_type(p[1]))

	p[0] = ('PUSHGP\n' + f'PUSHI {var_address_base(p[1])}\n' + f'PUSHI {var_num_colums(p[1])}\n' + p[3][0] + 'MUL\n' + 'ADD\n' + p[6][0] + 'ADD\n',var_type(p[1]),var_size(p[1])) 




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
	
	if p[1][1] == None:
		p[0] = f'ERR \"segmentation fault\\n\"\nSTOP\n'
	
	elif p[1][1] == 'int' and p[3][1] == 'float':
		p[0] = p[1][0] + p[3][0]+ 'FTOI\n' + 'STOREN\n'
	
	elif p[1][1] == 'float' and p[3][1] == 'int':
		p[0] = p[1][0] + p[3][0]+ 'ITOF\n'  + 'STOREN\n'

	else:
		p[0] = p[1][0] + p[3][0] +  'STOREN\n'







def p_instruction_atribution_condition(p):
	"""
	instruction : variable EQUAL condition SEMICOLON
	"""
	
	if p[1][1] == None:
		p[0] = f'ERR \"segmentation fault\\n\"\nSTOP\n'
	else:
		p[0] = p[1][0] + p[3] + 'STOREN\n'




	


def p_expression_var(p):
	"""
	expression : variable
	"""
	
	if p[1][1] == None:
		p[0] = f'ERR \"segmentation fault\\n\"\nSTOP\n'
	else:
		p[0] = (p[1][0] + 'LOADN\n',p[1][1])







def p_expression_num(p):
	"""
	expression : NUM
	"""
	p[0] = (f'PUSHI {p[1]}\n','int')

def p_expression_float(p):
	"""
	expression : REAL
	"""
	p[0] = (f'PUSHF {p[1]}\n','float')


def p_expression_between_parenthesis(p):
	"""
	expression : LPAREN expression RPAREN
	"""
	p[0] = p[2]





def p_expression_plus_expression(p):
	"""
	expression : expression PLUS expression
	"""
	if p[1][1] == 'int' and p[3][1] == 'int':
		p[0] = (p[1][0] + p[3][0] + 'ADD\n','int')
	
	elif p[1][1] == 'float' and p[3][1] == 'float':
		p[0] = (p[1][0] + p[3][0] + 'FADD\n','float')

	
	elif p[1][1] == 'int' and p[3][1] == 'float':
		p[0] = (p[1][0] + 'ITOF\n' + p[3][0] + 'FADD\n','float')
	
	else:
		p[0] = (p[1][0] + p[3][0] + 'ITOF\n' +'FADD\n','float')





def p_expression_minus_expression(p):
	"""
	expression : expression MINUS expression
	"""
	if p[1][1] == 'int' and p[3][1] == 'int':
		p[0] = (p[1][0] + p[3][0] + 'SUB\n','int')
	
	elif p[1][1] == 'float' and p[3][1] == 'float':
		p[0] = (p[1][0] + p[3][0] + 'FSUB\n','float')

	
	elif p[1][1] == 'int' and p[3][1] == 'float':
		p[0] = (p[1][0] + 'ITOF\n' + p[3][0] + 'FSUB\n','float')
	
	else:
		p[0] = (p[1][0] + p[3][0] + 'ITOF\n' +'FSUB\n','float')


def p_expression_mul_expression(p):
	"""
	expression : expression MUL expression
	"""
	if p[1][1] == 'int' and p[3][1] == 'int':
		p[0] = (p[1][0] + p[3][0] + 'MUL\n','int')
	
	elif p[1][1] == 'float' and p[3][1] == 'float':
		p[0] = (p[1][0] + p[3][0] + 'FMUL\n','float')

	
	elif p[1][1] == 'int' and p[3][1] == 'float':
		p[0] = (p[1][0] + 'ITOF\n' + p[3][0] + 'FMUL\n','float')
	
	else:
		p[0] = (p[1][0] + p[3][0] + 'ITOF\n' +'FMUL\n','float')


def p_expression_div_expression(p):
	"""
	expression : expression DIV expression
	"""
	if p[1][1] == 'int' and p[3][1] == 'int':
		p[0] = (p[1][0] + p[3][0] + 'DIV\n','int')
	
	elif p[1][1] == 'float' and p[3][1] == 'float':
		p[0] = (p[1][0] + p[3][0] + 'FDIV\n','float')

	
	elif p[1][1] == 'int' and p[3][1] == 'float':
		p[0] = (p[1][0] + 'ITOF\n' + p[3][0] + 'FDIV\n','float')
	
	else:
		p[0] = (p[1][0] + p[3][0] + 'ITOF\n' +'FDIV\n','float')


def p_expression_mod_expression(p):
	"""
	expression : expression MOD expression
	"""
	p[0] = (p[1][0] + p[3][0] + 'MOD\n','int')


def p_instruction_cicle(p):
	"""
	instruction : WHILE LPAREN condition RPAREN LCURLY instructions RCURLY
	"""
	p[0] = f'B{parser.labels}:\n' + p[3] + 'JZ ' + f'E{parser.labels}\n' + p[6] + f'JUMP B{parser.labels}\n' + f'E{parser.labels}:\n' 
	parser.labels +=1



def p_instruction_conditional_if(p):
	"""
	instruction : IF LPAREN condition RPAREN LCURLY instructions RCURLY
	"""
	p[0] = p[3] + 'JZ '+ f'E{parser.labels}\n' + p[6] + f'E{parser.labels}:\n' 
	parser.labels +=1

def p_instruction_conditional_if_else(p):
	"""
	instruction : IF LPAREN condition RPAREN LCURLY instructions RCURLY ELSE LCURLY instructions RCURLY
	"""
	p[0] = p[3] + 'JZ '+ f'E{parser.labels}\n' + p[6] + f'JUMP F{parser.labels}\n'  + f'E{parser.labels}:\n' + p[10] + f'F{parser.labels}:\n' 
	parser.labels +=1

	


def p_condition_expression_eqeq_expression(p):
	"""
	condition : expression EQEQ expression
	"""

	if p[1][1] == 'int' and p[3][1] == 'float':
		p[0] = p[1][0] + 'ITOF\n' + p[3][0] + 'EQUAL\n'
	
	elif p[1][1] == 'float' and p[3][1] == 'int':
		p[0] = p[1][0] + p[3][0] + 'ITOF\n' + 'EQUAL\n'

	else:
		p[0] = p[1][0] + p[3][0] + 'EQUAL\n'
	




def p_condition_expression_diff_expression(p):
	"""
	condition : expression DIFF expression
	"""

	if p[1][1] == 'int' and p[3][1] == 'float':
		p[0] = p[1][0] + 'ITOF\n' + p[3][0] + 'EQUAL\nNOT\n'
	
	elif p[1][1] == 'float' and p[3][1] == 'int':
		p[0] = p[1][0] + p[3][0] + 'ITOF\n' + 'EQUAL\nNOT\n'

	else:
		p[0] = p[1][0] + p[3][0] + 'EQUAL\nNOT\n'

def p_condition_expression_greater_expression(p):
	"""
	condition : expression GREATER expression
	"""

	if p[1][1] == 'float' and p[3][1] == 'float':
		p[0] = p[1][0] + p[3][0] + 'FSUP\n' + 'FTOI\n'

	elif p[1][1] == 'int' and p[3][1] == 'float':
		p[0] = p[1][0] + 'ITOF\n' + p[3][0] + 'FSUP\n' + 'FTOI\n'
	
	elif p[1][1] == 'float' and p[3][1] == 'int':
		p[0] = p[1][0] + p[3][0] + 'ITOF\n' + 'FSUP\n' + 'FTOI\n'

	else:
		p[0] = p[1][0] + p[3][0] + 'SUP\n'


def p_condition_expression_lesser_expression(p):
	"""
	condition : expression LESSER expression
	"""
	if p[1][1] == 'float' and p[3][1] == 'float':
		p[0] = p[1][0] + p[3][0] + 'FINF\n' + 'FTOI\n'

	elif p[1][1] == 'int' and p[3][1] == 'float':
		p[0] = p[1][0] + 'ITOF\n' + p[3][0] + 'FINF\n' + 'FTOI\n'
	
	elif p[1][1] == 'float' and p[3][1] == 'int':
		p[0] = p[1][0] + p[3][0] + 'ITOF\n' + 'FINF\n' + 'FTOI\n'

	else:
		p[0] = p[1][0] + p[3][0] + 'INF\n'

def p_condition_expression_greateq_expression(p):
	"""
	condition : expression GREATEQ expression
	"""
	if p[1][1] == 'float' and p[3][1] == 'float':
		p[0] = p[1][0] + p[3][0] + 'FSUPEQ\n' + 'FTOI\n'

	elif p[1][1] == 'int' and p[3][1] == 'float':
		p[0] = p[1][0] + 'ITOF\n' + p[3][0] + 'FSUPEQ\n' + 'FTOI\n'
	
	elif p[1][1] == 'float' and p[3][1] == 'int':
		p[0] = p[1][0] + p[3][0] + 'ITOF\n' + 'FSUPEQ\n' + 'FTOI\n'

	else:
		p[0] = p[1][0] + p[3][0] + 'SUPEQ\n'

def p_condition_expression_lesseq_expression(p):
	"""
	condition : expression LESSEQ expression
	"""
	if p[1][1] == 'float' and p[3][1] == 'float':
		p[0] = p[1][0] + p[3][0] + 'FINFEQ\n' + 'FTOI\n'

	elif p[1][1] == 'int' and p[3][1] == 'float':
		p[0] = p[1][0] + 'ITOF\n' + p[3][0] + 'FINFEQ\n' + 'FTOI\n'
	
	elif p[1][1] == 'float' and p[3][1] == 'int':
		p[0] = p[1][0] + p[3][0] + 'ITOF\n' + 'FINFEQ\n' + 'FTOI\n'

	else:
		p[0] = p[1][0] + p[3][0] + 'INFEQ\n'



def p_condition_num(p):
	"""
	condition : NUM
	"""
	p[0] = f'PUSHI {p[1]}\n'

def p_condition_var(p):
	"""
	condition : variable
	"""

	if p[1][1] == None:
		p[0] = f'ERR \"segmentation fault\\n\"\nSTOP\n'
	elif p[1][1] == 'float':
		
		p[0] = p[1][0] + 'LOADN\nFTOI\nPUSHI 0\nEQUAL\nNOT\n'
	else:
		p[0] = p[1][0] + 'LOADN\nPUSHI 0\nEQUAL\nNOT\n'





def p_instruction_scan(p):
	"""
	instruction : SCAN LPAREN variable RPAREN SEMICOLON
	"""

	if p[3][1] == None:
		p[0] = f'ERR \"segmentation fault\\n\"\nSTOP\n'
	elif p[3][1] == 'int':
		p[0] = p[3][0]  + 'READ\nATOI\nSTOREN\n'
	else:
		p[0] = p[3][0]  + 'READ\nATOF\nSTOREN\n'
	



def p_instruction_print_var(p):
	"""
	instruction : PRINT LPAREN variable RPAREN SEMICOLON
	"""
	if p[3][1] == None:
		p[0] = f'ERR \"segmentation fault\\n\"\nSTOP\n'
	elif p[3][1] == 'int':
		p[0] = p[3][0]  + 'LOADN\nWRITEI\n'
	else:
		p[0] = p[3][0]  + 'LOADN\nWRITEF\n'








def p_instruction_println_var(p):
	"""
	instruction : PRINTLN LPAREN variable RPAREN SEMICOLON
	"""
	if p[3][1] == None:
		p[0] = f'ERR \"segmentation fault\\n\"\nSTOP\n'
	elif p[3][1] == 'int':
		p[0] = p[3][0]  + 'LOADN\nWRITEI\n'
		p[0] += 'PUSHS\"\\n\"\nWRITES\n'
	else:
		p[0] = p[3][0]  + 'LOADN\nWRITEF\n'
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

parser.prox_address = 0
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

