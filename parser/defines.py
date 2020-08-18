# -*- coding: utf-8 -*-


TOKEN_PROP_ADDRESS_TYPE = 'address_type'
TOKEN_PROP_DATE_TYPE = 'type'
TOKEN_PROP_LEXEME = 'lexeme'
TOKEN_PROP_VALUE = 'value'


SYMBOL_COMMA = ','
SYMBOL_DATA_TYPE = 'data_type'
SYMBOL_END = '#'
SYMBOL_IF = 'if'
SYMBOL_LBRACE = '{'
SYMBOL_LBRACKET = '['
SYMBOL_LPRENE = '('
SYMBOL_RBRACE = '}'
SYMBOL_RBRACKET = ']'
SYMBOL_RETURN = 'return'
SYMBOL_RPRENE = ')'
SYMBOL_SEMICOLON = ';'
SYMBOL_START = '$START'
SYMBOL_VAR_ID = 'var_id'
SYMBOL_WHILE = 'while'


CMD_FJ = 0
CMD_INIT_ARRAY = 1
CMD_JUMP = 2
CMD_PUSH_ANY = 3
CMD_PUSH_FROM_ADDRESS = 4
CMD_PUSH_FROM_SEGMENT = 5
CMD_RETURN = 6
CMD_RUN = 7
CMD_SET_TO_ARRAY = 8


DATA_TYPE_ADDRESS = 0
DATA_TYPE_CHAR = 1
DATA_TYPE_FLOAT = 2
DATA_TYPE_INT = 3
DATA_TYPE_VOID = 4
DATA_TYPE_SYMBOL = {
	DATA_TYPE_ADDRESS: 'address', 
	DATA_TYPE_CHAR: 'char', 
	DATA_TYPE_FLOAT: 'float', 
	DATA_TYPE_INT: 'int', 
	DATA_TYPE_VOID: 'void', 
}
DATA_TYPE_VALUE_SYMBOL = {
	DATA_TYPE_ADDRESS: 'address_value', 
	DATA_TYPE_CHAR: 'char_value', 
	DATA_TYPE_FLOAT: 'float_value', 
	DATA_TYPE_INT: 'int_value', 
	DATA_TYPE_VOID: 'void_value', 
}
DATA_TYPE_SIZE = {
	DATA_TYPE_ADDRESS: 4, 
	DATA_TYPE_CHAR: 1, 
	DATA_TYPE_FLOAT: 4, 
	DATA_TYPE_INT: 4, 
	DATA_TYPE_VOID: 0, 
}
ALL_DATA_TYPE = [
	DATA_TYPE_ADDRESS, 
	DATA_TYPE_CHAR, 
	DATA_TYPE_FLOAT, 
	DATA_TYPE_INT, 
	DATA_TYPE_VOID, 
]


CMD_PUSH_ADDRESS = 9
CMD_PUSH_CHAR = 10
CMD_PUSH_FLOAT = 11
CMD_PUSH_INT = 12
CMD_PUSH_VOID = 13
DATA_TYPE_2_PUSH_DATA_CMD = {
	DATA_TYPE_ADDRESS: CMD_PUSH_ADDRESS, 
	DATA_TYPE_CHAR: CMD_PUSH_CHAR, 
	DATA_TYPE_FLOAT: CMD_PUSH_FLOAT, 
	DATA_TYPE_INT: CMD_PUSH_INT, 
	DATA_TYPE_VOID: CMD_PUSH_VOID, 
}


SYMBOL_PRINT = 'print'
CMD_PRINT_ADDRESS = 14
CMD_PRINT_CHAR = 15
CMD_PRINT_FLOAT = 16
CMD_PRINT_INT = 17
CMD_PRINT_VOID = 18
DATA_TYPE_2_PRINT_CMD = {
	DATA_TYPE_ADDRESS: CMD_PRINT_ADDRESS, 
	DATA_TYPE_CHAR: CMD_PRINT_CHAR, 
	DATA_TYPE_FLOAT: CMD_PRINT_FLOAT, 
	DATA_TYPE_INT: CMD_PRINT_INT, 
	DATA_TYPE_VOID: CMD_PRINT_VOID, 
}


SYMBOL_ADD = '+'
CMD_ADD_CHAR_CHAR = 19
CMD_ADD_CHAR_INT = 20
CMD_ADD_CHAR_FLOAT = 21
CMD_ADD_INT_CHAR = 22
CMD_ADD_INT_INT = 23
CMD_ADD_INT_FLOAT = 24
CMD_ADD_FLOAT_CHAR = 25
CMD_ADD_FLOAT_INT = 26
CMD_ADD_FLOAT_FLOAT = 27
CMD_ADD_ADDRESS_INT = 28


