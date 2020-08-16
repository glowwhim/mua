# -*- coding: utf-8 -*-
from defines import *


code_address = 0
code_list = []


def code(cmd, *args):
	global code_address
	global code_list
	code_address += CMD_SIZE[cmd]
	code_list.append([cmd] + [i for i in args])
