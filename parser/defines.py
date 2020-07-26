# -*- coding: utf-8 -*-


TOKEN_PROP_DATE_TYPE = 'type'
TOKEN_PROP_LEXEME = 'lexeme'
TOKEN_PROP_VALUE = 'value'


SYMBOL_END = '#'
SYMBOL_LBRACKET = '{'
SYMBOL_LPRENE = '('
SYMBOL_RBRACKET = '}'
SYMBOL_RPRENE = ')'
SYMBOL_SEMICOLON = ';'
SYMBOL_START = '$START'
SYMBOL_VAR_ID = 'var_id'
SYMBOL_WHILE = 'while'


CMD_FJ = 0
CMD_JUMP = 1
CMD_RETURN = 2
CMD_RUN = 3


DATA_TYPE_CHAR = 0
DATA_TYPE_FLOAT = 1
DATA_TYPE_INT = 2
DATA_TYPE_SYMBOL = {
	DATA_TYPE_CHAR: 'char', 
	DATA_TYPE_FLOAT: 'float', 
	DATA_TYPE_INT: 'int', 
}
DATA_TYPE_VALUE_SYMBOL = {
	DATA_TYPE_CHAR: 'char_value', 
	DATA_TYPE_FLOAT: 'float_value', 
	DATA_TYPE_INT: 'int_value', 
}
DATA_TYPE_SIZE = {
	DATA_TYPE_CHAR: 1, 
	DATA_TYPE_FLOAT: 4, 
	DATA_TYPE_INT: 4, 
}
ALL_DATA_TYPE = [
	DATA_TYPE_CHAR, 
	DATA_TYPE_FLOAT, 
	DATA_TYPE_INT, 
]


CMD_PUSH_CHAR = 4
CMD_PUSH_FLOAT = 5
CMD_PUSH_INT = 6
DATA_TYPE_2_PUSH_DATA_CMD = {
	DATA_TYPE_CHAR: CMD_PUSH_CHAR, 
	DATA_TYPE_FLOAT: CMD_PUSH_FLOAT, 
	DATA_TYPE_INT: CMD_PUSH_INT, 
}


CMD_PUSH_SEGMENT_CHAR = 7
CMD_PUSH_SEGMENT_FLOAT = 8
CMD_PUSH_SEGMENT_INT = 9
DATA_TYPE_2_PUSH_SEGMENT_DATA_CMD = {
	DATA_TYPE_CHAR: CMD_PUSH_SEGMENT_CHAR, 
	DATA_TYPE_FLOAT: CMD_PUSH_SEGMENT_FLOAT, 
	DATA_TYPE_INT: CMD_PUSH_SEGMENT_INT, 
}


SYMBOL_PRINT = 'print'
CMD_PRINT_CHAR = 10
CMD_PRINT_FLOAT = 11
CMD_PRINT_INT = 12
DATA_TYPE_2_PRINT_CMD = {
	DATA_TYPE_CHAR: CMD_PRINT_CHAR, 
	DATA_TYPE_FLOAT: CMD_PRINT_FLOAT, 
	DATA_TYPE_INT: CMD_PRINT_INT, 
}


SYMBOL_ADD = '+'
CMD_ADD_CHAR_CHAR = 13
CMD_ADD_CHAR_INT = 14
CMD_ADD_CHAR_FLOAT = 15
CMD_ADD_INT_CHAR = 16
CMD_ADD_INT_INT = 17
CMD_ADD_INT_FLOAT = 18
CMD_ADD_FLOAT_CHAR = 19
CMD_ADD_FLOAT_INT = 20
CMD_ADD_FLOAT_FLOAT = 21


SYMBOL_LT = '<'
CMD_LT_CHAR_CHAR = 22
CMD_LT_CHAR_INT = 23
CMD_LT_CHAR_FLOAT = 24
CMD_LT_INT_CHAR = 25
CMD_LT_INT_INT = 26
CMD_LT_INT_FLOAT = 27
CMD_LT_FLOAT_CHAR = 28
CMD_LT_FLOAT_INT = 29
CMD_LT_FLOAT_FLOAT = 30


SYMBOL_MUL = '*'
CMD_MUL_CHAR_CHAR = 31
CMD_MUL_CHAR_INT = 32
CMD_MUL_CHAR_FLOAT = 33
CMD_MUL_INT_CHAR = 34
CMD_MUL_INT_INT = 35
CMD_MUL_INT_FLOAT = 36
CMD_MUL_FLOAT_CHAR = 37
CMD_MUL_FLOAT_INT = 38
CMD_MUL_FLOAT_FLOAT = 39


