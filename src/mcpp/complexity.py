from mcpp.parse import Sitter
from mcpp.queries import Q_FOR_STMT, Q_DO_STMT, Q_WHILE_STMT


def c1(path, sitter: Sitter):
    """Cyclomatic complexity: number of for, while and do-while loops."""
    queries = {
        "Q_FOR_STMT": Q_FOR_STMT,
        "Q_DO_STMT": Q_DO_STMT,
        "Q_WHILE_STMT": Q_WHILE_STMT
    }
    sitter.add_queries(queries)
    tree, lang = sitter.parse_file(path)
    root = tree.root_node

    complexity = 0
    for query in queries.keys():
        complexity += len(sitter.captures(query, root, lang))
    return complexity
