class SkillTag():
    def __init__(self, skill_name, skill_type, skill_level, experience_years=None):
        self.__name = skill_name
        self.__type = skill_type
        self.__level = skill_level
        self.__experience_years = experience_years

    @property
    def nameX(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def level(self):
        return self.__level

    @property
    def experience_years(self):
        return self.__experience_years


class Job():
    pass
