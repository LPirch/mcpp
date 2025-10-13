from mcpp.queries import Q_CALL_NAME, Q_NEW_EXPRESSION, Q_SUBSCRIPT_EXPR, Q_FIELD_EXPR

def m1(root, sitter, lang, calls=None):
    """ # memory allocations

    Capture libc memory allocations as well as potential wrappers or individual alloctors.
    """
    sitter.add_queries({
        "Q_CALL_NAME": Q_CALL_NAME,
        "Q_NEW_EXPRESSION": Q_NEW_EXPRESSION,
    })

    num_allocations = 0

    # Number of calls to allocation functions
    for name in sitter.captures("Q_CALL_NAME", root, lang).get("name", []):
        if "alloc" in name.text.decode("utf-8").lower():
            num_allocations += 1

    # Number of new object instantiations
    num_new_expressions = len(sitter.captures("Q_NEW_EXPRESSION", root, lang).get("expr", []))
    
    return {
        "m1": num_allocations + num_new_expressions,
    }

def m2(root, sitter, lang, calls=None):
    """ # ptr dereferences
    """
    sitter.add_queries({
        "Q_CALL_NAME": Q_CALL_NAME,
        "Q_NEW_EXPRESSION": Q_NEW_EXPRESSION,
        "Q_SUBSCRIPT_EXPR": Q_SUBSCRIPT_EXPR,
        "Q_FIELD_EXPR": Q_FIELD_EXPR,
    })

    num_ptr_expressions = 0

    # Number of pointer dereferences using the asterisk syntax (*)
    for ptr in sitter.captures("Q_POINTER_EXPR", root, lang).get("pointer", []):
        if ptr.text.decode("utf-8").startswith("*"):
            num_ptr_expressions += 1

    # Number of pointer dereferences using the subscript syntax ([])
    num_subscript_expressions = len(sitter.captures("Q_SUBSCRIPT_EXPR", root, lang).get("expr", []))

    # Number of pointer dereferences using the field expression syntax (ptr->field)
    num_field_expressions = len(sitter.captures("Q_FIELD_EXPR", root, lang).get("expr", []))
    
    return {
        "m2": num_ptr_expressions + num_subscript_expressions + num_field_expressions,
    }
