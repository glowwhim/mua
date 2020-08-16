# -*- coding: utf-8 -*-
from typing import List
from lexer import *
from parser import Production
import defines


def _copy_prop(dst, src):
	# type: (Token, Token) -> None
	for s in src.get_all_prop_name():
		setattr(dst, s, getattr(src, s))


class VariableTable(object):

	parent = None  # type: VariableTable

	def __init__(self, parent):
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
		self.variable_table = VariableTable(None)
		self.semantics_code = ""
		self.code_list = []
		self.def_func = {}
		self.loop_begin_stack = []
		self.loop_fj_stack = []
		self._env = {
			"copy": _copy_prop,
			"code": self._code,
			"add_func": self._add_func,
			"run_func": self._run_func,
			"_loop_begin": self._loop_begin,
			"_fj_begin": self._fj_begin,
			"_fj_end": self._fj_end,
			"get_func_return_type": self._get_func_return_type,
			"clear_func": self._clear_func,
			"func_params_type": [],
			"method_params": [],
		}
		for _s in dir(defines):
			self._env[_s] = getattr(defines, _s)
		self._clear_func()
		self._load_semantics_code()

	def _load_semantics_code(self):
		import os
		import sys
		root_path = os.path.split(sys.argv[0])[0]
		semantics_path = os.path.join(root_path, "semantics.py")
		f = open(semantics_path)
		self.semantics_code = f.read()
		f.close()

	def _add_func(self, name, r_type):
		print "add func", name
		self.def_func[name] = self._env["code_address"], r_type

	def _clear_func(self):
		self.variable_table = VariableTable(None)
		self._env["add_var"] = self.variable_table.add_var
		self._env["get_var"] = self.variable_table.get_var
		self._env["add_array"] = self.variable_table.add_array
		self._env["move_address"] = self.variable_table.move_address

	def _run_func(self, name, func_params_size):
		if name in self.def_func:
			self._code(CMD_RUN, self.def_func[name][0], func_params_size)
		else:
			self._code(CMD_RUN, 0, func_params_size)

	def _get_func_return_type(self, name):
		if name in self.def_func:
			return self.def_func[name][1]
		else:
			return DATA_TYPE_INT

	def _code(self, cmd, *args):
		self._env["code_address"] += CMD_SIZE[cmd]
		self.code_list.append([cmd] + [i for i in args])

	def _loop_begin(self):
		self.loop_begin_stack.append(self._env["code_address"])

	def _fj_begin(self):
		self.loop_fj_stack.append(len(self.code_list))
		self._code(CMD_FJ, 0)

	def _fj_end(self):
		self._code(CMD_JUMP, self.loop_begin_stack.pop())
		self.code_list[self.loop_fj_stack.pop()][1] = self._env["code_address"]

	def do_semantics_start(self):
		self.variable_table = VariableTable(None)
		self.code_list = []
		self.loop_begin_stack = []
		self.loop_fj_stack = []
		exec (self.semantics_code, self._env)

	def do_semantics(self, production, rd, pd):
		# type: (Production, Token, List[Token]) -> None
		self._env["rd"] = rd
		self._env["pd"] = pd
		self._env["fpd"] = pd[0]
		exec (production.get_semantics_action(), self._env)

	def output_code(self, path):
		f = open(path, "w")
		lines = [str(self._env["code_address"]), str(self.def_func["main()"][0])]
		for c in self.code_list:
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
		for c in self.code_list:
			cmd = c[0]
			print "%s: %s %s" % (address, cmd_name[cmd], " ".join([str(s) for s in c[1:]]))
			address += CMD_SIZE[cmd]
