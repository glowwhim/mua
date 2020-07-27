# -*- coding: utf-8 -*-
from typing import Tuple
from defines import *


class FakeObj(object):
    value = None
    type = None
    lexeme = ""

    def print_prop(self):
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


def add_var(name, data_type):
    print name, data_type


def get_var(name):
    return 0, ""


rd = FakeObj()
fpd = FakeObj()
pd = [FakeObj(), ]


# ==============================grammar are follows==============================
# $Return -> return $Expr14 ;
code(DATA_TYPE_2_RETURN_CMD[pd[1].type])

# $Print -> print $Expr14 ;
code(DATA_TYPE_2_PRINT_CMD[pd[1].type])

# $CharDef -> char var_id ;
add_var(pd[1].lexeme, DATA_TYPE_CHAR)
code(DATA_TYPE_2_PUSH_DATA_CMD[DATA_TYPE_CHAR], 0)

# $IntDef -> int var_id ;
add_var(pd[1].lexeme, DATA_TYPE_INT)
code(DATA_TYPE_2_PUSH_DATA_CMD[DATA_TYPE_INT], 0)

# $FloatDef -> float var_id ;
add_var(pd[1].lexeme, DATA_TYPE_FLOAT)
code(DATA_TYPE_2_PUSH_DATA_CMD[DATA_TYPE_FLOAT], 0)

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
var_address, var_type = get_var(fpd.lexeme)
rd.type = var_type
code(DATA_TYPE_2_PUSH_SEGMENT_DATA_CMD[var_type], var_address)

# $Expr3 -> $Expr0
# $Expr4 -> $Expr3
# $Expr5 -> $Expr4
# $Expr6 -> $Expr5
# $Expr14 -> $Expr6
rd.type = fpd.type

# $Expr3 -> $Expr3 * $Expr0
# $Expr4 -> $Expr4 + $Expr3
# $Expr6 -> $Expr6 < $Expr5
cmd = OPERATOR_CMD[(pd[1].lexeme, pd[0].type, pd[2].type)]
rd.type = CMD_RETURN_DATA_TYPE[cmd]
code(cmd)

# $Expr14 -> var_id = $Expr14
var_address, var_type = get_var(fpd.lexeme)
code(DATA_TYPE_2_PUSH_DATA_CMD[DATA_TYPE_INT], var_address)
cmd = OPERATOR_CMD[(pd[1].lexeme, var_type, pd[2].type)]
rd.type = CMD_RETURN_DATA_TYPE[cmd]
code(cmd)

# $WhileBegin -> while
_loop_begin()

# $WhileCondition -> $WhileBegin ( $Expr14 )
_fj_begin()

# $While -> $WhileCondition $Expr14 ;
_fj_end()

# $While -> $WhileCondition { $StatementList }
_fj_end()

# $FuncDefHead -> int var_id ( )
add_func(pd[1].lexeme, DATA_TYPE_INT)

# $FuncDefHead -> float var_id ( )
add_func(pd[1].lexeme, DATA_TYPE_FLOAT)

# $FuncDef -> $FuncDefHead { $StatementList }
code(CMD_RETURN_INT)

# $Program -> $FuncDefList
# $FuncDefList -> $FuncDef
# $FuncDefList -> $FuncDefList $FuncDef
# $Statement -> $Expr14 ;
# $Statement -> $Print
# $Statement -> $Return
# $Statement -> $CharDef
# $Statement -> $IntDef
# $Statement -> $FloatDef
# $Statement -> $While
# $StatementList -> $Statement
# $StatementList -> $StatementList $Statement
