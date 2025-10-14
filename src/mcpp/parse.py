from pathlib import Path

from tree_sitter import Language, Parser, QueryCursor
import tree_sitter_c as ts_c
import tree_sitter_cpp as ts_cpp

from mcpp.queries import Q_ERROR_NODE, Q_CALL_NAME, Q_IDENTIFIER


LANGS = {
    "c": Language(ts_c.language()),
    "cpp": Language(ts_cpp.language())
}


class Sitter(object):
    def __init__(self, lib_path: Path, *languages):
        self.langs = {k:v for k, v in LANGS.items() if k in languages}
        self.parser = {lang: self._init_parser(lang) for lang in languages}
        self.queries = {}
        self.queries = {"Q_ERROR_NODE": Q_ERROR_NODE}

    def _init_parser(self, language: str):
        parser = Parser(self.langs[language])
        return parser

    def parse_lang(self, source: str, lang: str):
        return self.parser[lang].parse(bytes(source, "utf-8"))

    def parse(self, source: str):
        min_errors = None
        best_tree = None
        best_lang = None
        for lang in self.langs.keys():
            tree = self.parse_lang(source, lang)
            num_errors = self._count_error_nodes(tree, lang)
            if min_errors is None or num_errors < min_errors:
                best_tree = tree
                best_lang = lang
                min_errors = num_errors
        return best_tree, best_lang

    def parse_file(self, path: Path):
        with open(path, "r") as f:
            return self.parse(f.read())

    def _count_error_nodes(self, tree, lang):
        query = self.langs[lang].query(self.queries["Q_ERROR_NODE"])
        cursor = QueryCursor(query)
        return len(cursor.captures(tree.root_node))

    def add_queries(self, queries):
        self.queries.update(queries)

    def captures(self, query, node, lang):
        lang = self.langs[lang]
        cursor = QueryCursor(lang.query(self.queries[query]))
        return cursor.captures(node)


def get_call_names(sitter, root, lang):
    """ Return all function call names. """
    call_names = []
    sitter.add_queries({"Q_CALL_NAME": Q_CALL_NAME})
    for node in sitter.captures("Q_CALL_NAME", root, lang).get("name", []):
        call_names.append(node.text.decode())
    return call_names


def get_identifiers(sitter, root, lang, filter=None):
    """ Return all identifier names, optionally filtered by list of known function names. """
    identifiers = []
    sitter.add_queries({"Q_IDENTIFIER": Q_IDENTIFIER})
    for node in sitter.captures("Q_IDENTIFIER", root, lang).get("variable", []):
        identifier = node.text.decode()
        if filter is None or identifier not in filter:
            identifiers.append(identifier)
    return identifiers
