from uuid import uuid4

class Application():
    def __init__(self):
        self.__id: str = str(uuid4())
        pass

    @property
    def id(self):
        return self.__id
