from core.enums import SkillType, ImportanceLevel

class SkillTag():
    def __init__(self, skill_name: str, skill_type: SkillType, skill_level: ImportanceLevel, experience_years=None):
        self._name = skill_name
        self._type = skill_type
        self._level = skill_level
        self._experience_years = experience_years

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, skill_name: str):
        if not skill_name:
            raise  ValueError("Missing required argument: 'skill_name' for SkillTag")
        if not isinstance(skill_name, str):
            raise  ValueError("Wrong type for argument: 'skill_name' for SkillTag (should be a str object)")
        self._name = skill_name

    @property
    def type(self):
        return self._type

    @property
    def level(self):
        return self._level

    @property
    def experience_years(self):
        return self._experience_years


class Job():
    pass
