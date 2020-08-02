# -*- coding: utf-8 -*-
import os
import sys
import origindefines


lines = []
all_data_type = {}
cmd_size = {}
cmd_return_data_type = {}


def get_data_type_id(origin_data_type):
	for _id, info in all_data_type.items():
		if origin_data_type == (info["keyword"], info["value_keyword"], info["size"]):
			return _id


def add_cmd(cmd, args_size, rtype=None):
	global lines
	global cmd_size
	lines.append("%s = %s" % (cmd, len(cmd_size)))
	cmd_size[cmd] = args_size + 1
	if rtype is not None:
		cmd_return_data_type[cmd] = rtype


def init_data_type_list():
	_id = 0
	for attr in dir(origindefines):
		if attr.startswith("DATA_TYPE_"):
			info = getattr(origindefines, attr)
			all_data_type[_id] = {
				"name": attr,
				"short_name": attr[10:],
				"keyword": info[0],
				"value_keyword": info[1],
				"size": info[2],
			}
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
	for _id, info in all_data_type.items():
		lines.append("%s = %s" % (info["name"], _id))
	lines.append("DATA_TYPE_SYMBOL = {")
	for data_type in all_data_type.values():
		lines.append("\t%s: '%s', " % (data_type["name"], data_type["keyword"]))
	lines.append("}")
	lines.append("DATA_TYPE_VALUE_SYMBOL = {")
	for data_type in all_data_type.values():
		lines.append("\t%s: '%s', " % (data_type["name"], data_type["value_keyword"]))
	lines.append("}")
	lines.append("DATA_TYPE_SIZE = {")
	for data_type in all_data_type.values():
		lines.append("\t%s: %s, " % (data_type["name"], data_type["size"]))
	lines.append("}")
	lines.append("ALL_DATA_TYPE = [")
	for data_type in all_data_type.values():
		lines.append("\t%s, " % data_type["name"])
	lines.append("]")


def gen_print_define():
	global lines
	lines.append("")
	lines.append("")
	lines.append("SYMBOL_PRINT = 'print'")
	for data_type in all_data_type.values():
		add_cmd("CMD_PRINT_%s" % data_type["short_name"], 0)
	lines.append("DATA_TYPE_2_PRINT_CMD = {")
	for data_type in all_data_type.values():
		lines.append("\t%s: %s, " % (data_type["name"], "CMD_PRINT_%s" % data_type["short_name"]))
	lines.append("}")


def gen_push_data_cmd():
	global lines
	lines.append("")
	lines.append("")
	for data_type in all_data_type.values():
		add_cmd("CMD_PUSH_%s" % data_type["short_name"], data_type["size"])
	lines.append("DATA_TYPE_2_PUSH_DATA_CMD = {")
	for data_type in all_data_type.values():
		lines.append("\t%s: %s, " % (data_type["name"], "CMD_PUSH_%s" % data_type["short_name"]))
	lines.append("}")


def gen_push_segment_data_cmd():
	global lines
	lines.append("")
	lines.append("")
	for data_type in all_data_type.values():
		add_cmd("CMD_PUSH_SEGMENT_%s" % data_type["short_name"], 4)
	lines.append("DATA_TYPE_2_PUSH_SEGMENT_DATA_CMD = {")
	for data_type in all_data_type.values():
		lines.append("\t%s: %s, " % (data_type["name"], "CMD_PUSH_SEGMENT_%s" % data_type["short_name"]))
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
				l_id = get_data_type_id(l_data)
				r_id = get_data_type_id(r_data)
				if l_data is None:
					cmd = "CMD_%s_%s" % (define_name, all_data_type[r_id]["short_name"])
					cmd_name_define[len(cmd_size)] = cmd
					data_type_2_cmd[(symbol, None, get_data_type_id(r_data))] = cmd
					add_cmd(cmd, 0, get_data_type_id(rtype))
				else:
					cmd = "CMD_%s_%s_%s" % (define_name, all_data_type[l_id]["short_name"], all_data_type[r_id]["short_name"])
					cmd_name_define[len(cmd_size)] = cmd
					data_type_2_cmd[(symbol, get_data_type_id(l_data), get_data_type_id(r_data))] = cmd
					add_cmd(cmd, 0, get_data_type_id(rtype))
	lines.append("OPERATOR_CMD = {")
	for k, v in data_type_2_cmd.items():
		if k[1] is None:
			key = "(%s, None, %s)" % (k[0], all_data_type[k[2]]["name"])
		else:
			key = "(%s, %s, %s)" % (k[0], all_data_type[k[1]]["name"], all_data_type[k[2]]["name"])
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
	for k, v in cmd_size.items():
		lines.append("\t%s: %s, " % (k, v))
	lines.append("}")


def gen_cmd_return_data_type_defines():
	global lines
	lines.append("")
	lines.append("")
	lines.append("CMD_RETURN_DATA_TYPE = {")
	for cmd, _id in cmd_return_data_type.items():
		lines.append("\t%s: %s, " % (cmd, all_data_type[_id]["name"]))
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
