# -*- coding: utf-8 -*-
from typing import Tuple
from defines import *


class FakeObj(object):
    value = None
    type = None
    lexeme = ""
    address_type = None

    def print_prop(self):
        pass


def add_array(x, y):
    pass


def get_func_return_type(name):
    return 0


def run_func(name):
    pass


def add_func(name, r_type):
    pass


def _get_code_address(*args):
    return 0


def _loop_begin():
    pass


def _fj_begin():
    pass


def _fj_end():
    pass


def code(*args):
    # type: (Tuple[object]) -> None
    print args


def add_var(tokenxxx):
    pass


def get_var(name):
    return 0, ""


rd = FakeObj()
fpd = FakeObj()
pd = [FakeObj(), ]


# ==============================grammar are follows==============================
# $Return -> return ;
code(DATA_TYPE_2_RETURN_CMD[DATA_TYPE_VOID])

# $Return -> return $Expr14 ;
code(DATA_TYPE_2_RETURN_CMD[pd[1].type])

# $Print -> print $Expr14 ;
code(DATA_TYPE_2_PRINT_CMD[pd[1].type])

# $ArrayDef -> data_type var_id [ int_value ] ;
pd[1].type = DATA_TYPE_ADDRESS
pd[1].address_type = fpd.type
add_array(pd[1], pd[3].value)
code(CMD_PUSH_ANY, pd[3].value * DATA_TYPE_SIZE[fpd.type])

# $DataDef -> data_type var_id ;
pd[1].type = fpd.type
add_var(pd[1])
code(CMD_PUSH_ANY, DATA_TYPE_SIZE[fpd.type])

# $MethodExpr -> var_id ( )
run_func(fpd.lexeme)
rd.lexeme = fpd.lexeme

# $Expr0 -> char_value
# $Expr0 -> int_value
# $Expr0 -> float_value
rd.type = fpd.type
code(DATA_TYPE_2_PUSH_DATA_CMD[fpd.type], fpd.value)

# $Expr0 -> $MethodExpr
rd.type = get_func_return_type(fpd.lexeme)

# $Expr0 -> var_id
var_address, token = get_var(fpd.lexeme)
rd.type = token.type
code(DATA_TYPE_2_PUSH_SEGMENT_DATA_CMD[token.type], var_address)

# $Expr1 -> var_id [ int_value ]
var_address, token = get_var(fpd.lexeme)
rd.type = token.address_type
data_type_size = DATA_TYPE_SIZE[token.address_type]
code(CMD_PUSH_FROM_ADDRESS, var_address + data_type_size * pd[2].value, data_type_size)

# $Expr1 -> $Expr0
# $Expr2 -> $Expr1
# $Expr3 -> $Expr2
# $Expr4 -> $Expr3
# $Expr5 -> $Expr4
# $Expr6 -> $Expr5
# $Expr7 -> $Expr6
# $Expr14 -> $Expr7
rd.type = fpd.type

# $Expr2 -> ! $Expr0
cmd = OPERATOR_CMD[(pd[0].lexeme, None, pd[1].type)]
rd.type = CMD_RETURN_DATA_TYPE[cmd]
code(cmd)

# $Expr2 -> & var_id
var_address, token = get_var(pd[1].lexeme)
rd.type = DATA_TYPE_ADDRESS
rd.address_type = token.type
code(CMD_PUSH_ADDRESS, var_address)

# $Expr3 -> $Expr3 * $Expr2
# $Expr4 -> $Expr4 + $Expr3
# $Expr6 -> $Expr6 < $Expr5
# $Expr7 -> $Expr7 == $Expr6
cmd = OPERATOR_CMD[(pd[1].lexeme, pd[0].type, pd[2].type)]
rd.type = CMD_RETURN_DATA_TYPE[cmd]
code(cmd)

# $Expr14 -> var_id = $Expr14
var_address, token = get_var(fpd.lexeme)
code(DATA_TYPE_2_PUSH_DATA_CMD[DATA_TYPE_INT], var_address)
cmd = OPERATOR_CMD[(pd[1].lexeme, token.type, pd[2].type)]
rd.type = CMD_RETURN_DATA_TYPE[cmd]
code(cmd)

# $Expr14 -> var_id [ int_value ] = $Expr14
var_address, token = get_var(fpd.lexeme)
var_address += DATA_TYPE_SIZE[token.address_type] * pd[2].value
code(CMD_SET_TO_ADDRESS, var_address, DATA_TYPE_SIZE[token.address_type])

# $WhileBegin -> while
_loop_begin()

# $WhileCondition -> $WhileBegin ( $Expr14 )
_fj_begin()

# $While -> $WhileCondition $Expr14 ;
_fj_end()

# $While -> $WhileCondition { $StatementList }
_fj_end()

# $FuncDefHead -> data_type var_id ( )
add_func(pd[1].lexeme, fpd.type)

# $FuncDef -> $FuncDefHead { $StatementList }
code(CMD_RETURN_VOID)

# $Program -> $FuncDefList
# $FuncDefList -> $FuncDef
# $FuncDefList -> $FuncDefList $FuncDef
# $Statement -> $Expr14 ;
# $Statement -> $Print
# $Statement -> $Return
# $Statement -> $DataDef
# $Statement -> $ArrayDef
# $Statement -> $While
# $StatementList -> $Statement
# $StatementList -> $StatementList $Statement
