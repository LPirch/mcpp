Q_ERROR_NODE = """
(ERROR) @error_node
"""

Q_FOR_STMT = """
(for_statement) @for_stmt
"""

Q_DO_STMT = """
(do_statement) @do_stmt
"""

Q_WHILE_STMT = """
(while_statement) @while_stmt
"""

Q_IF_STMT = """
(if_statement) @if_stmt
"""

Q_SWITCH_STMT = """
(switch_statement) @switch_stmt
"""


Q_CONDITION = """
(_
    condition: ((_) @condition)
) @control_stmnt
"""

Q_BINARY_EXPR = """
(binary_expression) @binary_expression
"""

Q_CALL_NAME = """
(call_expression
    function: ((identifier) @name)
) @call
"""

Q_ARGLIST = """
(call_expression
    arguments: ((argument_list) @args)
) @call
"""

Q_IDENTIFIER = """
(identifier) @variable
"""

Q_FUNCTION_PARAMETER = """
(parameter_declaration) @param
"""

Q_POINTER_EXPR = """
(pointer_expression) @pointer
"""

Q_ASSIGNMENT_EXPR = """
(assignment_expression) @assignment
"""

Q_IF_WITHOUT_ELSE = """
(if_statement
    condition: ((_) @if)
    consequence: ((_) @then)
    !alternative
) @if_stmt
"""