SYMBOL_ADDRESS = '&'
CMD_ADDRESS_CHAR = 29
CMD_ADDRESS_INT = 30
CMD_ADDRESS_FLOAT = 31


SYMBOL_EQ = '=='
CMD_EQ_CHAR_CHAR = 32
CMD_EQ_CHAR_INT = 33
CMD_EQ_CHAR_FLOAT = 34
CMD_EQ_INT_CHAR = 35
CMD_EQ_INT_INT = 36
CMD_EQ_INT_FLOAT = 37
CMD_EQ_FLOAT_CHAR = 38
CMD_EQ_FLOAT_INT = 39
CMD_EQ_FLOAT_FLOAT = 40
CMD_EQ_ADDRESS_ADDRESS = 41


SYMBOL_LT = '<'
CMD_LT_CHAR_CHAR = 42
CMD_LT_CHAR_INT = 43
CMD_LT_CHAR_FLOAT = 44
CMD_LT_INT_CHAR = 45
CMD_LT_INT_INT = 46
CMD_LT_INT_FLOAT = 47
CMD_LT_FLOAT_CHAR = 48
CMD_LT_FLOAT_INT = 49
CMD_LT_FLOAT_FLOAT = 50


SYMBOL_MUL = '*'
CMD_MUL_CHAR_CHAR = 51
CMD_MUL_CHAR_INT = 52
CMD_MUL_CHAR_FLOAT = 53
CMD_MUL_INT_CHAR = 54
CMD_MUL_INT_INT = 55
CMD_MUL_INT_FLOAT = 56
CMD_MUL_FLOAT_CHAR = 57
CMD_MUL_FLOAT_INT = 58
CMD_MUL_FLOAT_FLOAT = 59


SYMBOL_NOT = '!'
CMD_NOT_CHAR = 60


