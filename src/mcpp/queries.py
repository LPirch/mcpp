Q_FOR_STMT = """
(for_statement) @for_stmt
"""

Q_DO_STMT = """
(do_statement) @do_stmt
"""

Q_WHILE_STMT = """
(while_statement) @while_stmt
"""

Q_CONDITION = """
(_
    condition: ((_) @condition)
) @control_stmnt
"""

Q_BINARY_EXPRESSION = """
(binary_expression) @binary_expression
"""
