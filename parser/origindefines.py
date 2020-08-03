# -*- coding: utf-8 -*-


TOKEN_PROP_VALUE = "value"
TOKEN_PROP_DATE_TYPE = "type"
TOKEN_PROP_LEXEME = "lexeme"
TOKEN_PROP_ADDRESS_TYPE = "address_type"


DATA_TYPE_VOID = "void", "void_value", 0
DATA_TYPE_CHAR = "char", "char_value", 1
DATA_TYPE_INT = "int", "int_value", 4
DATA_TYPE_FLOAT = "float", "float_value", 4
DATA_TYPE_ADDRESS = "address", "address_value", 4


SYMBOL_START = "$START"
SYMBOL_END = "#"
SYMBOL_DATA_TYPE = "data_type"
SYMBOL_RETURN = "return"
SYMBOL_VAR_ID = "var_id"
SYMBOL_WHILE = "while"
SYMBOL_SEMICOLON = ";"
SYMBOL_LPRENE = "("
SYMBOL_RPRENE = ")"
SYMBOL_LBRACKET = "["
SYMBOL_RBRACKET = "]"
SYMBOL_LBRACE = "{"
SYMBOL_RBRACE = "}"
SYMBOL_COMMA = ","


CMD_FJ = 4
CMD_JUMP = 4
CMD_RUN = 8
CMD_PUSH_ANY = 4
CMD_SET_TO_ADDRESS = 8
CMD_PUSH_FROM_ADDRESS = 8
CMD_RETURN = 8


OPERATOR_ADD = [
	"+",
	[
		(DATA_TYPE_CHAR, DATA_TYPE_CHAR, DATA_TYPE_CHAR),
		(DATA_TYPE_CHAR, DATA_TYPE_INT, DATA_TYPE_INT),
		(DATA_TYPE_CHAR, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT),
		(DATA_TYPE_INT, DATA_TYPE_CHAR, DATA_TYPE_INT),
		(DATA_TYPE_INT, DATA_TYPE_INT, DATA_TYPE_INT),
		(DATA_TYPE_INT, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT),
		(DATA_TYPE_FLOAT, DATA_TYPE_CHAR, DATA_TYPE_FLOAT),
		(DATA_TYPE_FLOAT, DATA_TYPE_INT, DATA_TYPE_FLOAT),
		(DATA_TYPE_FLOAT, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT),
		(DATA_TYPE_ADDRESS, DATA_TYPE_INT, DATA_TYPE_ADDRESS),
	],
]
OPERATOR_MUL = [
	"*",
	[
		(DATA_TYPE_CHAR, DATA_TYPE_CHAR, DATA_TYPE_CHAR),
		(DATA_TYPE_CHAR, DATA_TYPE_INT, DATA_TYPE_INT),
		(DATA_TYPE_CHAR, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT),
		(DATA_TYPE_INT, DATA_TYPE_CHAR, DATA_TYPE_INT),
		(DATA_TYPE_INT, DATA_TYPE_INT, DATA_TYPE_INT),
		(DATA_TYPE_INT, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT),
		(DATA_TYPE_FLOAT, DATA_TYPE_CHAR, DATA_TYPE_FLOAT),
		(DATA_TYPE_FLOAT, DATA_TYPE_INT, DATA_TYPE_FLOAT),
		(DATA_TYPE_FLOAT, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT),
	],
]
OPERATOR_SET = [
	"=",
	[
		(DATA_TYPE_CHAR, DATA_TYPE_CHAR, DATA_TYPE_CHAR),
		(DATA_TYPE_CHAR, DATA_TYPE_INT, DATA_TYPE_INT),
		(DATA_TYPE_CHAR, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT),
		(DATA_TYPE_INT, DATA_TYPE_CHAR, DATA_TYPE_INT),
		(DATA_TYPE_INT, DATA_TYPE_INT, DATA_TYPE_INT),
		(DATA_TYPE_INT, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT),
		(DATA_TYPE_FLOAT, DATA_TYPE_CHAR, DATA_TYPE_FLOAT),
		(DATA_TYPE_FLOAT, DATA_TYPE_INT, DATA_TYPE_FLOAT),
		(DATA_TYPE_FLOAT, DATA_TYPE_FLOAT, DATA_TYPE_FLOAT),
	],
]
OPERATOR_LT = [
	"<",
	[
		(DATA_TYPE_CHAR, DATA_TYPE_CHAR, DATA_TYPE_CHAR),
		(DATA_TYPE_CHAR, DATA_TYPE_INT, DATA_TYPE_CHAR),
		(DATA_TYPE_CHAR, DATA_TYPE_FLOAT, DATA_TYPE_CHAR),
		(DATA_TYPE_INT, DATA_TYPE_CHAR, DATA_TYPE_CHAR),
		(DATA_TYPE_INT, DATA_TYPE_INT, DATA_TYPE_CHAR),
		(DATA_TYPE_INT, DATA_TYPE_FLOAT, DATA_TYPE_CHAR),
		(DATA_TYPE_FLOAT, DATA_TYPE_CHAR, DATA_TYPE_CHAR),
		(DATA_TYPE_FLOAT, DATA_TYPE_INT, DATA_TYPE_CHAR),
		(DATA_TYPE_FLOAT, DATA_TYPE_FLOAT, DATA_TYPE_CHAR),
	],
]
OPERATOR_EQ = [
	"==",
	[
		(DATA_TYPE_CHAR, DATA_TYPE_CHAR, DATA_TYPE_CHAR),
		(DATA_TYPE_CHAR, DATA_TYPE_INT, DATA_TYPE_CHAR),
		(DATA_TYPE_CHAR, DATA_TYPE_FLOAT, DATA_TYPE_CHAR),
		(DATA_TYPE_INT, DATA_TYPE_CHAR, DATA_TYPE_CHAR),
		(DATA_TYPE_INT, DATA_TYPE_INT, DATA_TYPE_CHAR),
		(DATA_TYPE_INT, DATA_TYPE_FLOAT, DATA_TYPE_CHAR),
		(DATA_TYPE_FLOAT, DATA_TYPE_CHAR, DATA_TYPE_CHAR),
		(DATA_TYPE_FLOAT, DATA_TYPE_INT, DATA_TYPE_CHAR),
		(DATA_TYPE_FLOAT, DATA_TYPE_FLOAT, DATA_TYPE_CHAR),
		(DATA_TYPE_ADDRESS, DATA_TYPE_ADDRESS, DATA_TYPE_CHAR),
	],
]
OPERATOR_NOT = [
	"!",
	[
		(None, DATA_TYPE_CHAR, DATA_TYPE_CHAR),
	],
]
OPERATOR_ADDRESS = [
	"&",
	[
		(None, DATA_TYPE_CHAR, DATA_TYPE_ADDRESS),
		(None, DATA_TYPE_INT, DATA_TYPE_ADDRESS),
		(None, DATA_TYPE_FLOAT, DATA_TYPE_ADDRESS),
	],
]
