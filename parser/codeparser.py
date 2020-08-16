# -*- coding: utf-8 -*-
from typing import List
from lexer import *
from parser import Production
import defines


class VariableTable(object):

	parent = None  # type: VariableTable

	def __init__(self, parent=None):
		# type: (VariableTable) -> None
		self.parent = parent
		self.variable = {}
		self.next_address = 0

	def move_address(self, offset):
		self.next_address += offset

	def add_var(self, token):
		name = token.lexeme
		if name in self.variable:
			raise Exception("%s already define" % name)
		self.variable[name] = self.next_address, token
		self.next_address += DATA_TYPE_SIZE[token.type]

	def add_array(self, token, size):
		name = token.lexeme
		if name in self.variable:
			raise Exception("%s already define" % name)
		self.variable[name] = self.next_address, token
		self.next_address += DATA_TYPE_SIZE[token.address_type] * size

	def get_var(self, name):
		return self.variable[name]


class CodeParser(object):

	def __init__(self):
		self.semantics_code = ""
		self._env = {}
		self._init_semantics_code()

	def _init_semantics_code(self):
		import os
		import sys
		root_path = os.path.split(sys.argv[0])[0]
		semantics_path = os.path.join(root_path, "semantics.py")
		f = open(semantics_path)
		self.semantics_code = f.read()
		f.close()
		exec (self.semantics_code, self._env)

	def on_parse_start(self):
		self._env["on_parse_start"]()

	def do_semantics(self, production, rd, pd):
		# type: (Production, Token, List[Token]) -> None
		self._env["rd"] = rd
		self._env["pd"] = pd
		self._env["fpd"] = pd[0]
		exec (production.get_semantics_action(), self._env)

	def output_code(self, path):
		f = open(path, "w")
		lines = [str(self._env["code_address"]), str(self._env["def_func"]["main()"][0])]
		for c in self._env["code_list"]:
			cmd = c[0]
			lines.append("%s %s" % (cmd, " ".join([str(s) for s in c[1:]])))
		f.write("\n".join(lines))
		f.close()

	def print_code(self):
		address = 0
		cmd_name = {}
		for attr in dir(defines):
			if attr.startswith("CMD_"):
				cmd = getattr(defines, attr)
				if not isinstance(cmd, int):
					continue
				cmd_name[cmd] = attr
		for c in self._env["code_list"]:
			cmd = c[0]
			print "%s: %s %s" % (address, cmd_name[cmd], " ".join([str(s) for s in c[1:]]))
			address += CMD_SIZE[cmd]
