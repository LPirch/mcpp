import json
from collections import defaultdict

import hydra
from tqdm import tqdm

from mcpp import REPO_ROOT
from mcpp.config import Config
from mcpp.parse import Sitter
from mcpp.complexity import c1, c2, c3_c4
from mcpp.vulnerability import v1, v2, v3_v4, v5


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
        v5
    ]
    sitter = Sitter(cfg.treesitter.build_path, "c", "cpp")
    results = defaultdict(dict)
    for path in tqdm(in_files):
        res = {}
        for fun in metrics:
            res.update(fun(path, sitter))
        results[str(path)] = res

    with open(cfg.mcpp.out_file, "w") as f:
        json.dump(results, f, indent=4)


if __name__ == '__main__':
    main()
