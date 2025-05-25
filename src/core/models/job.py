from core.enums import SkillType, ImportanceLevel

class SkillTag():
    def __init__(self, skill_name: str, skill_type: SkillType, skill_level: ImportanceLevel, experience_years=None):
        self.__name = skill_name
        self.__type = skill_type
        self.__level = skill_level
        self.__experience_years = experience_years

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, skill_name: str):
        if not skill_name:
            raise  ValueError("Missing required argument: 'skill_name' for SkillTag")
        if not isinstance(skill_name, str):
            raise  ValueError("Wrong type for argument: 'skill_name' for SkillTag (should be a str object)")
        self.__name = skill_name

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
