# -*- coding: utf-8 -*-
from semantics import *
func_params_type = []


class FakeObj(object):
    value = None
    type = None
    lexeme = ""
    address_type = None

    def print_prop(self):
        pass


rd = FakeObj()
fpd = FakeObj()
pd = [FakeObj(), ]


# ==============================grammar are follows==============================
# $Return -> return ;
func_params_size = sum([DATA_TYPE_SIZE[i] for i in func_params_type])
code(CMD_RETURN, 0, func_params_size)
func_params_type = []

# $Return -> return $Expr14 ;
func_params_size = sum([DATA_TYPE_SIZE[i] for i in func_params_type])
code(CMD_RETURN, DATA_TYPE_SIZE[pd[1].type], func_params_size)
func_params_type = []

# $Print -> print $Expr14 ;
code(DATA_TYPE_2_PRINT_CMD[pd[1].type])

# $ArrayDef -> data_type var_id [ int_value ] ;
pd[1].type = DATA_TYPE_ADDRESS
pd[1].address_type = fpd.type
variable_table.add_array(pd[1], pd[3].value)
code(CMD_PUSH_ANY, pd[3].value * DATA_TYPE_SIZE[fpd.type])

# $DataDef -> data_type var_id ;
pd[1].type = fpd.type
variable_table.add_var(pd[1])
code(CMD_PUSH_ANY, DATA_TYPE_SIZE[fpd.type])

# $MethodExprParams -> $Expr14
method_params = [fpd.type]

# $MethodExprParams -> $MethodExprParams , $Expr14
method_params.append(pd[2].type)

# $MethodExpr -> var_id ( )
# $MethodExpr -> var_id ( $MethodExprParams )
func_params_size = sum([DATA_TYPE_SIZE[i] for i in method_params])
func_name = "%s(%s)" % (fpd.lexeme, ",".join([str(i) for i in method_params]))
run_func(func_name, func_params_size)
rd.lexeme = func_name
method_params = []

# $Expr0 -> char_value
# $Expr0 -> int_value
# $Expr0 -> float_value
rd.type = fpd.type
code(DATA_TYPE_2_PUSH_DATA_CMD[fpd.type], fpd.value)

# $Expr0 -> $MethodExpr
rd.type = get_func_return_type(fpd.lexeme)

# $Expr0 -> var_id
var_address, token = variable_table.get_var(fpd.lexeme)
rd.type = token.type
code(CMD_PUSH_FROM_ADDRESS, var_address, DATA_TYPE_SIZE[token.type])

# $Expr1 -> var_id [ int_value ]
var_address, token = variable_table.get_var(fpd.lexeme)
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
var_address, token = variable_table.get_var(pd[1].lexeme)
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
var_address, token = variable_table.get_var(fpd.lexeme)
code(DATA_TYPE_2_PUSH_DATA_CMD[DATA_TYPE_INT], var_address)
cmd = OPERATOR_CMD[(pd[1].lexeme, token.type, pd[2].type)]
rd.type = CMD_RETURN_DATA_TYPE[cmd]
code(cmd)

# $Expr14 -> var_id [ int_value ] = $Expr14
var_address, token = variable_table.get_var(fpd.lexeme)
var_address += DATA_TYPE_SIZE[token.address_type] * pd[2].value
code(CMD_SET_TO_ADDRESS, var_address, DATA_TYPE_SIZE[token.address_type])

# $WhileBegin -> while
loop_begin()

# $WhileCondition -> $WhileBegin ( $Expr14 )
fj_begin()

# $While -> $WhileCondition $Expr14 ;
fj_end()

# $While -> $WhileCondition { $StatementList }
fj_end()

# $FuncDefHeadParams -> data_type var_id
func_params_type = [fpd.type]
pd[1].type = fpd.type
variable_table.add_var(pd[1])

# $FuncDefHeadParams -> $FuncDefHeadParams , data_type var_id
func_params_type.append(pd[2].type)
pd[3].type = pd[2].type
variable_table.add_var(pd[3])

# $FuncDefHead -> data_type var_id ( )
# $FuncDefHead -> data_type var_id ( $FuncDefHeadParams )
add_func("%s(%s)" % (pd[1].lexeme, ",".join([str(i) for i in func_params_type])), fpd.type)
variable_table.move_address(4)

# $FuncDef -> $FuncDefHead { $StatementList }
func_params_size = sum([DATA_TYPE_SIZE[i] for i in func_params_type])
code(CMD_RETURN, 0, func_params_size)
clear_func()
func_params_type = []

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
