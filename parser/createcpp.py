# -*- coding: utf-8 -*-
import os
import sys
import defines


def gen_cmd_define():
	root_path = os.path.split(sys.argv[0])[0]
	machine_path = os.path.join(root_path, "../machine")
	if not os.path.exists(machine_path):
		os.mkdir(machine_path)
	all_cmd = {}
	for attr in dir(defines):
		if not attr.startswith("CMD_"):
			continue
		i = getattr(defines, attr)
		if not isinstance(i, int):
			continue
		all_cmd[attr] = i
	f = open(os.path.join(machine_path, "cmd.h"), "w")
	f.write("\n".join(["const int %s = %s;" % (k, v) for k, v in sorted(all_cmd.iteritems(), key=lambda items: items[1])]))
	f.close()


if __name__ == '__main__':
	gen_cmd_define()
