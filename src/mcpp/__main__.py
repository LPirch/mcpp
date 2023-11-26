import json
from collections import defaultdict

import hydra
from tqdm import tqdm

from mcpp import REPO_ROOT
from mcpp.config import Config
from mcpp.parse import Sitter, get_call_names
from mcpp.complexity import c1, c2, c3_c4
from mcpp.vulnerability import v1, v2, v3_v4, v5, v6_v7, v8, v9, v10, v11


@hydra.main(
    version_base=None,
    config_path=str(REPO_ROOT),
    config_name="config.yaml")
def main(cfg: Config):
    if cfg.mcpp.in_path.is_dir():
        in_files = list(cfg.mcpp.in_path.glob("**/source"))
        from random import choices
        in_files = choices(in_files, k=100)
    else:
        in_files = [cfg.mcpp.in_path]

    metrics = [
        c1,
        c2,
        c3_c4,
        v1,
        v2,
        v3_v4,
        v5,
        v6_v7,
        v8,
        v9,
        v10,
        v11
    ]
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

    with open(cfg.mcpp.out_file, "w") as f:
        json.dump(results, f, indent=4)


if __name__ == '__main__':
    main()