SYMBOL_SET = '='
CMD_SET_CHAR_CHAR = 61
CMD_SET_CHAR_INT = 62
CMD_SET_CHAR_FLOAT = 63
CMD_SET_INT_CHAR = 64
CMD_SET_INT_INT = 65
CMD_SET_INT_FLOAT = 66
CMD_SET_FLOAT_CHAR = 67
CMD_SET_FLOAT_INT = 68
CMD_SET_FLOAT_FLOAT = 69
CMD_SET_ADDRESS_ADDRESS = 70
OPERATOR_CMD = {
	(SYMBOL_MUL, DATA_TYPE_INT, DATA_TYPE_CHAR): CMD_MUL_INT_CHAR, 
	(SYMBOL_EQ, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT): CMD_EQ_FLOAT_FLOAT, 
	(SYMBOL_SET, DATA_TYPE_INT, DATA_TYPE_INT): CMD_SET_INT_INT, 
	(SYMBOL_ADDRESS, None, DATA_TYPE_CHAR): CMD_ADDRESS_CHAR, 
	(SYMBOL_SET, DATA_TYPE_INT, DATA_TYPE_FLOAT): CMD_SET_INT_FLOAT, 
	(SYMBOL_EQ, DATA_TYPE_INT, DATA_TYPE_FLOAT): CMD_EQ_INT_FLOAT, 
	(SYMBOL_ADDRESS, None, DATA_TYPE_FLOAT): CMD_ADDRESS_FLOAT, 
	(SYMBOL_MUL, DATA_TYPE_CHAR, DATA_TYPE_FLOAT): CMD_MUL_CHAR_FLOAT, 
	(SYMBOL_ADD, DATA_TYPE_ADDRESS, DATA_TYPE_INT): CMD_ADD_ADDRESS_INT, 
	(SYMBOL_EQ, DATA_TYPE_INT, DATA_TYPE_INT): CMD_EQ_INT_INT, 
	(SYMBOL_SET, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT): CMD_SET_FLOAT_FLOAT, 
	(SYMBOL_ADDRESS, None, DATA_TYPE_INT): CMD_ADDRESS_INT, 
	(SYMBOL_SET, DATA_TYPE_CHAR, DATA_TYPE_INT): CMD_SET_CHAR_INT, 
	(SYMBOL_LT, DATA_TYPE_INT, DATA_TYPE_FLOAT): CMD_LT_INT_FLOAT, 
	(SYMBOL_SET, DATA_TYPE_FLOAT, DATA_TYPE_INT): CMD_SET_FLOAT_INT, 
	(SYMBOL_LT, DATA_TYPE_INT, DATA_TYPE_CHAR): CMD_LT_INT_CHAR, 
	(SYMBOL_SET, DATA_TYPE_CHAR, DATA_TYPE_FLOAT): CMD_SET_CHAR_FLOAT, 
	(SYMBOL_EQ, DATA_TYPE_INT, DATA_TYPE_CHAR): CMD_EQ_INT_CHAR, 
	(SYMBOL_ADD, DATA_TYPE_CHAR, DATA_TYPE_FLOAT): CMD_ADD_CHAR_FLOAT, 
	(SYMBOL_EQ, DATA_TYPE_ADDRESS, DATA_TYPE_ADDRESS): CMD_EQ_ADDRESS_ADDRESS, 
	(SYMBOL_SET, DATA_TYPE_CHAR, DATA_TYPE_CHAR): CMD_SET_CHAR_CHAR, 
	(SYMBOL_MUL, DATA_TYPE_CHAR, DATA_TYPE_INT): CMD_MUL_CHAR_INT, 
	(SYMBOL_ADD, DATA_TYPE_FLOAT, DATA_TYPE_INT): CMD_ADD_FLOAT_INT, 
	(SYMBOL_LT, DATA_TYPE_INT, DATA_TYPE_INT): CMD_LT_INT_INT, 
	(SYMBOL_ADD, DATA_TYPE_CHAR, DATA_TYPE_INT): CMD_ADD_CHAR_INT, 
	(SYMBOL_ADD, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT): CMD_ADD_FLOAT_FLOAT, 
	(SYMBOL_MUL, DATA_TYPE_CHAR, DATA_TYPE_CHAR): CMD_MUL_CHAR_CHAR, 
	(SYMBOL_MUL, DATA_TYPE_FLOAT, DATA_TYPE_CHAR): CMD_MUL_FLOAT_CHAR, 
	(SYMBOL_ADD, DATA_TYPE_FLOAT, DATA_TYPE_CHAR): CMD_ADD_FLOAT_CHAR, 
	(SYMBOL_ADD, DATA_TYPE_CHAR, DATA_TYPE_CHAR): CMD_ADD_CHAR_CHAR, 
	(SYMBOL_MUL, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT): CMD_MUL_FLOAT_FLOAT, 
	(SYMBOL_MUL, DATA_TYPE_FLOAT, DATA_TYPE_INT): CMD_MUL_FLOAT_INT, 
	(SYMBOL_LT, DATA_TYPE_CHAR, DATA_TYPE_FLOAT): CMD_LT_CHAR_FLOAT, 
	(SYMBOL_LT, DATA_TYPE_FLOAT, DATA_TYPE_INT): CMD_LT_FLOAT_INT, 
	(SYMBOL_LT, DATA_TYPE_CHAR, DATA_TYPE_CHAR): CMD_LT_CHAR_CHAR, 
	(SYMBOL_EQ, DATA_TYPE_CHAR, DATA_TYPE_CHAR): CMD_EQ_CHAR_CHAR, 
	(SYMBOL_SET, DATA_TYPE_ADDRESS, DATA_TYPE_ADDRESS): CMD_SET_ADDRESS_ADDRESS, 
	(SYMBOL_LT, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT): CMD_LT_FLOAT_FLOAT, 
	(SYMBOL_EQ, DATA_TYPE_CHAR, DATA_TYPE_FLOAT): CMD_EQ_CHAR_FLOAT, 
	(SYMBOL_LT, DATA_TYPE_FLOAT, DATA_TYPE_CHAR): CMD_LT_FLOAT_CHAR, 
	(SYMBOL_SET, DATA_TYPE_FLOAT, DATA_TYPE_CHAR): CMD_SET_FLOAT_CHAR, 
	(SYMBOL_EQ, DATA_TYPE_CHAR, DATA_TYPE_INT): CMD_EQ_CHAR_INT, 
	(SYMBOL_NOT, None, DATA_TYPE_CHAR): CMD_NOT_CHAR, 
	(SYMBOL_ADD, DATA_TYPE_INT, DATA_TYPE_CHAR): CMD_ADD_INT_CHAR, 
	(SYMBOL_EQ, DATA_TYPE_FLOAT, DATA_TYPE_CHAR): CMD_EQ_FLOAT_CHAR, 
	(SYMBOL_MUL, DATA_TYPE_INT, DATA_TYPE_INT): CMD_MUL_INT_INT, 
	(SYMBOL_ADD, DATA_TYPE_INT, DATA_TYPE_FLOAT): CMD_ADD_INT_FLOAT, 
	(SYMBOL_SET, DATA_TYPE_INT, DATA_TYPE_CHAR): CMD_SET_INT_CHAR, 
	(SYMBOL_MUL, DATA_TYPE_INT, DATA_TYPE_FLOAT): CMD_MUL_INT_FLOAT, 
	(SYMBOL_ADD, DATA_TYPE_INT, DATA_TYPE_INT): CMD_ADD_INT_INT, 
	(SYMBOL_EQ, DATA_TYPE_FLOAT, DATA_TYPE_INT): CMD_EQ_FLOAT_INT, 
	(SYMBOL_LT, DATA_TYPE_CHAR, DATA_TYPE_INT): CMD_LT_CHAR_INT, 
}
OPERATOR1 = [
	SYMBOL_ADD, 
	SYMBOL_ADDRESS, 
	SYMBOL_LT, 
	SYMBOL_MUL, 
	SYMBOL_NOT, 
	SYMBOL_SET, 
]
OPERATOR2 = [
	SYMBOL_EQ, 
]