SYMBOL_SET = '='
CMD_SET_CHAR_CHAR = 40
CMD_SET_CHAR_INT = 41
CMD_SET_CHAR_FLOAT = 42
CMD_SET_INT_CHAR = 43
CMD_SET_INT_INT = 44
CMD_SET_INT_FLOAT = 45
CMD_SET_FLOAT_CHAR = 46
CMD_SET_FLOAT_INT = 47
CMD_SET_FLOAT_FLOAT = 48
OPERATOR_CMD = {
	(SYMBOL_MUL, DATA_TYPE_CHAR, DATA_TYPE_FLOAT): CMD_MUL_CHAR_FLOAT, 
	(SYMBOL_ADD, DATA_TYPE_CHAR, DATA_TYPE_FLOAT): CMD_ADD_CHAR_FLOAT, 
	(SYMBOL_ADD, DATA_TYPE_CHAR, DATA_TYPE_CHAR): CMD_ADD_CHAR_CHAR, 
	(SYMBOL_MUL, DATA_TYPE_INT, DATA_TYPE_FLOAT): CMD_MUL_INT_FLOAT, 
	(SYMBOL_MUL, DATA_TYPE_INT, DATA_TYPE_CHAR): CMD_MUL_INT_CHAR, 
	(SYMBOL_SET, DATA_TYPE_INT, DATA_TYPE_INT): CMD_SET_INT_INT, 
	(SYMBOL_ADD, DATA_TYPE_CHAR, DATA_TYPE_INT): CMD_ADD_CHAR_INT, 
	(SYMBOL_SET, DATA_TYPE_FLOAT, DATA_TYPE_INT): CMD_SET_FLOAT_INT, 
	(SYMBOL_SET, DATA_TYPE_INT, DATA_TYPE_CHAR): CMD_SET_INT_CHAR, 
	(SYMBOL_ADD, DATA_TYPE_FLOAT, DATA_TYPE_INT): CMD_ADD_FLOAT_INT, 
	(SYMBOL_SET, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT): CMD_SET_FLOAT_FLOAT, 
	(SYMBOL_SET, DATA_TYPE_INT, DATA_TYPE_FLOAT): CMD_SET_INT_FLOAT, 
	(SYMBOL_LT, DATA_TYPE_CHAR, DATA_TYPE_FLOAT): CMD_LT_CHAR_FLOAT, 
	(SYMBOL_SET, DATA_TYPE_CHAR, DATA_TYPE_FLOAT): CMD_SET_CHAR_FLOAT, 
	(SYMBOL_ADD, DATA_TYPE_INT, DATA_TYPE_INT): CMD_ADD_INT_INT, 
	(SYMBOL_ADD, DATA_TYPE_FLOAT, DATA_TYPE_CHAR): CMD_ADD_FLOAT_CHAR, 
	(SYMBOL_LT, DATA_TYPE_CHAR, DATA_TYPE_CHAR): CMD_LT_CHAR_CHAR, 
	(SYMBOL_ADD, DATA_TYPE_INT, DATA_TYPE_FLOAT): CMD_ADD_INT_FLOAT, 
	(SYMBOL_ADD, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT): CMD_ADD_FLOAT_FLOAT, 
	(SYMBOL_MUL, DATA_TYPE_INT, DATA_TYPE_INT): CMD_MUL_INT_INT, 
	(SYMBOL_ADD, DATA_TYPE_INT, DATA_TYPE_CHAR): CMD_ADD_INT_CHAR, 
	(SYMBOL_SET, DATA_TYPE_FLOAT, DATA_TYPE_CHAR): CMD_SET_FLOAT_CHAR, 
	(SYMBOL_LT, DATA_TYPE_CHAR, DATA_TYPE_INT): CMD_LT_CHAR_INT, 
	(SYMBOL_LT, DATA_TYPE_FLOAT, DATA_TYPE_INT): CMD_LT_FLOAT_INT, 
	(SYMBOL_MUL, DATA_TYPE_FLOAT, DATA_TYPE_INT): CMD_MUL_FLOAT_INT, 
	(SYMBOL_MUL, DATA_TYPE_FLOAT, DATA_TYPE_CHAR): CMD_MUL_FLOAT_CHAR, 
	(SYMBOL_SET, DATA_TYPE_CHAR, DATA_TYPE_CHAR): CMD_SET_CHAR_CHAR, 
	(SYMBOL_LT, DATA_TYPE_INT, DATA_TYPE_INT): CMD_LT_INT_INT, 
	(SYMBOL_LT, DATA_TYPE_FLOAT, DATA_TYPE_CHAR): CMD_LT_FLOAT_CHAR, 
	(SYMBOL_MUL, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT): CMD_MUL_FLOAT_FLOAT, 
	(SYMBOL_LT, DATA_TYPE_INT, DATA_TYPE_FLOAT): CMD_LT_INT_FLOAT, 
	(SYMBOL_LT, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT): CMD_LT_FLOAT_FLOAT, 
	(SYMBOL_SET, DATA_TYPE_CHAR, DATA_TYPE_INT): CMD_SET_CHAR_INT, 
	(SYMBOL_LT, DATA_TYPE_INT, DATA_TYPE_CHAR): CMD_LT_INT_CHAR, 
	(SYMBOL_MUL, DATA_TYPE_CHAR, DATA_TYPE_INT): CMD_MUL_CHAR_INT, 
	(SYMBOL_MUL, DATA_TYPE_CHAR, DATA_TYPE_CHAR): CMD_MUL_CHAR_CHAR, 
}
OPERATOR1 = [
	SYMBOL_ADD, 
	SYMBOL_LT, 
	SYMBOL_MUL, 
	SYMBOL_SET, 
]


