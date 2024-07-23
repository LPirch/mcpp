from typing import List
from dataclasses import dataclass
from pathlib import Path

from hydra.core.config_store import ConfigStore


@dataclass
class PathConfig:
    repo_root: Path
    lib_root: Path
    data_root: Path
    out_root: Path
    log_root: Path



@dataclass
class Config:
    in_path: Path
    out_path: Path
    metrics: List[str]
    paths: PathConfig


cs = ConfigStore.instance()
cs.store(name='mcpp.config', node=Config)
