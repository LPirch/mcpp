import json
from collections import defaultdict

import hydra
from tqdm import tqdm

from mcpp import REPO_ROOT
from mcpp.config import Config
from mcpp.parse import Sitter
from mcpp.complexity import c1


@hydra.main(
    version_base=None,
    config_path=str(REPO_ROOT),
    config_name="config.yaml")
def main(cfg: Config):
    if cfg.mcpp.in_path.is_dir():
        in_files = list(cfg.mcpp.in_path.glob("**/source"))
        from random import choices
        in_files = choices(in_files, k=1_000)
    else:
        in_files = [cfg.mcpp.in_path]

    metrics = {
        "C1": c1
    }
    sitter = Sitter(cfg.treesitter.build_path, "c", "cpp")
    results = defaultdict(dict)
    for path in tqdm(in_files):
        results[str(path)] = {m: fun(path, sitter) for m, fun in metrics.items()}

    with open(cfg.mcpp.out_file, "w") as f:
        json.dump(results, f, indent=4)


if __name__ == '__main__':
    main()
