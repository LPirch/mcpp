from mcpp.queries import Q_BINARY_EXPR, Q_IDENTIFIER, Q_NUMBER


def x1(root, sitter, lang, calls=None):
    QUERY = "(return_statement) @stmt"
    sitter.add_queries({"Q_RETURN_STMT": QUERY})
    return_statements = sitter.captures("Q_RETURN_STMT", root, lang).get("stmt", [])
    return {
        "x1": len(return_statements)
    }


def x2(root, sitter, lang, calls=None):
    QUERY = "(cast_expression) @expr"
    sitter.add_queries({"Q_CAST_EXPR": QUERY})
    cast_exprs = sitter.captures("Q_CAST_EXPR", root, lang).get("expr", [])
    return {
        "x2": len(cast_exprs)
    }


def x3(root, sitter, lang, calls=None):
    QUERY = "(declaration) @stmt"
    sitter.add_queries({"Q_VAR_DECL": QUERY})
    var_decls = sitter.captures("Q_VAR_DECL", root, lang).get("stmt", [])
    return {
        "x3": len(var_decls)
    }


def x4(root, sitter, lang, calls=None):
    """ Max # of operands in expression
    """
    sitter.add_queries({
        "Q_BINARY_EXPR": Q_BINARY_EXPR,
        "Q_IDENTIFIER": Q_IDENTIFIER,
        "Q_NUMBER": Q_NUMBER,
    })

    num_ops = [0]

    for expr in sitter.captures("Q_BINARY_EXPR", root, lang).get("expr", []):
        identifiers = sitter.captures("Q_IDENTIFIER", expr, lang).get("variable", [])
        constants = sitter.captures("Q_NUMBER", expr, lang).get("constant", [])
        num_ops.append(len(identifiers) + len(constants))

    return {
        "x4": max(num_ops),
    }
