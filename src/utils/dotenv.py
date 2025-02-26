"""
Utils file for manage the environment variables.
"""
from __future__ import annotations

from os import environ
from pathlib import Path


class DotEnv:
    def __init__(self, file_path: Path | str):

        if not isinstance(file_path, Path):
            file_path = Path(file_path)

        self.file_path = file_path

    def load(self) -> None:
        if self.file_path.exists():
            with open(file=self.file_path) as envfile:
                for line in envfile:
                    if line.startswith('#') or not line.strip():
                        continue
                    key, value = line.strip().split('=', 1)
                    environ[key] = value
        else:
            raise FileNotFoundError(f'{self.file_path} does not exist')

    @staticmethod
    def get(key: str) -> str:
        return environ.get(key)
