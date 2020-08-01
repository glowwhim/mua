# -*- coding: utf-8 -*-
import os
import sys
import origindefines


lines = []
data_type_id = {}
data_type_list = []
data_type_define_name = {}
cmd_size = {}
cmd_return_data_type = {}


def add_cmd(cmd, args_size, rtype=None):
	global lines
	global cmd_size
	lines.append("%s = %s" % (cmd, len(cmd_size)))
	cmd_size[cmd] = args_size + 1
	if rtype is not None:
		cmd_return_data_type[cmd] = rtype


def init_data_type_list():
	global data_type_list
	global data_type_id
	global data_type_define_name
	_id = 0
	for attr in dir(origindefines):
		if attr.startswith("DATA_TYPE_"):
			info = getattr(origindefines, attr)
			data_type_list.append(info)
			data_type_define_name[_id] = attr
			data_type_id[info] = _id
			_id += 1


def copy_defines():
	global lines
	lines.append("")
	lines.append("")
	for attr in dir(origindefines):
		if attr.startswith("TOKEN_PROP_"):
			lines.append("%s = '%s'" % (attr, getattr(origindefines, attr)))

	lines.append("")
	lines.append("")
	for attr in dir(origindefines):
		if attr.startswith("SYMBOL_"):
			lines.append("%s = '%s'" % (attr, getattr(origindefines, attr)))

	lines.append("")
	lines.append("")
	for attr in dir(origindefines):
		if attr.startswith("CMD_"):
			add_cmd(attr, getattr(origindefines, attr))


def gen_data_type_defines():
	global lines
	lines.append("")
	lines.append("")
	for data_type in data_type_list:
		data_type_name = "DATA_TYPE_%s" % data_type[0].upper()
		lines.append("%s = %s" % (data_type_name, data_type_id[data_type]))
	lines.append("DATA_TYPE_SYMBOL = {")
	for data_type in data_type_list:
		lines.append("\tDATA_TYPE_%s: '%s', " % (data_type[0].upper(), data_type[0]))
	lines.append("}")
	lines.append("DATA_TYPE_VALUE_SYMBOL = {")
	for data_type in data_type_list:
		lines.append("\tDATA_TYPE_%s: '%s', " % (data_type[0].upper(), data_type[1]))
	lines.append("}")
	lines.append("DATA_TYPE_SIZE = {")
	for data_type in data_type_list:
		lines.append("\tDATA_TYPE_%s: %s, " % (data_type[0].upper(), data_type[2]))
	lines.append("}")
	lines.append("ALL_DATA_TYPE = [")
	for data_type in data_type_list:
		lines.append("\tDATA_TYPE_%s, " % data_type[0].upper())
	lines.append("]")


def gen_print_define():
	global lines
	lines.append("")
	lines.append("")
	lines.append("SYMBOL_PRINT = 'print'")
	for data_type in data_type_list:
		add_cmd("CMD_PRINT_%s" % data_type[0].upper(), 0)
	lines.append("DATA_TYPE_2_PRINT_CMD = {")
	for data_type in data_type_list:
		lines.append("\tDATA_TYPE_%s: %s, " % (data_type[0].upper(), "CMD_PRINT_%s" % data_type[0].upper()))
	lines.append("}")


def gen_return_define():
	global lines
	lines.append("")
	lines.append("")
	lines.append("SYMBOL_RETURN = 'return'")
	for data_type in data_type_list:
		add_cmd("CMD_RETURN_%s" % data_type[0].upper(), 0)
	lines.append("DATA_TYPE_2_RETURN_CMD = {")
	for data_type in data_type_list:
		lines.append("\tDATA_TYPE_%s: %s, " % (data_type[0].upper(), "CMD_RETURN_%s" % data_type[0].upper()))
	lines.append("}")


