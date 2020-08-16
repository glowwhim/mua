# -*- coding: utf-8 -*-
from defines import *
from codeparser import VariableTable


variable_table = VariableTable()
code_address = 0
code_list = []
def_func = {}
loop_begin_stack = []
loop_fj_stack = []
func_params_type = []
method_params = []


def clear_func():
	global variable_table
	variable_table = VariableTable()


def do_semantics_start():
	global code_address
	global code_list
	global loop_begin_stack
	global loop_fj_stack
	global variable_table
	variable_table = VariableTable()
	code_address = 0
	code_list = []
	loop_begin_stack = []
	loop_fj_stack = []


def loop_begin():
	loop_begin_stack.append(code_address)


def fj_begin():
	loop_fj_stack.append(len(code_list))
	code(CMD_FJ, 0)


def fj_end():
	code(CMD_JUMP, loop_begin_stack.pop())
	code_list[loop_fj_stack.pop()][1] = code_address


def add_func(name, r_type):
	global def_func
	print "add func", name
	def_func[name] = code_address, r_type


def get_func_return_type(name):
	if name in def_func:
		return def_func[name][1]
	else:
		return DATA_TYPE_INT


def run_func(name, func_params_size):
	if name in def_func:
		code(CMD_RUN, def_func[name][0], func_params_size)
	else:
		code(CMD_RUN, 0, func_params_size)


def code(cmd, *args):
	global code_address
	global code_list
	code_address += CMD_SIZE[cmd]
	code_list.append([cmd] + [i for i in args])
