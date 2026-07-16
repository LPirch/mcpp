from pathlib import Path

import pytest

from mcpp.__main__ import extract_code

EXAMPLES_DIR = Path(__file__).resolve().parents[1] / "examples" / "data"


@pytest.fixture
def extract():
    """Run extract_code for a snippet, optionally restricted to a subset of metrics."""

    def _extract(code, metrics=None):
        return extract_code(code, metrics)

    return _extract
