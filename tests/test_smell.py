def test_s1_counts_non_trivial_magic_numbers(extract):
    code = """
    void f() {
        int a = 42;
        int b = -1;
        int c = 0;
        int d = 1;
        int e = 100;
    }
    """
    # -1 is not recognized as a signed literal: the number_literal node only covers "1"
    # (the unary minus is a separate sibling), so it parses as 1 and gets filtered out
    # like the other trivial constants (-1, 0, 1). Only 42 and 100 remain non-trivial.
    assert extract(code, ["s1"]) == {"s1": 2}


def test_s2_counts_goto_statements(extract):
    code = """
    void f() {
        goto end;
        end:
        ;
    }
    """
    assert extract(code, ["s2"]) == {"s2": 1}


def test_s3_counts_function_pointer_params(extract):
    code = """
    void f(int (*callback)(int)) {
        ;
    }
    """
    assert extract(code, ["s3"]) == {"s3": 1}


def test_s3_counts_initialized_function_pointer_locals(extract):
    code = """
    int add(int a, int b) { return a + b; }
    void f(int (*callback)(int)) {
        int (*fp)(int, int) = add;
    }
    """
    # local function-pointer declarations only match the query when they carry an
    # initializer (init_declarator); an uninitialized "int (*fp)(int, int);" would not
    # be counted here - existing behavior, pinned down so it doesn't regress silently
    assert extract(code, ["s3"]) == {"s3": 2}


def test_s4_counts_calls_without_return_value_used(extract):
    code = """
    int g();
    void f() {
        g();
        int x = g();
    }
    """
    assert extract(code, ["s4"]) == {"s4": 1}
