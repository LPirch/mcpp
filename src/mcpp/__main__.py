import json
from collections import defaultdict
from importlib.resources import files

import hydra
from tqdm import tqdm

from mcpp import REPO_ROOT
from mcpp.config import Config
from mcpp.parse import Sitter, get_call_names
from mcpp.complexity import c1, c2, c3_c4
from mcpp.vulnerability import v1, v2, v3_v4, v5, v6_v7, v8, v9, v10, v11

with files("mcpp.assets") / "config.yaml" as p:
    config_path = str(p.parent)
    config_name = str(p.name)


METRICS = {
    "C1": c1,
    "C2": c2,
    "C3": c3_c4,
    "C4": c3_c4,
    "V1": v1,
    "V2": v2,
    "V3": v3_v4,
    "V4": v3_v4,
    "V5": v5,
    "V6": v6_v7,
    "V7": v6_v7,
    "V8": v8,
    "V9": v9,
    "V10": v10,
    "V11": v11
}

@hydra.main(
    version_base=None,
    config_path=config_path,
    config_name=config_name)
def main(cfg: Config):
    results = run(config)

    with open(cfg.out_path, "w") as f:
        json.dump(results, f, indent=4)


def run(cfg: Config):
    if cfg.in_path.is_dir():
        in_files = list(cfg.in_path.glob("**/source"))
        from random import choices
        in_files = choices(in_files, k=100)
    else:
        in_files = [cfg.in_path]

    metrics = [fun for name, fun in METRICS.items() if name in cfg.metrics]
    sitter = Sitter(cfg.treesitter.build_path, "c", "cpp")
    results = defaultdict(dict)
    for path in tqdm(in_files):
        res = {}
        tree, lang = sitter.parse_file(path)
        root = tree.root_node
        calls = set(get_call_names(sitter, root, lang))
        for fun in metrics:
            res.update(fun(root, sitter, lang, calls))
        results[str(path)] = res


if __name__ == '__main__':
    main()
