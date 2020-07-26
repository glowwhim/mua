# -*- coding: utf-8 -*-
from typing import Tuple, List, Set
import lexer
from defines import *

ACTION_S = 1
ACTION_R = 2
ACTION_ACC = 3


def is_terminal(sSymbol):
	"""
	:type sSymbol: str
	"""
	return not sSymbol.startswith("$")


class LRTable(object):

	action_table = {}
	goto_table = {}

	def set_action(self, state, terminal, action, value):
		# type: (int, str, int, int) -> None
		if state not in self.action_table:
			self.action_table[state] = {}
		self.action_table[state][terminal] = action, value

	def set_goto(self, state, non_terminal, goto):
		if state not in self.goto_table:
			self.goto_table[state] = {}
		self.goto_table[state][non_terminal] = goto

	def get_action(self, state, symbol):
		# type: (int, str) -> str
		return self.action_table[state][symbol]

	def get_goto(self, state, symbol):
		# type: (int, str) -> int
		return self.goto_table[state][symbol]

	def print_table(self):
		setTerminal = set()
		setNonTerminal = set()
		for dctSymbol in self.action_table.itervalues():
			for sSymbol in dctSymbol:
				setTerminal.add(sSymbol)
		for dctSymbol in self.goto_table.itervalues():
			for sSymbol in dctSymbol:
				setNonTerminal.add(sSymbol)
		lstTitle = []
		lstTitle.extend(setTerminal)
		lstTitle.extend(setNonTerminal)
		print "\t\t" + "\t\t".join(lstTitle)
		for i in xrange(10000):
			lstPrint = [str(i)]
			bIsEnd = True
			for sSymbol in lstTitle:
				if i in self.action_table and sSymbol in self.action_table[i]:
					bIsEnd = False
					iAction, iValue = self.action_table[i][sSymbol]
					if iAction == ACTION_S:
						sAction = "s%d" % iValue
					elif iAction == ACTION_R:
						sAction = "r%d" % iValue
					elif iAction == ACTION_ACC:
						sAction = "acc"
					else:
						sAction = ""
					lstPrint.append(sAction)
				elif i in self.goto_table and sSymbol in self.goto_table[i]:
					bIsEnd = False
					lstPrint.append(str(self.goto_table[i][sSymbol]))
				else:
					lstPrint.append(" ")
			if bIsEnd:
				break
			print "\t\t".join(lstPrint)


class LRContext(object):

	all_production = {}
	all_lr_item = {}

	def add_production(self, production):
		"""
		:type production: Production
		"""
		if production.get_id() in self.all_production:
			raise Exception("production exist")
		self.all_production[production.get_id()] = production

	def get_production(self, _id):
		"""
		:rtype: Production
		"""
		return self.all_production.get(_id)

	def production_iter(self):
		"""
		:rtype: list
		"""
		return self.all_production.itervalues()

	def add_lr_item(self, item):
		"""
		:type item: LRItem
		"""
		if item.get_key() in self.all_lr_item:
			raise Exception("lr item exist")
		self.all_lr_item[item.get_key()] = item

	def get_lr_item(self, key):
		"""
		:rtype: LRItem
		"""
		return self.all_lr_item.get(key)

	def lr_item_iter(self):
		"""
		:rtype: list
		"""
		return self.all_lr_item.itervalues()


class LRObject(object):

	def __init__(self, context):
		# type: (LRContext) -> None
		self.context = context

	def get_context(self):
		# type: () -> LRContext
		return self.context


class Production(LRObject):

	_id = None  # type: int
	name = None  # type: str
	production = None  # type: List[str]
	semantics_action = ""

	def __str__(self):
		return "%s -> %s {%s}" % (self.name, " ".join(self.production), self.semantics_action)

	def __init__(self, context, _id, name, production, semantics_action=""):
		# type: (LRContext, int, str, str, List[str]) -> None
		LRObject.__init__(self, context)
		self._id = _id
		self.name = name
		self.production = production.split(" ")
		self.semantics_action = semantics_action
		context.add_production(self)

	def get_id(self):
		# type: () -> int
		return self._id

	def get_name(self):
		# type: () -> str
		return self.name

	def get_production(self):
		# type: () -> List[str]
		return self.production

	def get_semantics_action(self):
		# type: () -> List[str]
		return self.semantics_action

	def set_semantics_action(self, semantics_action):
		# type: (str) -> None
		self.semantics_action = semantics_action


