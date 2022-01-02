import ply.lex as lex
import sys


tokens = ('LCURLY','RCURLY','LPAREN','RPAREN','LBRACKET','RBRACKET','NUM','REAL','VAR','TRUE','FALSE','BOOL','INT','SEMICOLON','MAIN','WHILE','IF','STRING',
	'EQUAL','PLUS','MINUS','MUL','DIV','EQEQ','DIFF','GREATER','LESSER','GREATEQ','LESSEQ','INPUT','PRINT')




def t_SEMICOLON(t):
	r';'
	return t

def t_LCURLY(t):
	r'\{'
	return t

def t_RCURLY(t):
	r'\}'
	return t

def t_LPAREN(t):
	r'\('
	return t

def t_RPAREN(t):
	r'\)'
	return t


def t_LBRACKET(t):
	r'\['
	return t

def t_RBRACKET(t):
	r'\]'
	return t


def t_BOOL(t):
	r'bool'
	return t

def t_INT(t):
	r'int'
	return t


def t_TRUE(t):
    r'True'
    return t

def t_FALSE(t):
    r'False'
    return t

def t_MAIN(t):
	r'main'
	return t

def t_WHILE(t):
	r'while'
	return t

def t_IF(t):
	r'if'
	return t

def t_PRINT(t):
	r'print'
	return t

def t_INPUT(t):
	r'input'
	return t


def t_STRING(t):
	r'"([^"]|[\\"])*"'
	return t


def t_REAL(t):
    r'([1-9][0-9]*\.[0-9]+|0\.[0-9]+)'
    return t


def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_EQEQ(t):
	r'(\=\=)'
	return t

def t_DIFF(t):
	r'\!\='
	return t

def t_GREAEQ(t):
	r'\>\='
	return t

def t_LESSEQ(t):
	r'\<\='
	return t

def t_GREATER(t):
	r'\>'
	return t

def t_LESSER(t):
	r'\<'
	return t

def t_EQUAL(t):
	r'\='
	return t

def t_PLUS(t):
	r'\+'
	return t

def t_MINUS(t):
	r'\-'
	return t

def t_MUL(t):
	r'\*'
	return t

def t_DIV(t):
	r'\/'
	return t

def t_VAR(t):
	r'\w+'
	return t


def t_error(t):
	print("Illegal Character:", t.value[0])
	t.lexer.skip(1)

t_ignore = ' \r\n\t'

lexer = lex.lex()


#for linha in sys.stdin:
#	lexer.input(linha) 
#	for tok in lexer:
#		print(tok)
#		pass