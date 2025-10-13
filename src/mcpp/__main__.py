import json
from pathlib import Path
from typing import List
from collections import defaultdict
from importlib.resources import files, as_file

import hydra
from tqdm import tqdm

from mcpp.config import Config
from mcpp.parse import Sitter, get_call_names
from mcpp.complexity import c1, c2, c3_c4
from mcpp.vulnerability import v1, v2, v3_v4_v5, v6_v7, v8, v9, v10, v11

from mcpp.additional import x1, x2, x3, x4
from mcpp.tree import t1, t2, t3
from mcpp.smell import s1, s2, s3, s4
from mcpp.memory import m1, m2

with as_file(files("mcpp.assets") / "config.yaml") as p:
    config_path = str(p.parent)
    config_name = str(p.name)


METRICS = {
    "C1": c1,
    "C2": c2,
    "C3": c3_c4,
    "C4": c3_c4,
    "V1": v1,
    "V2": v2,
    "V3": v3_v4_v5,
    "V4": v3_v4_v5,
    "V5": v3_v4_v5,
    "V6": v6_v7,
    "V7": v6_v7,
    "V8": v8,
    "V9": v9,
    "V10": v10,
    "V11": v11,
    "x1": x1,
    "x2": x2,
    "x3": x3,
    "x4": x4,
    "t1": t1,
    "t2": t2,
    "t3": t3,
    "s1": s1,
    "s2": s2,
    "s3": s3,
    "s4": s4,
    "m1": m1,
    "m2": m2,
}


@hydra.main(
    version_base=None,
    config_path=config_path,
    config_name=config_name)
def main(cfg: Config):
    if cfg.in_path.is_dir():
        in_files = tqdm(list(cfg.in_path.glob("**/source")))
    else:
        in_files = [cfg.in_path]

    results = extract(in_files, cfg.metrics)

    with open(cfg.out_path, "w") as f:
        json.dump(results, f, indent=4)


def extract(in_files: List[Path], metrics: List[str] = list(METRICS.keys())):
    metrics = [fun for name, fun in METRICS.items() if name in metrics]
    sitter = Sitter("c", "cpp")
    results = defaultdict(dict)
    for path in in_files:
        res = {}
        tree, lang = sitter.parse_file(path)
        root = tree.root_node
        calls = set(get_call_names(sitter, root, lang))
        for fun in metrics:
            res.update(fun(root, sitter, lang, calls))
        results[str(path)] = res
    return results


def extract_single(in_file: Path, metrics: List[str]):
    return extract([in_file], metrics)


def extract_code(code: str, metrics: List[str] = list(METRICS.keys())):
    metrics = [fun for name, fun in METRICS.items() if name in metrics]
    sitter = Sitter("c", "cpp")

    tree, lang = sitter.parse(code)
    root = tree.root_node
    calls = set(get_call_names(sitter, root, lang))
    res = {}
    for fun in metrics:
        res.update(fun(root, sitter, lang, calls))
    return res


if __name__ == '__main__':
    main()