class Grammar(LRObject):

	production_list = []
	terminal_set = set()
	non_terminal_set = set()
	all_first = {}

	@classmethod
	def load_from_file(cls, context, path):
		f = open(path)
		grammar = Grammar(context)
		_id = 0
		cur_production = []  # type: List[Production]
		action_code_list = []
		grammar_begin = False
		for line in f.readlines():
			if not grammar_begin:
				line = line.strip()
			if line == "# ==============================grammar are follows==============================":
				grammar_begin = True
				continue
			if not line or not grammar_begin:
				continue
			if line.startswith("# $"):
				line = line[2:].strip()
				name, production = line.strip().split(" -> ")
				if action_code_list:
					semantics_action = "\n".join(action_code_list)
					for p in cur_production:
						p.set_semantics_action(semantics_action)
						grammar.add_production(p)
					cur_production = []
					action_code_list = []
				cur_production.append(Production(grammar.get_context(), _id, name, production))
			else:
				action_code_list.append(line)
			_id += 1
		semantics_action = "\n".join(action_code_list)
		for p in cur_production:
			p.set_semantics_action(semantics_action)
			grammar.add_production(p)
		f.close()
		grammar.compute_first()
		return grammar

	def add_production(self, p):
		# type: (Production) -> None
		self.production_list.append(p)
		self.non_terminal_set.add(p.get_name())
		for s in p.get_production():
			if is_terminal(s):
				self.terminal_set.add(s)

	def first(self, symbol_list):
		# type: (List[str]) -> Set[str]
		result = {SYMBOL_END}
		for symbol in symbol_list:
			result.remove(SYMBOL_END)
			result.update(self.all_first[symbol])
			if SYMBOL_END not in result:
				break
		return result

	def compute_first(self):
		self.all_first[SYMBOL_END] = {SYMBOL_END}
		self.all_first[SYMBOL_START] = {SYMBOL_END}
		for s in self.terminal_set:
			self.all_first[s] = {s}
		for s in self.non_terminal_set:
			self.all_first[s] = set()
		changed = True
		while changed:
			changed = False
			for p in self.production_list:
				f = self.all_first[p.get_name()]
				for s in self.first(p.get_production()):
					changed = changed or s not in f
					f.add(s)


class LRItem(LRObject):

	key = None  # type: Tuple

	@classmethod
	def create(cls, context, production_id, dot_index, look_ahead):
		# type: (LRContext, int, int, str) -> LRItem
		key = (production_id, dot_index, look_ahead)
		exist = context.get_lr_item(key)
		if exist:
			return exist
		i = LRItem(context)
		i.key = key
		context.add_lr_item(i)
		return i

	def __str__(self):
		str1 = " ".join(self.get_symbols(0, self.get_dot_index()))
		str2 = " ".join(self.get_symbols(self.get_dot_index()))
		return "%s -> %s · %s, %s" % (self.get_production().get_name(), str1, str2, self.get_look_ahead())

	def get_key(self):
		return self.key

	def get_production_id(self):
		return self.get_key()[0]

	def get_production(self):
		# type: () -> Production
		return self.get_context().get_production(self.get_production_id())

	def get_dot_index(self):
		return self.get_key()[1]

	def get_look_ahead(self):
		return self.get_key()[2]

	def create_forward_item(self):
		pid = self.get_production().get_id()
		dot_index = self.get_dot_index() + 1
		return LRItem.create(self.get_context(), pid, dot_index, self.get_look_ahead())

	def get_symbol(self, index=None):
		# type: (int) -> str
		if index is None:
			index = self.get_dot_index()
		if len(self.get_production().get_production()) <= index:
			return SYMBOL_END
		return self.get_production().get_production()[index]

	def get_symbols(self, from_index, to_index=None):
		# type: (int, int) -> List[str]
		p = self.get_production().get_production()
		if to_index is None:
			to_index = len(p)
		return p[from_index:to_index]


class LRClosure(LRObject):

	def __init__(self, grammar, start_items):
		# type: (Grammar, List[LRItem]) -> None
		LRObject.__init__(self, grammar.get_context())
		self.start_items = start_items
		self.all_items = [] + start_items
		i = 0
		while i < len(self.all_items):
			self._extend(grammar, self.all_items[i])
			i += 1

	def _extend(self, grammar, lr_item):
		# type: (Grammar, LRItem) -> None
		next_symbol = lr_item.get_symbol()
		if is_terminal(next_symbol):
			return
		follow_list = lr_item.get_symbols(lr_item.get_dot_index() + 1)
		follow_list.append(lr_item.get_look_ahead())
		follow_set = grammar.first(follow_list)
		for p in self.get_context().production_iter():
			if p.get_name() != next_symbol:
				continue
			for look_ahead in follow_set:
				new_lr_item = LRItem.create(self.get_context(), p.get_id(), 0, look_ahead)
				if new_lr_item in self.all_items:
					continue
				self.all_items.append(new_lr_item)

	def get_all_items(self):
		# type: () -> List[LRItem]
		return self.all_items

	def get_begin_items(self):
		# type: () -> List[LRItem]
		return self.start_items

	def print_closure(self):
		for i in self.all_items:
			print i


