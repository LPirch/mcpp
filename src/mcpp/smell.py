def s1(root, sitter, lang, calls=None):
    QUERY = "(number_literal) @num"
    sitter.add_queries({"Q_NUMBER_LITERAL": QUERY})
    number_literals = sitter.captures("Q_NUMBER_LITERAL", root, lang).get("num", [])
    number_literals = [node.text.decode("utf8") for node in number_literals]
    number_literals = [
        int(s)
        for s in number_literals
        if s.isnumeric() or ((s.startswith("+") or s.startswith("-")) and s[1:].isnumeric())]
    # only non-trivial constants
    number_literals = [x for x in number_literals if x not in [-1, 0, 1]]
    return {
        "s1": len(number_literals)
    }


def s2(root, sitter, lang, calls=None):
    QUERY = "(goto_statement) @stmt"
    sitter.add_queries({"Q_GOTO_STMT": QUERY})
    goto_statements = sitter.captures("Q_GOTO_STMT", root, lang).get("stmt", [])
    return {
        "s2": len(goto_statements)
    }


def s3(root, sitter, lang, calls=None):
    QUERY = "(declaration (init_declarator (function_declarator) @decl))"
    sitter.add_queries({"Q_FUNCTION_POINTERS": QUERY})
    function_pointers = sitter.captures("Q_FUNCTION_POINTERS", root, lang).get("decl", [])
    return {
        "s3": len(function_pointers)
    }


def s4(root, sitter, lang, calls=None):
    QUERY = "(expression_statement (call_expression) @expr)"
    sitter.add_queries({"Q_CALLS_WO_RETURN": QUERY})
    functions_wo_return = sitter.captures("Q_CALLS_WO_RETURN", root, lang).get("expr", [])
    return {
        "s4": len(functions_wo_return)
    }
