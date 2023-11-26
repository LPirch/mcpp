import json
from collections import defaultdict

import hydra
from tqdm import tqdm

from mcpp import REPO_ROOT
from mcpp.config import Config
from mcpp.parse import Sitter
from mcpp.complexity import c1, c2, c3_c4
from mcpp.vulnerability import vd1, vd2


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

    metrics = {
        "C1": c1,
        "C2": c2,
        "C3_C4": c3_c4,
        "VD1": vd1,
        "VD2": vd2
    }
    sitter = Sitter(cfg.treesitter.build_path, "c", "cpp")
    results = defaultdict(dict)
    for path in tqdm(in_files):
        res = {}
        for m, fun in metrics.items():
            res.update(fun(path, sitter))
        results[str(path)] = res

    with open(cfg.mcpp.out_file, "w") as f:
        json.dump(results, f, indent=4)


if __name__ == '__main__':
    main()
