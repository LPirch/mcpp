# %%
from pathlib import Path
from tree_sitter import Language, Parser


Q_ERROR_NODE = """
(ERROR) @error_node
"""

class Sitter(object):
    def __init__(self, library_path: Path, *languages):
        self._library_path = library_path
        self.langs = {lang: self._init_lang(lang) for lang in languages}
        self.parser = {lang: self._init_parser(lang) for lang in languages}
        self.queries = {}
        self.queries = {"Q_ERROR_NODE": Q_ERROR_NODE}

    def _init_lang(self, lang: str):
        return Language(self._library_path, lang)

    def _init_parser(self, language: str):
        parser = Parser()
        parser.set_language(self.langs[language])
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
        return len(query.captures(tree.root_node))

    def add_queries(self, queries):
        self.queries.update(queries)

    def captures(self, query, node, lang):
        lang = self.langs[lang]
        return lang.query(self.queries[query]).captures(node)
