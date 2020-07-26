# -*- coding: utf-8 -*-


TOKEN_PROP_DATE_TYPE = 'type'
TOKEN_PROP_LEXEME = 'lexeme'
TOKEN_PROP_VALUE = 'value'


SYMBOL_END = '#'
SYMBOL_L_BRACKET = '('
SYMBOL_R_BRACKET = ')'
SYMBOL_SEMICOLON = ';'
SYMBOL_START = '$START'
SYMBOL_VAR_ID = 'var_id'
SYMBOL_WHILE = 'while'


CMD_EXIT = 0
CMD_FJ = 1
CMD_JUMP = 2


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


CMD_PUSH_CHAR = 3
CMD_PUSH_FLOAT = 4
CMD_PUSH_INT = 5
DATA_TYPE_2_PUSH_DATA_CMD = {
	DATA_TYPE_CHAR: CMD_PUSH_CHAR, 
	DATA_TYPE_FLOAT: CMD_PUSH_FLOAT, 
	DATA_TYPE_INT: CMD_PUSH_INT, 
}


CMD_PUSH_SEGMENT_CHAR = 6
CMD_PUSH_SEGMENT_FLOAT = 7
CMD_PUSH_SEGMENT_INT = 8
DATA_TYPE_2_PUSH_SEGMENT_DATA_CMD = {
	DATA_TYPE_CHAR: CMD_PUSH_SEGMENT_CHAR, 
	DATA_TYPE_FLOAT: CMD_PUSH_SEGMENT_FLOAT, 
	DATA_TYPE_INT: CMD_PUSH_SEGMENT_INT, 
}


SYMBOL_PRINT = 'print'
CMD_PRINT_CHAR = 9
CMD_PRINT_FLOAT = 10
CMD_PRINT_INT = 11
DATA_TYPE_2_PRINT_CMD = {
	DATA_TYPE_CHAR: CMD_PRINT_CHAR, 
	DATA_TYPE_FLOAT: CMD_PRINT_FLOAT, 
	DATA_TYPE_INT: CMD_PRINT_INT, 
}


SYMBOL_ADD = '+'
CMD_ADD_CHAR_CHAR = 12
CMD_ADD_CHAR_INT = 13
CMD_ADD_CHAR_FLOAT = 14
CMD_ADD_INT_CHAR = 15
CMD_ADD_INT_INT = 16
CMD_ADD_INT_FLOAT = 17
CMD_ADD_FLOAT_CHAR = 18
CMD_ADD_FLOAT_INT = 19
CMD_ADD_FLOAT_FLOAT = 20


SYMBOL_MUL = '*'
CMD_MUL_CHAR_CHAR = 21
CMD_MUL_CHAR_INT = 22
CMD_MUL_CHAR_FLOAT = 23
CMD_MUL_INT_CHAR = 24
CMD_MUL_INT_INT = 25
CMD_MUL_INT_FLOAT = 26
CMD_MUL_FLOAT_CHAR = 27
CMD_MUL_FLOAT_INT = 28
CMD_MUL_FLOAT_FLOAT = 29


SYMBOL_SET = '='
CMD_SET_CHAR_CHAR = 30
CMD_SET_CHAR_INT = 31
CMD_SET_CHAR_FLOAT = 32
CMD_SET_INT_CHAR = 33
CMD_SET_INT_INT = 34
CMD_SET_INT_FLOAT = 35
CMD_SET_FLOAT_CHAR = 36
CMD_SET_FLOAT_INT = 37
CMD_SET_FLOAT_FLOAT = 38
OPERATOR_CMD = {
	(SYMBOL_MUL, DATA_TYPE_CHAR, DATA_TYPE_FLOAT): CMD_MUL_CHAR_FLOAT, 
	(SYMBOL_ADD, DATA_TYPE_CHAR, DATA_TYPE_FLOAT): CMD_ADD_CHAR_FLOAT, 
	(SYMBOL_ADD, DATA_TYPE_CHAR, DATA_TYPE_CHAR): CMD_ADD_CHAR_CHAR, 
	(SYMBOL_SET, DATA_TYPE_INT, DATA_TYPE_INT): CMD_SET_INT_INT, 
	(SYMBOL_ADD, DATA_TYPE_CHAR, DATA_TYPE_INT): CMD_ADD_CHAR_INT, 
	(SYMBOL_SET, DATA_TYPE_FLOAT, DATA_TYPE_INT): CMD_SET_FLOAT_INT, 
	(SYMBOL_SET, DATA_TYPE_INT, DATA_TYPE_CHAR): CMD_SET_INT_CHAR, 
	(SYMBOL_ADD, DATA_TYPE_FLOAT, DATA_TYPE_INT): CMD_ADD_FLOAT_INT, 
	(SYMBOL_SET, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT): CMD_SET_FLOAT_FLOAT, 
	(SYMBOL_SET, DATA_TYPE_INT, DATA_TYPE_FLOAT): CMD_SET_INT_FLOAT, 
	(SYMBOL_MUL, DATA_TYPE_INT, DATA_TYPE_CHAR): CMD_MUL_INT_CHAR, 
	(SYMBOL_SET, DATA_TYPE_FLOAT, DATA_TYPE_CHAR): CMD_SET_FLOAT_CHAR, 
	(SYMBOL_ADD, DATA_TYPE_INT, DATA_TYPE_INT): CMD_ADD_INT_INT, 
	(SYMBOL_ADD, DATA_TYPE_FLOAT, DATA_TYPE_CHAR): CMD_ADD_FLOAT_CHAR, 
	(SYMBOL_MUL, DATA_TYPE_INT, DATA_TYPE_FLOAT): CMD_MUL_INT_FLOAT, 
	(SYMBOL_ADD, DATA_TYPE_INT, DATA_TYPE_FLOAT): CMD_ADD_INT_FLOAT, 
	(SYMBOL_ADD, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT): CMD_ADD_FLOAT_FLOAT, 
	(SYMBOL_MUL, DATA_TYPE_INT, DATA_TYPE_INT): CMD_MUL_INT_INT, 
	(SYMBOL_ADD, DATA_TYPE_INT, DATA_TYPE_CHAR): CMD_ADD_INT_CHAR, 
	(SYMBOL_MUL, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT): CMD_MUL_FLOAT_FLOAT, 
	(SYMBOL_MUL, DATA_TYPE_FLOAT, DATA_TYPE_CHAR): CMD_MUL_FLOAT_CHAR, 
	(SYMBOL_SET, DATA_TYPE_CHAR, DATA_TYPE_CHAR): CMD_SET_CHAR_CHAR, 
	(SYMBOL_SET, DATA_TYPE_CHAR, DATA_TYPE_FLOAT): CMD_SET_CHAR_FLOAT, 
	(SYMBOL_MUL, DATA_TYPE_FLOAT, DATA_TYPE_INT): CMD_MUL_FLOAT_INT, 
	(SYMBOL_SET, DATA_TYPE_CHAR, DATA_TYPE_INT): CMD_SET_CHAR_INT, 
	(SYMBOL_MUL, DATA_TYPE_CHAR, DATA_TYPE_INT): CMD_MUL_CHAR_INT, 
	(SYMBOL_MUL, DATA_TYPE_CHAR, DATA_TYPE_CHAR): CMD_MUL_CHAR_CHAR, 
}


