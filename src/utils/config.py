"""
Utils file for manage configuration files.
"""
from __future__ import annotations

import configparser
from pathlib import Path


def load(config_path: str | Path) -> configparser.ConfigParser:
    """
    Load a configuration file.
    :param config_path: configuration file path.
    :return: configuration parser.
    """
    if not isinstance(config_path, Path):
        config_path = Path(config_path)

    parser = configparser.ConfigParser()

    if not config_path.exists():
        raise FileNotFoundError(f"File {config_path} does not exist.")

    parser.read(config_path)

    return parser
