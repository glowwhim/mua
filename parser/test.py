# -*- coding: utf-8 -*-
from parser import *
import os
import sys
import lexer


CODE_PATH = "../code/testcase.txt"
OUTPUT_PATH = "../code/output.txt"


if __name__ == '__main__':
	root_path = os.path.split(sys.argv[0])[0]
	input_path = os.path.join(root_path, CODE_PATH)
	output_path = os.path.join(root_path, OUTPUT_PATH)
	grammar_path = os.path.join(root_path, "grammar.py")
	f = open(os.path.join(root_path, CODE_PATH))
	code = f.read()
	f.close()
	context = LRContext()
	g = Grammar.load_from_file(context, grammar_path)
	token_generator = lexer.token_generator(code)
	p = Parser(g)
	p.parse("$Program", token_generator, output_path)