CMD_SIZE = {
	CMD_SET_CHAR_INT: 1, 
	CMD_MUL_INT_FLOAT: 1, 
	CMD_MUL_FLOAT_FLOAT: 1, 
	CMD_SET_FLOAT_FLOAT: 1, 
	CMD_LT_CHAR_FLOAT: 1, 
	CMD_RUN: 5, 
	CMD_LT_INT_INT: 1, 
	CMD_LT_FLOAT_INT: 1, 
	CMD_LT_INT_FLOAT: 1, 
	CMD_MUL_CHAR_CHAR: 1, 
	CMD_SET_CHAR_FLOAT: 1, 
	CMD_LT_CHAR_CHAR: 1, 
	CMD_LT_CHAR_INT: 1, 
	CMD_ADD_CHAR_FLOAT: 1, 
	CMD_ADD_FLOAT_FLOAT: 1, 
	CMD_MUL_CHAR_INT: 1, 
	CMD_SET_INT_INT: 1, 
	CMD_PUSH_SEGMENT_CHAR: 5, 
	CMD_MUL_FLOAT_CHAR: 1, 
	CMD_RETURN: 1, 
	CMD_MUL_INT_INT: 1, 
	CMD_ADD_FLOAT_INT: 1, 
	CMD_SET_CHAR_CHAR: 1, 
	CMD_PRINT_INT: 1, 
	CMD_MUL_FLOAT_INT: 1, 
	CMD_SET_INT_FLOAT: 1, 
	CMD_ADD_FLOAT_CHAR: 1, 
	CMD_ADD_CHAR_CHAR: 1, 
	CMD_ADD_INT_CHAR: 1, 
	CMD_PUSH_SEGMENT_FLOAT: 5, 
	CMD_PUSH_SEGMENT_INT: 5, 
	CMD_ADD_INT_FLOAT: 1, 
	CMD_LT_INT_CHAR: 1, 
	CMD_SET_INT_CHAR: 1, 
	CMD_ADD_INT_INT: 1, 
	CMD_PUSH_FLOAT: 5, 
	CMD_SET_FLOAT_INT: 1, 
	CMD_PRINT_CHAR: 1, 
	CMD_PUSH_CHAR: 2, 
	CMD_JUMP: 5, 
	CMD_PRINT_FLOAT: 1, 
	CMD_ADD_CHAR_INT: 1, 
	CMD_LT_FLOAT_CHAR: 1, 
	CMD_MUL_CHAR_FLOAT: 1, 
	CMD_PUSH_INT: 5, 
	CMD_SET_FLOAT_CHAR: 1, 
	CMD_FJ: 5, 
	CMD_LT_FLOAT_FLOAT: 1, 
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
	CMD_LT_INT_FLOAT: DATA_TYPE_CHAR, 
	CMD_MUL_CHAR_CHAR: DATA_TYPE_CHAR, 
	CMD_LT_CHAR_CHAR: DATA_TYPE_CHAR, 
	CMD_LT_CHAR_INT: DATA_TYPE_CHAR, 
	CMD_ADD_CHAR_FLOAT: DATA_TYPE_FLOAT, 
	CMD_ADD_FLOAT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_MUL_CHAR_INT: DATA_TYPE_INT, 
	CMD_SET_INT_INT: DATA_TYPE_INT, 
	CMD_MUL_FLOAT_CHAR: DATA_TYPE_FLOAT, 
	CMD_MUL_INT_INT: DATA_TYPE_INT, 
	CMD_SET_CHAR_CHAR: DATA_TYPE_CHAR, 
	CMD_MUL_FLOAT_INT: DATA_TYPE_FLOAT, 
	CMD_ADD_FLOAT_CHAR: DATA_TYPE_FLOAT, 
	CMD_ADD_CHAR_CHAR: DATA_TYPE_CHAR, 
	CMD_ADD_INT_CHAR: DATA_TYPE_INT, 
	CMD_SET_CHAR_FLOAT: DATA_TYPE_FLOAT, 
	CMD_MUL_INT_CHAR: DATA_TYPE_INT, 
	CMD_SET_FLOAT_CHAR: DATA_TYPE_FLOAT, 
	CMD_SET_INT_CHAR: DATA_TYPE_INT, 
	CMD_ADD_INT_INT: DATA_TYPE_INT, 
	CMD_SET_FLOAT_INT: DATA_TYPE_FLOAT, 
	CMD_ADD_INT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_LT_INT_CHAR: DATA_TYPE_CHAR, 
	CMD_ADD_FLOAT_INT: DATA_TYPE_FLOAT, 
	CMD_LT_FLOAT_FLOAT: DATA_TYPE_CHAR, 
	CMD_LT_FLOAT_CHAR: DATA_TYPE_CHAR, 
	CMD_MUL_CHAR_FLOAT: DATA_TYPE_FLOAT, 
	CMD_SET_INT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_ADD_CHAR_INT: DATA_TYPE_INT, 
}
