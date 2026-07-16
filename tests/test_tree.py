import pytest


def test_tree_metrics_on_minimal_function(extract):
    code = "int f() { return 1; }"
    # these values are a direct function of the grammar's AST shape for this snippet;
    # pinning them down catches any tree-sitter/grammar upgrade that reshapes the AST
    res = extract(code, ["t1", "t2", "t3"])
    assert res["t1"] == 15
    assert res["t2"] == 5
    assert res["t3"] == pytest.approx(2.3333333333333335)
