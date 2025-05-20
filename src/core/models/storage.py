from core.models.resume import Resume
from core.models.application import Application
from core.models.letter import Letter
from core.utils import Singleton

class Storage(Singleton):
    def __init__(self):
        self.__applications: dict[str, Application] = {}
        self.__resumes: dict[str, Resume] = {}
        self.__letters: dict[str, Letter] = {}

    @property
    def applications(self):
        return self.__applications

    @property
    def resumes(self):
        return self.__resumes

    @property
    def letters(self):
        return self.__letters

    def addApplication(self, application: Application):
        if application.id in self.__applications:
            raise KeyError(f"Key {application.id} already exists in the storage")
        self.applications[application.id] = application

storage = Storage()