CMD_SIZE = {
	CMD_SET_CHAR_INT: 1, 
	CMD_MUL_INT_FLOAT: 1, 
	CMD_MUL_FLOAT_FLOAT: 1, 
	CMD_SET_FLOAT_FLOAT: 1, 
	CMD_MUL_INT_CHAR: 1, 
	CMD_SET_INT_CHAR: 1, 
	CMD_EXIT: 1, 
	CMD_MUL_CHAR_CHAR: 1, 
	CMD_SET_CHAR_FLOAT: 1, 
	CMD_ADD_CHAR_FLOAT: 1, 
	CMD_ADD_FLOAT_FLOAT: 1, 
	CMD_MUL_CHAR_INT: 1, 
	CMD_SET_INT_INT: 1, 
	CMD_PUSH_SEGMENT_CHAR: 5, 
	CMD_MUL_FLOAT_CHAR: 1, 
	CMD_MUL_INT_INT: 1, 
	CMD_ADD_FLOAT_INT: 1, 
	CMD_SET_CHAR_CHAR: 1, 
	CMD_PRINT_INT: 2, 
	CMD_MUL_FLOAT_INT: 1, 
	CMD_SET_INT_FLOAT: 1, 
	CMD_ADD_FLOAT_CHAR: 1, 
	CMD_ADD_CHAR_CHAR: 1, 
	CMD_ADD_INT_CHAR: 1, 
	CMD_PUSH_SEGMENT_FLOAT: 5, 
	CMD_PUSH_SEGMENT_INT: 5, 
	CMD_ADD_INT_FLOAT: 1, 
	CMD_SET_FLOAT_CHAR: 1, 
	CMD_ADD_INT_INT: 1, 
	CMD_PUSH_FLOAT: 5, 
	CMD_SET_FLOAT_INT: 1, 
	CMD_PRINT_CHAR: 2, 
	CMD_PUSH_CHAR: 2, 
	CMD_JUMP: 5, 
	CMD_PRINT_FLOAT: 2, 
	CMD_ADD_CHAR_INT: 1, 
	CMD_MUL_CHAR_FLOAT: 1, 
	CMD_PUSH_INT: 5, 
	CMD_FJ: 1, 
}


CMD_RETURN_DATA_TYPE = {
	CMD_SET_CHAR_INT: DATA_TYPE_INT, 
	CMD_MUL_INT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_MUL_FLOAT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_SET_FLOAT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_SET_CHAR_FLOAT: DATA_TYPE_FLOAT, 
	CMD_SET_INT_CHAR: DATA_TYPE_INT, 
	CMD_MUL_CHAR_CHAR: DATA_TYPE_CHAR, 
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
	CMD_MUL_INT_CHAR: DATA_TYPE_INT, 
	CMD_SET_FLOAT_CHAR: DATA_TYPE_FLOAT, 
	CMD_ADD_INT_INT: DATA_TYPE_INT, 
	CMD_SET_FLOAT_INT: DATA_TYPE_FLOAT, 
	CMD_ADD_INT_FLOAT: DATA_TYPE_FLOAT, 
	CMD_ADD_FLOAT_INT: DATA_TYPE_FLOAT, 
	CMD_ADD_CHAR_INT: DATA_TYPE_INT, 
	CMD_MUL_CHAR_FLOAT: DATA_TYPE_FLOAT, 
	CMD_SET_INT_FLOAT: DATA_TYPE_FLOAT, 
}
