def test_x1_counts_return_statements(extract):
    code = """
    int f(int a) {
        if (a > 0) { return 1; }
        return 0;
    }
    """
    assert extract(code, ["x1"]) == {"x1": 2}


def test_x2_counts_cast_expressions(extract):
    code = """
    void f(void *p) {
        int x = (int)p;
        double y = (double)x;
    }
    """
    assert extract(code, ["x2"]) == {"x2": 2}


def test_x3_counts_declaration_statements(extract):
    code = """
    void f() {
        int a;
        int b, c;
        double d = 1.0;
    }
    """
    # each declaration statement counts once, regardless of how many declarators it holds
    assert extract(code, ["x3"]) == {"x3": 3}


def test_x4_max_operands_in_binary_expression(extract):
    code = """
    void f(int a, int b, int c, int d) {
        int x = a + b;
        int y = a + b + c + d;
    }
    """
    # counts all identifier/number descendants of a binary_expression subtree, so the
    # outermost (fully nested) expression a+b+c+d dominates with 4
    assert extract(code, ["x4"]) == {"x4": 4}
