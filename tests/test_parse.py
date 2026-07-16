from mcpp.parse import Sitter, get_call_names, get_identifiers


def test_parse_picks_c_for_plain_c_source():
    sitter = Sitter("c", "cpp")
    code = """
    void f() {
        int *p = malloc(sizeof(int));
    }
    """
    tree, lang = sitter.parse(code)
    assert lang == "c"
    assert tree.root_node.type == "translation_unit"


def test_parse_picks_cpp_for_range_based_for():
    sitter = Sitter("c", "cpp")
    code = """
    void f(int arr[], int n) {
        for (int x : arr) {
            ;
        }
    }
    """
    tree, lang = sitter.parse(code)
    assert lang == "cpp"


def test_get_call_names_returns_one_entry_per_call():
    sitter = Sitter("c", "cpp")
    code = """
    void g(int x);
    void f() {
        g(1);
        g(2);
    }
    """
    tree, lang = sitter.parse(code)
    assert get_call_names(sitter, tree.root_node, lang) == ["g", "g"]


def test_get_identifiers_filters_given_names():
    sitter = Sitter("c", "cpp")
    code = """
    void g(int x);
    void f() {
        int a;
        g(a);
    }
    """
    tree, lang = sitter.parse(code)
    root = tree.root_node
    all_names = set(get_identifiers(sitter, root, lang))
    assert "g" in all_names

    filtered_names = set(get_identifiers(sitter, root, lang, filter={"g"}))
    assert "g" not in filtered_names
    assert "a" in filtered_names