CMD_SIZE = {
	CMD_SET_CHAR_INT: 1, 
	CMD_MUL_INT_FLOAT: 1, 
	CMD_MUL_FLOAT_FLOAT: 1, 
	CMD_SET_FLOAT_FLOAT: 1, 
	CMD_MUL_INT_INT: 1, 
	CMD_LT_CHAR_FLOAT: 1, 
	CMD_RUN: 9, 
	CMD_LT_INT_INT: 1, 
	CMD_LT_FLOAT_INT: 1, 
	CMD_MUL_FLOAT_CHAR: 1, 
	CMD_EQ_INT_INT: 1, 
	CMD_PUSH_VOID: 1, 
	CMD_LT_INT_FLOAT: 1, 
	CMD_MUL_CHAR_CHAR: 1, 
	CMD_PUSH_ADDRESS: 5, 
	CMD_LT_CHAR_CHAR: 1, 
	CMD_LT_CHAR_INT: 1, 
	CMD_EQ_FLOAT_CHAR: 1, 
	CMD_ADDRESS_CHAR: 1, 
	CMD_ADD_CHAR_FLOAT: 1, 
	CMD_ADD_FLOAT_FLOAT: 1, 
	CMD_MUL_CHAR_INT: 1, 
	CMD_SET_INT_INT: 1, 
	CMD_EQ_CHAR_CHAR: 1, 
	CMD_ADD_ADDRESS_INT: 1, 
	CMD_INIT_ARRAY: 5, 
	CMD_RETURN: 9, 
	CMD_PRINT_ADDRESS: 1, 
	CMD_ADD_FLOAT_INT: 1, 
	CMD_SET_ADDRESS_ADDRESS: 1, 
	CMD_LT_INT_CHAR: 1, 
	CMD_PRINT_INT: 1, 
	CMD_MUL_FLOAT_INT: 1, 
	CMD_SET_INT_FLOAT: 1, 
	CMD_ADD_FLOAT_CHAR: 1, 
	CMD_EQ_INT_CHAR: 1, 
	CMD_ADD_CHAR_CHAR: 1, 
	CMD_PUSH_ANY: 5, 
	CMD_ADD_INT_CHAR: 1, 
	CMD_NOT_CHAR: 1, 
	CMD_EQ_FLOAT_INT: 1, 
	CMD_EQ_CHAR_INT: 1, 
	CMD_SET_CHAR_FLOAT: 1, 
	CMD_ADD_INT_FLOAT: 1, 
	CMD_PUSH_FROM_ADDRESS: 5, 
	CMD_ADDRESS_FLOAT: 1, 
	CMD_SET_TO_ARRAY: 5, 
	CMD_ADD_INT_INT: 1, 
	CMD_PUSH_FLOAT: 5, 
	CMD_SET_FLOAT_INT: 1, 
	CMD_EQ_CHAR_FLOAT: 1, 
	CMD_LT_FLOAT_FLOAT: 1, 
	CMD_ADDRESS_INT: 1, 
	CMD_PRINT_CHAR: 1, 
	CMD_PUSH_CHAR: 2, 
	CMD_EQ_INT_FLOAT: 1, 
	CMD_SET_INT_CHAR: 1, 
	CMD_JUMP: 5, 
	CMD_PRINT_FLOAT: 1, 
	CMD_ADD_CHAR_INT: 1, 
	CMD_LT_FLOAT_CHAR: 1, 
	CMD_MUL_CHAR_FLOAT: 1, 
	CMD_PUSH_INT: 5, 
	CMD_EQ_ADDRESS_ADDRESS: 1, 
	CMD_SET_CHAR_CHAR: 1, 
	CMD_FJ: 5, 
	CMD_EQ_FLOAT_FLOAT: 1, 
	CMD_SET_FLOAT_CHAR: 1, 
	CMD_PRINT_VOID: 1, 
	CMD_PUSH_FROM_SEGMENT: 5, 
	CMD_MUL_INT_CHAR: 1, 
}


