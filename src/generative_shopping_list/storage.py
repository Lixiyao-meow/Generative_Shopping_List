import pathlib
from typing import Protocol


class StorageBackend(Protocol):
    def read(self): ...


class YamlFileStorage:
    def __init__(self, path: pathlib.Path | str) -> None:
        self.path = path

    def read(self):
        import yaml

        with open(self.path, "r") as file:
            recipes = yaml.safe_load(file)
            return recipes


class HttpStorage:
    def __init__(self, url: str) -> None:
        self.path = url

    def read(self):
        import requests

        response = requests.get(self.path)
        return response.text


class S3Storage:
    # TODO
    pass
