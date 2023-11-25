from typing import List
from pathlib import Path
import logging

import hydra
from tree_sitter import Language

from mcpp import REPO_ROOT
from mcpp.config import Config


def build(build_path: Path, lib_paths: List[Path]):
    log = logging.getLogger(__name__)
    log.info("building tree-sitter library")

    if len(lib_paths) > 0:
        build_path.parent.mkdir(exist_ok=True, parents=True)
        Language.build_library(
            # Store the library in the `build` directory
            build_path.resolve(),

            # Include one or more languages
            [lib.resolve() for lib in lib_paths]
        )


@hydra.main(
    version_base=None,
    config_path=str(REPO_ROOT),
    config_name="config.yaml")
def main(cfg: Config):
    build(cfg.treesitter.build_path, cfg.treesitter.libraries)


if __name__ == '__main__':
    main()
