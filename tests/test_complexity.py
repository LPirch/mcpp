def test_c1_counts_if_and_loops_plus_base(extract):
    code = """
    int f(int a, int b) {
        if (a > 0) {
            a++;
        }
        for (int i = 0; i < 10; i++) {
            a += i;
        }
        while (b > 0) {
            b--;
        }
        return a;
    }
    """
    # C2 (2 loops) + 1 if + final +1 = 4
    assert extract(code, ["C1"]) == {"C1": 4}


def test_c1_counts_logical_operators_in_condition(extract):
    code = """
    int f(int a, int b) {
        if (a > 0 && b > 0) {
            a++;
        }
        return a;
    }
    """
    # 0 loops + 1 if + 1 for && + final +1 = 3
    assert extract(code, ["C1"]) == {"C1": 3}


def test_c2_counts_for_while_do_loops(extract):
    code = """
    void f() {
        for (int i = 0; i < 10; i++) {
            while (i < 5) {
                i++;
            }
        }
        do {
            ;
        } while (0);
    }
    """
    assert extract(code, ["C2"]) == {"C2": 3}


def test_c3_c4_nesting(extract):
    code = """
    void f() {
        for (int i = 0; i < 10; i++) {
            while (i < 5) {
                i++;
            }
        }
        do {
            ;
        } while (0);
    }
    """
    # only the inner while is nested inside another loop
    assert extract(code, ["C3", "C4"]) == {"C3": 1, "C4": 1}


def test_c2_counts_cpp_range_for_loop(extract):
    code = """
    void f(int arr[], int n) {
        for (int x : arr) {
            ;
        }
    }
    """
    assert extract(code, ["C2"]) == {"C2": 1}
