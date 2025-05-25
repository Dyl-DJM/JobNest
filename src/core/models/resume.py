from pathlib import Path
from uuid import uuid4

from utils import validate_required_arg_type


class Resume():
    def __init__(self, name: str, path: Path):
        Resume._validate_construction(name, path)
        self.__id = str(uuid4())
        self.name = name
        self.path = path

    @staticmethod
    def _validate_construction(name: str, path: Path):
        validate_required_arg_type(name, "name", str)
        validate_required_arg_type(path, "path", Path)

    @property
    def id(self):
        return self.__id

    def attach_application(self, application_id: int):
        self.application_id = application_id
