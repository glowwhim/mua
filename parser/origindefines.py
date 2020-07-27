# -*- coding: utf-8 -*-


TOKEN_PROP_VALUE = "value"
TOKEN_PROP_DATE_TYPE = "type"
TOKEN_PROP_LEXEME = "lexeme"


DATA_TYPE_CHAR = "char", "char_value", 1
DATA_TYPE_INT = "int", "int_value", 4
DATA_TYPE_FLOAT = "float", "float_value", 4


SYMBOL_START = "$START"
SYMBOL_END = "#"
SYMBOL_VAR_ID = "var_id"
SYMBOL_WHILE = "while"
SYMBOL_SEMICOLON = ";"
SYMBOL_LPRENE = "("
SYMBOL_RPRENE = ")"
SYMBOL_LBRACKET = "{"
SYMBOL_RBRACKET = "}"


CMD_FJ = 4
CMD_JUMP = 4
CMD_RUN = 4


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
