from core.enums import SkillType, ImportanceLevel
from utils import validate_required_arg_type, validate_arg_type

class SkillTag():
    def __init__(self, skill_name: str, skill_type: SkillType,
                 skill_level: ImportanceLevel, experience_years:int=None):
        SkillTag._validate_construction(skill_name, skill_type, skill_level, experience_years)
        self._name = skill_name
        self._type = skill_type
        self._level = skill_level
        self._experience_years = experience_years

    @staticmethod
    def _validate_construction(skill_name: str, skill_type: SkillType,
                 skill_level: ImportanceLevel, experience_years=None):
        validate_required_arg_type(skill_name, 'skill_name', str)
        validate_required_arg_type(skill_type, 'skill_type', SkillType)
        validate_required_arg_type(skill_level, 'skill_level', ImportanceLevel)
        validate_arg_type(experience_years, 'experience_years', int)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, skill_name: str):
        validate_required_arg_type(skill_name, 'skill_name', str)
        self._name = skill_name

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, skill_type: SkillType):
        validate_required_arg_type(skill_type, "skill_type", SkillType)
        self._type = skill_type

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, skill_level:ImportanceLevel):
        validate_required_arg_type(skill_level, "skill_level", ImportanceLevel)
        self._level= skill_level

    @property
    def experience_years(self):
        return self._experience_years


class Job():
    pass
