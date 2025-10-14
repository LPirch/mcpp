from mcpp.queries import Q_FOR_STMT, Q_DO_STMT, Q_WHILE_STMT, \
    Q_FOR_RANGE_STMT, Q_BINARY_EXPR, Q_CONDITION


def c1(root, sitter, lang, calls=None):
    """Cyclomatic complexity (McCabe): 
        number conditional predicates + number of loop statements + 1
    """
    sitter.add_queries({
        "Q_BINARY_EXPR": Q_BINARY_EXPR,
        "Q_CONDITION": Q_CONDITION,
        "Q_FOR_STMT": Q_FOR_STMT,
        "Q_DO_STMT": Q_DO_STMT,
        "Q_WHILE_STMT": Q_WHILE_STMT,
    })
    logical_ops = [
        "&&", "||", "and", "or",
    ]
    loop_stmts = [
        "for_statement", "while_statement",
    ]

    complexity = c2(root, sitter, lang, calls)["C2"]

    # if statements
    for condition in sitter.captures("Q_CONDITION", root, lang).get("condition", []):
        if condition.parent.type in loop_stmts:
            continue
        complexity += 1
        for expr in sitter.captures("Q_BINARY_EXPR", condition, lang).get("expr", []):
            if len(expr.children) != 3:
                continue
            left, op, right = expr.children
            if op.text.decode() in logical_ops:
                complexity += 1
    complexity += 1
    return {
        "C1": complexity
    }


def c2(root, sitter, lang, calls=None):
    """number of for, while and do-while loops"""
    loops = {
        "Q_FOR_STMT": Q_FOR_STMT,
        "Q_FOR_RANGE_STMT": Q_FOR_RANGE_STMT,
        "Q_WHILE_STMT": Q_WHILE_STMT,
        "Q_DO_STMT": Q_DO_STMT,
    } 
    sitter.add_queries(loops)
    complexity = 0
    for query in loops.keys():
        complexity += len(sitter.captures(query, root, lang).get("stmt", []))
    return {
        "C2": complexity
    }


def c3_c4(root, sitter, lang, calls=None):
    """
    C3: number of nested for, while and do-while loops
    C4: maximum nesting depth

    - count all loops that have some loop ancestor
    - count ancestors that are also loops
    """
    loops = {
        "Q_FOR_STMT": Q_FOR_STMT,
        "Q_FOR_RANGE_STMT": Q_FOR_RANGE_STMT,
        "Q_DO_STMT": Q_DO_STMT,
        "Q_WHILE_STMT": Q_WHILE_STMT
    }
    sitter.add_queries(loops)
    c3_val = 0
    c4_val = 0
    for query in loops.keys():
        for loop_node in sitter.captures(query, root, lang).get("stmt", []):
            nesting_level = _loop_nesting_level(loop_node)
            if nesting_level > 0:
                c3_val += 1
            c4_val = max(c4_val, nesting_level)
    return {
        "C3": c3_val,
        "C4": c4_val
    }


def _loop_nesting_level(node):
    loop_types = [
        "do_statement",
        "while_statement",
        "for_statement",
        "for_range_loop",
    ]
    parent = node.parent
    num_loop_ancestors = 0
    while parent is not None:
        if parent.type in loop_types:
            num_loop_ancestors += 1
        parent = parent.parent
    return num_loop_ancestors
