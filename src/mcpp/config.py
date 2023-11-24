from typing import List
from dataclasses import dataclass
from pathlib import Path

from hydra.core.config_store import ConfigStore


@dataclass
class PathConfig:
    repo_root: Path
    data_root: Path
    out_root: Path
    lang_root: Path
    log_root: Path
    reports: Path


@dataclass
class BaseConfig:
    jobs: int


@dataclass
class TreeSitterConfig:
    build_path: Path
    libraries: List[Path]


@dataclass
class Config:
    paths: PathConfig
    base: BaseConfig

    treesitter: TreeSitterConfig


cs = ConfigStore.instance()
cs.store(name='mcpp.config', node=Config)
