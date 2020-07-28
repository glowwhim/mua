# -*- coding: utf-8 -*-
from defines import *


KEYWORD = [
	SYMBOL_WHILE,
	SYMBOL_PRINT,
	SYMBOL_RETURN,
]
SPACE_CHAR = [" ", "\t", "\n"]
SEPARATOR = [
	SYMBOL_SEMICOLON,
	SYMBOL_LPRENE,
	SYMBOL_RPRENE,
	SYMBOL_LBRACKET,
	SYMBOL_RBRACKET,
]


TOKEN_FUNC_NAME = ["get_symbol", "set_prop", "get_prop", "print_prop", "get_all_prop_name"]


class Token(object):

	def __str__(self):
		return self.symbol

	def __init__(self, symbol):
		self.symbol = symbol

	def get_symbol(self):
		return self.symbol

	def set_prop(self, key, value):
		setattr(self, key, value)
		return self

	def get_prop(self, key):
		return getattr(self, key)

	def get_all_prop_name(self):
		l = []
		for s in dir(self):
			if s.startswith("_") or s in TOKEN_FUNC_NAME:
				continue
			l.append(s)
		return l

	def print_prop(self):
		prop = {}
		for s in self.get_all_prop_name():
			prop[s] = getattr(self, s)
		print prop


def _try_parse_data_type_keyword(code, left):
	for data_type, keyword in DATA_TYPE_SYMBOL.iteritems():
		i = left
		for char in keyword:
			if char != code[i]:
				break
			i += 1
		else:
			return i, data_type
	return -1, 0


def _try_parse_keyword(code, left):
	for keyword in KEYWORD:
		i = left
		for char in keyword:
			if char != code[i]:
				break
			i += 1
		else:
			return i
	return -1


def _try_parse_id(code, left):
	# type: (str, int) -> int
	if not code[left].isalpha():
		return -1
	i = left + 1
	code_len = len(code)
	while i < code_len and (code[i].isalpha() or code[i].isdigit() or code[i] == "_"):
		i += 1
	return i


def token_generator(code):
	"""
	:type code: str
	"""
	left = 0
	right = 0
	code_len = len(code)
	while right < code_len:
		if code[right].isdigit():
			# int, float
			while right < code_len and code[right].isdigit():
				right += 1
			if right < code_len and code[right] == ".":
				right += 1
				while right < code_len and code[right].isdigit():
					right += 1
				token = Token(DATA_TYPE_VALUE_SYMBOL[DATA_TYPE_FLOAT])
				token.set_prop(TOKEN_PROP_VALUE, float(code[left:right]))
				token.set_prop(TOKEN_PROP_DATE_TYPE, DATA_TYPE_FLOAT)
				yield token
			else:
				token = Token(DATA_TYPE_VALUE_SYMBOL[DATA_TYPE_INT])
				token.set_prop(TOKEN_PROP_VALUE, int(code[left:right]))
				token.set_prop(TOKEN_PROP_DATE_TYPE, DATA_TYPE_INT)
				yield token
			left = right
		elif code[right] in SPACE_CHAR:
			# tab
			left += 1
			right = left
		elif code[right] in OPERATOR1:
			# operator1
			yield Token(code[right]).set_prop(TOKEN_PROP_LEXEME, code[right])
			left += 1
			right = left
		elif code[right] in SEPARATOR:
			# separator
			yield Token(code[right]).set_prop(TOKEN_PROP_LEXEME, code[right])
			left += 1
			right = left
		else:
			# keyword
			right, data_type = _try_parse_data_type_keyword(code, left)
			if right != -1:
				yield Token(SYMBOL_DATA_TYPE).set_prop(TOKEN_PROP_DATE_TYPE, data_type)
				left = right
			else:
				right = _try_parse_keyword(code, left)
				if right != -1:
					yield Token(code[left:right])
					left = right
				else:
					# id
					right = _try_parse_id(code, left)
					if right != -1:
						yield Token(SYMBOL_VAR_ID).set_prop(TOKEN_PROP_LEXEME, code[left:right])
						left = right
					else:
						raise Exception("unexpected char %s" % code[right])
	yield Token(SYMBOL_END)
