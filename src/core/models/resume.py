from pathlib import Path
from uuid import uuid4


class Resume():
    def __init__(self, name: str, path: Path):
        if name is None:
            raise ValueError("Missing required argument: 'name' for Resume")
        if path is None:
            raise ValueError("Missing required argument: 'path' for Resume")
        self.__id = str(uuid4())
        self.name = name
        self.path = path

    @property
    def id(self):
        return self.__id

    def attach_application(self, application_id: int):
        self.application_id = application_id
