# -*- coding: utf-8 -*-
from parser import *


if __name__ == '__main__':
	import sys
	import lexer
	f = open(sys.argv[0].replace("/main.py", "/code.txt"))
	code = f.read()
	f.close()
	grammar_path = sys.argv[0].replace("/main.py", "/grammar.py")
	output_path = sys.argv[0].replace("/main.py", "/output.txt")
	context = LRContext()
	g = Grammar.load_from_file(context, grammar_path)
	token_generator = lexer.token_generator(code)
	p = Parser(g)
	p.parse("$Program", token_generator, output_path)
