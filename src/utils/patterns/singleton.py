class SingletonException(Exception):
    pass

class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls)
            return cls._instances[cls]
        raise SingletonException("Another instance of the singleton is already running")
