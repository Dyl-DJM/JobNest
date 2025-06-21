from core.enums import SkillType, ImportanceLevel
from utils import validate_required_arg_type, validate_arg_type, validate_int_in_range

class SkillTag():
    """Represent a skill tag that can be used to describe a skill needed by a job offer.

    Warning:
        Each private attribute should match its corresponding property name.

    Attributes:
        name (str): skill name/title
        type (SkillType): indication of the skill nature
        level (ImportanceLevel): indication of the skill importance
        experience_years (int): Number of years of experience with the skill
                                (0 ≤ n ≤ 20) (default None)
    """
    def __init__(self, skill_name: str, skill_type: SkillType,
                 skill_level: ImportanceLevel, experience_years:int=None):
        SkillTag._validate_construction(skill_name, skill_type, skill_level, experience_years)
        self._name = skill_name
        self._type = skill_type
        self._level = skill_level
        self._experience_years = experience_years

    @staticmethod
    def _validate_construction(skill_name: str, skill_type: SkillType,
                 skill_level: ImportanceLevel, experience_years: int=None):
        """Check that parameters are valid for creating a SkillTag object.

        Validates the input by raising an exception if a parameter is of the wrong type
        or violates value constraints. This function returns nothing.
        """
        validate_required_arg_type(skill_name, 'skill_name', str)
        validate_required_arg_type(skill_type, 'skill_type', SkillType)
        validate_required_arg_type(skill_level, 'skill_level', ImportanceLevel)
        SkillTag._validate_experience_years(experience_years)

    @property
    def name(self):
        """Get the skill's name."""
        return self._name

    @name.setter
    def name(self, skill_name: str):
        """Set the skill's name."""
        validate_required_arg_type(skill_name, 'skill_name', str)
        self._name = skill_name

    @property
    def type(self):
        """Get the skill's type."""
        return self._type

    @type.setter
    def type(self, skill_type: SkillType):
        """Set the skill's type."""
        validate_required_arg_type(skill_type, "skill_type", SkillType)
        self._type = skill_type

    @property
    def level(self):
        """Get the skill's level of importance."""
        return self._level

    @level.setter
    def level(self, skill_level:ImportanceLevel):
        """Set the skill's level of importance."""
        validate_required_arg_type(skill_level, "skill_level", ImportanceLevel)
        self._level = skill_level

    @staticmethod
    def _validate_experience_years(experience_years: int):
        """Verify the skill's experience input."""
        if experience_years is None:
            return
        validate_arg_type(experience_years, "experience_years", int)
        validate_int_in_range(experience_years, (0, 20), "experience_years")

    @property
    def experience_years(self):
        """Get the skill's years of experience."""
        return self._experience_years

    @experience_years.setter
    def experience_years(self, years: int):
        """Set the skill's years of experience.

        Not all skills can be associated with a number of years. In such cases, the value can be None.

        Raises:
            ValueError: If the number of years is less than 0 or greater than 20.
        """
        SkillTag._validate_experience_years(years)
        self._experience_years = years


class Job():
    pass
