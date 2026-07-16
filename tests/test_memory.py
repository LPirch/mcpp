from mcpp.parse import Sitter


def test_m1_counts_alloc_calls(extract):
    code = """
    void f() {
        int *p = malloc(sizeof(int));
        int *q = my_alloc(10);
    }
    """
    assert extract(code, ["m1"]) == {"m1": 2}


def test_m1_skips_new_expression_query_on_c(extract):
    # 'new_expression' is a C++-only grammar node. On plain C input, m1() must not
    # even attempt that query (rather than attempt-and-catch a QueryError): under
    # tree-sitter 0.26.0, a failed Query() compile corrupts its source string
    # in place (the last byte gets overwritten with a NUL), permanently breaking
    # every other use of that same query constant for the rest of the process.
    code = """
    void f() {
        int *p = malloc(sizeof(int));
    }
    """
    sitter = Sitter("c", "cpp")
    tree, lang = sitter.parse(code)
    assert lang == "c"
    assert extract(code, ["m1"]) == {"m1": 1}


def test_m1_counts_cpp_new_expression(extract):
    code = """
    class C {};
    void f() {
        C *c = new C();
    }
    """
    assert extract(code, ["m1"]) == {"m1": 1}


def test_m1_new_expression_not_corrupted_after_processing_c_first(extract):
    # Regression test for the tree-sitter 0.26.0 query-corruption issue above: process
    # a plain-C sample (which must never touch the new_expression query) before a C++
    # sample that relies on it, and confirm the C++ result is still correct.
    c_code = """
    void f() {
        int *p = malloc(sizeof(int));
    }
    """
    cpp_code = """
    class C {};
    void f() {
        C *c = new C();
    }
    """
    assert extract(c_code, ["m1"]) == {"m1": 1}
    assert extract(cpp_code, ["m1"]) == {"m1": 1}


def test_m2_counts_pointer_dereferences(extract):
    code = """
    struct S { int field; };
    void f(int *p, int arr[10], struct S *s) {
        *p = 1;
        arr[0] = 2;
        s->field = 3;
    }
    """
    assert extract(code, ["m2"]) == {"m2": 3}
