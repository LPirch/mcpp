from importlib.resources import files
from typing import List
from pathlib import Path

import hydra
from loguru import logger as log
from tree_sitter import Language

from mcpp.config import Config


with files("mcpp.assets") / "config.yaml" as p:
    config_path = str(p.parent)
    config_name = str(p.name)


def build(build_path: Path, lib_paths: List[Path]):
    log.info("building tree-sitter library")

    if len(lib_paths) > 0:
        build_path.parent.mkdir(exist_ok=True, parents=True)
        Language.build_library(
            # Store the library in the `build` directory
            str(build_path.resolve()),

            # Include one or more languages
            [str(lib.resolve()) for lib in lib_paths]
        )


@hydra.main(
    version_base=None,
    config_path=config_path,
    config_name=config_name)
def main(cfg: Config):
    build(cfg.treesitter.build_path, cfg.treesitter.libraries)


if __name__ == '__main__':
    main()