CMD_RETURN_DATA_TYPE = {
	CMD_SET_CHAR_INT: DATA_TYPE_INT, 
	CMD_MUL_INT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_MUL_FLOAT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_SET_FLOAT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_LT_CHAR_FLOAT: DATA_TYPE_CHAR, 
	CMD_LT_INT_INT: DATA_TYPE_CHAR, 
	CMD_LT_FLOAT_INT: DATA_TYPE_CHAR, 
	CMD_EQ_INT_INT: DATA_TYPE_CHAR, 
	CMD_LT_INT_FLOAT: DATA_TYPE_CHAR, 
	CMD_MUL_CHAR_CHAR: DATA_TYPE_CHAR, 
	CMD_LT_CHAR_CHAR: DATA_TYPE_CHAR, 
	CMD_LT_CHAR_INT: DATA_TYPE_CHAR, 
	CMD_EQ_FLOAT_CHAR: DATA_TYPE_CHAR, 
	CMD_MUL_INT_INT: DATA_TYPE_INT, 
	CMD_ADD_CHAR_FLOAT: DATA_TYPE_FLOAT, 
	CMD_ADD_FLOAT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_MUL_CHAR_INT: DATA_TYPE_INT, 
	CMD_SET_INT_INT: DATA_TYPE_INT, 
	CMD_EQ_CHAR_CHAR: DATA_TYPE_CHAR, 
	CMD_ADD_ADDRESS_INT: DATA_TYPE_ADDRESS, 
	CMD_MUL_FLOAT_CHAR: DATA_TYPE_FLOAT, 
	CMD_ADDRESS_CHAR: DATA_TYPE_ADDRESS, 
	CMD_SET_CHAR_CHAR: DATA_TYPE_CHAR, 
	CMD_SET_ADDRESS_ADDRESS: DATA_TYPE_ADDRESS, 
	CMD_MUL_FLOAT_INT: DATA_TYPE_FLOAT, 
	CMD_ADD_FLOAT_CHAR: DATA_TYPE_FLOAT, 
	CMD_EQ_INT_CHAR: DATA_TYPE_CHAR, 
	CMD_ADD_CHAR_CHAR: DATA_TYPE_CHAR, 
	CMD_ADD_INT_CHAR: DATA_TYPE_INT, 
	CMD_NOT_CHAR: DATA_TYPE_CHAR, 
	CMD_EQ_FLOAT_INT: DATA_TYPE_CHAR, 
	CMD_EQ_CHAR_INT: DATA_TYPE_CHAR, 
	CMD_SET_CHAR_FLOAT: DATA_TYPE_FLOAT, 
	CMD_ADD_INT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_ADDRESS_FLOAT: DATA_TYPE_ADDRESS, 
	CMD_SET_INT_CHAR: DATA_TYPE_INT, 
	CMD_ADD_INT_INT: DATA_TYPE_INT, 
	CMD_SET_FLOAT_INT: DATA_TYPE_FLOAT, 
	CMD_EQ_CHAR_FLOAT: DATA_TYPE_CHAR, 
	CMD_LT_FLOAT_FLOAT: DATA_TYPE_CHAR, 
	CMD_ADDRESS_INT: DATA_TYPE_ADDRESS, 
	CMD_LT_INT_CHAR: DATA_TYPE_CHAR, 
	CMD_EQ_INT_FLOAT: DATA_TYPE_CHAR, 
	CMD_ADD_FLOAT_INT: DATA_TYPE_FLOAT, 
	CMD_ADD_CHAR_INT: DATA_TYPE_INT, 
	CMD_LT_FLOAT_CHAR: DATA_TYPE_CHAR, 
	CMD_MUL_CHAR_FLOAT: DATA_TYPE_FLOAT, 
	CMD_EQ_ADDRESS_ADDRESS: DATA_TYPE_CHAR, 
	CMD_SET_INT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_EQ_FLOAT_FLOAT: DATA_TYPE_CHAR, 
	CMD_SET_FLOAT_CHAR: DATA_TYPE_FLOAT, 
	CMD_MUL_INT_CHAR: DATA_TYPE_INT, 
}