class LRAutomata(LRObject):

	def __init__(self, grammar, start_symbol):
		# type: (Grammar, str) -> None
		LRObject.__init__(self, grammar.get_context())
		start_production = Production(self.get_context(), -1, SYMBOL_START, start_symbol)
		closure0 = LRClosure(grammar, [LRItem.create(self.get_context(), start_production.get_id(), 0, SYMBOL_END)])
		self.all_closure = [closure0]
		self.closure_mapping = {0: {}}
		self._extend(grammar, 0)

	def _is_closure_exist(self, closure_begin_item):
		# type: (List[LRItem]) -> int
		for _id, closure in enumerate(self.all_closure):
			for item in closure_begin_item:
				if item not in closure.get_begin_items():
					break
			else:
				return _id
		return -1

	def _extend(self, grammar, closure_id):
		# type: (Grammar, int) -> None
		closure = self.all_closure[closure_id]
		already_extend_symbol = []
		for item in closure.get_all_items():
			item_cur_symbol = item.get_symbol()
			if item_cur_symbol == SYMBOL_END:
				continue
			if item_cur_symbol in already_extend_symbol:
				continue
			already_extend_symbol.append(item_cur_symbol)
			new_closure_begin_items = []
			for i in closure.get_all_items():
				if i.get_symbol() == item_cur_symbol:
					new_closure_begin_items.append(i.create_forward_item())
			exist_id = self._is_closure_exist(new_closure_begin_items)
			if exist_id >= 0:
				self.closure_mapping[closure_id][item_cur_symbol] = exist_id
				continue
			new_closure_id = len(self.all_closure)
			oNewClosure = LRClosure(grammar, new_closure_begin_items)
			self.all_closure.append(oNewClosure)
			self.closure_mapping[new_closure_id] = {}
			self.closure_mapping[closure_id][item_cur_symbol] = new_closure_id
			self._extend(grammar, new_closure_id)

	def create_table(self):
		# type: () -> LRTable
		table = LRTable()
		for state, closure in enumerate(self.all_closure):
			for item in closure.get_all_items():
				if item.get_symbol() == SYMBOL_END:
					if item.get_production().get_name() == SYMBOL_START:
						table.set_action(state, item.get_look_ahead(), ACTION_ACC, 0)
					else:
						table.set_action(state, item.get_look_ahead(), ACTION_R, item.get_production_id())
			for symbol, goto in self.closure_mapping[state].iteritems():
				if is_terminal(symbol):
					table.set_action(state, symbol, ACTION_S, goto)
				else:
					table.set_goto(state, symbol, goto)
		return table

	def print_automata(self):
		for i, j in enumerate(self.all_closure):
			print ""
			print i
			j.print_closure()


class Parser(object):

	def __init__(self, g):
		# type: (Grammar) -> None
		self.grammar = g

	def parse(self, non_terminal, token_generator, output_path):
		# type: (str, List[lexer.Token], str) -> object
		import codeparser
		code_parser = codeparser.CodeParser()
		lr_automata = LRAutomata(self.grammar, non_terminal)
		table = lr_automata.create_table()
		cursor = 0
		state_stack = [0]
		token_stack = [SYMBOL_END]
		for token in token_generator:
			action, value = table.get_action(state_stack[-1], token.get_symbol())
			while action == ACTION_R:
				p = self.grammar.get_context().get_production(value)
				prod_list = []
				for _ in xrange(len(p.get_production())):
					prod_list.insert(0, token_stack.pop())
					state_stack.pop()
				token_stack.append(lexer.Token(p.get_name()))
				state_stack.append(table.get_goto(state_stack[-1], token_stack[-1].get_symbol()))
				action, value = table.get_action(state_stack[-1], token.get_symbol())
				code_parser.do_semantics(p, token_stack[-1], prod_list)
			if action == ACTION_S:
				token_stack.append(token)
				state_stack.append(value)
				cursor += 1
			elif action == ACTION_ACC:
				code_parser.do_semantics_finish()
				print "==============================lr parse acc=============================="
			else:
				print "error"
				return
		code_parser.print_code()
		code_parser.output_code(output_path)
