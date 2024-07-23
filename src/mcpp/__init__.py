import os
from importlib import resources

from mcpp.__main__ import extract, extract_single, extract_code, METRICS


with resources.path("mcpp", "__init__.py") as root_path:
    PKG_ROOT = root_path.parents[1].resolve()
    REPO_ROOT = PKG_ROOT.parents[0].resolve()
    os.environ['PKG_ROOT'] = str(PKG_ROOT)
    os.environ['REPO_ROOT'] = str(REPO_ROOT)
