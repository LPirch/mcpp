from pathlib import Path

from mcpp.__main__ import extract_code, METRICS

EXAMPLES_DIR = Path(__file__).resolve().parents[1] / "examples" / "data"

EXPECTED_METRICS = {
    "C1": 12,
    "C2": 2,
    "C3": 1,
    "C4": 1,
    "V1": 2,
    "V2": 1,
    "V3": 6,
    "V4": 8,
    "V5": 5,
    "V6": 4,
    "V7": 2,
    "V8": 3,
    "V9": 1,
    "V10": 6,
    "V11": 3,
    "x1": 0,
    "x2": 0,
    "x3": 3,
    "x4": 6,
    "t1": 159,
    "t2": 11,
    "t3": 2.981132075471698,
    "s1": 3,
    "s2": 0,
    "s3": 0,
    "s4": 1,
    "m1": 0,
    "m2": 0,
}


def test_all_metrics_on_shipped_example():
    """Broad end-to-end regression net: every metric, run through the real
    Sitter/query pipeline, against the sample file shipped in examples/data/source."""
    source = (EXAMPLES_DIR / "source").read_text()
    result = extract_code(source, list(METRICS.keys()))
    assert result == EXPECTED_METRICS