def gen_push_data_cmd():
	global lines
	lines.append("")
	lines.append("")
	for data_type in data_type_list:
		add_cmd("CMD_PUSH_%s" % data_type[0].upper(), data_type[2])
	lines.append("DATA_TYPE_2_PUSH_DATA_CMD = {")
	for data_type in data_type_list:
		lines.append("\tDATA_TYPE_%s: %s, " % (data_type[0].upper(), "CMD_PUSH_%s" % data_type[0].upper()))
	lines.append("}")


def gen_push_segment_data_cmd():
	global lines
	lines.append("")
	lines.append("")
	for data_type in data_type_list:
		add_cmd("CMD_PUSH_SEGMENT_%s" % data_type[0].upper(), 4)
	lines.append("DATA_TYPE_2_PUSH_SEGMENT_DATA_CMD = {")
	for data_type in data_type_list:
		lines.append("\tDATA_TYPE_%s: %s, " % (data_type[0].upper(), "CMD_PUSH_SEGMENT_%s" % data_type[0].upper()))
	lines.append("}")


def gen_operator_defines():
	global lines
	global cmd_return_data_type
	data_type_2_cmd = {}
	cmd_name_define = {}
	operator1 = []
	operator2 = []
	for attr in dir(origindefines):
		if attr.startswith("OPERATOR_"):
			lines.append("")
			lines.append("")
			define_name = attr[9:]
			op, op_list = getattr(origindefines, attr)
			symbol = "SYMBOL_%s" % define_name
			if len(op) == 1:
				operator1.append(symbol)
			if len(op) == 2:
				operator2.append(symbol)
			lines.append("%s = '%s'" % (symbol, op))
			for l_data, r_data, rtype in op_list:
				if l_data is None:
					cmd = "CMD_%s_%s" % (define_name, r_data[0].upper())
					cmd_name_define[len(cmd_size)] = cmd
					data_type_2_cmd[(symbol, None, data_type_id[r_data])] = cmd
					add_cmd(cmd, 0, rtype)
				else:
					cmd = "CMD_%s_%s_%s" % (define_name, l_data[0].upper(), r_data[0].upper())
					cmd_name_define[len(cmd_size)] = cmd
					data_type_2_cmd[(symbol, data_type_id[l_data], data_type_id[r_data])] = cmd
					add_cmd(cmd, 0, rtype)
	lines.append("OPERATOR_CMD = {")
	for k, v in data_type_2_cmd.iteritems():
		if k[1] is None:
			key = "(%s, None, %s)" % (k[0], data_type_define_name[k[2]])
		else:
			key = "(%s, %s, %s)" % (k[0], data_type_define_name[k[1]], data_type_define_name[k[2]])
		lines.append("\t%s: %s, " % (key, str(v)))
	lines.append("}")
	lines.append("OPERATOR1 = [")
	for op in operator1:
		lines.append("\t%s, " % op)
	lines.append("]")
	lines.append("OPERATOR2 = [")
	for op in operator2:
		lines.append("\t%s, " % op)
	lines.append("]")


def gen_cmd_size_defines():
	global lines
	lines.append("")
	lines.append("")
	lines.append("CMD_SIZE = {")
	for k, v in cmd_size.iteritems():
		lines.append("\t%s: %s, " % (k, v))
	lines.append("}")


def gen_cmd_return_data_type_defines():
	global lines
	lines.append("")
	lines.append("")
	lines.append("CMD_RETURN_DATA_TYPE = {")
	for k, v in cmd_return_data_type.iteritems():
		lines.append("\t%s: DATA_TYPE_%s, " % (k, v[0].upper()))
	lines.append("}")


def gen_defines():
	global lines
	init_data_type_list()

	lines = ["# -*- coding: utf-8 -*-"]

	copy_defines()
	gen_data_type_defines()
	gen_push_data_cmd()
	gen_push_segment_data_cmd()
	gen_print_define()
	gen_return_define()
	gen_operator_defines()
	gen_cmd_size_defines()
	gen_cmd_return_data_type_defines()

	root_path = os.path.split(sys.argv[0])[0]
	lines.append("")
	f = open(os.path.join(root_path, "defines.py"), "w")
	f.write("\n".join(lines))
	f.close()


if __name__ == '__main__':
	gen_defines()
