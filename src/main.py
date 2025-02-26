#!/usr/bin/env python
"""
Application main file.
"""
from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

import utils.config as config
import utils.logger as logger

import modules.webapi as webapi
from modules.db_manager import LootDatabase

__author__ = "Julien Balderiotti"
__copyright__ = "Copyright 2025, INOCESS"
__credits__ = ["Julien Balderiotti"]
__license__ = ""
__version__ = "0.1"
__maintainer__ = "Julien Balderiotti"
__email__ = "balderiotti@inocess.fr"
__status__ = "development"  # or production

ROOT_PATH = Path(__file__).parent.parent.resolve()
LOGS_DIR_PATH = ROOT_PATH / "logs"
CONFIG_DIR_PATH = ROOT_PATH / "config"
CONFIG_PATH = CONFIG_DIR_PATH / "config.ini"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="nvblootchecker")
    parser.add_argument('host', type=str)
    parser.add_argument('port', type=int)
    parser.add_argument('db_path', type=str)
    args = parser.parse_args(argv)

    # Load the configuration
    config_parser = config.load(CONFIG_PATH)

    # Configure the logging
    log_app = logger.setup(alias="app", file_path=LOGS_DIR_PATH / "app.log", level="INFO")
    if config_parser.getboolean('DEFAULT', 'Debug'):
        log_debug = logger.setup(alias="debug", file_path=LOGS_DIR_PATH / "debug.log", level="DEBUG")

    # Display configuration loaded
    log_app.info(f"Configuration loaded: {dict(config_parser.items('DEFAULT'))}")

    # Launch API
    webapi.run_app(args.host, args.port, args.db_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
