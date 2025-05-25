import pytest
import inspect

from core.models.job import Job, SkillTag
from core.enums import ImportanceLevel, SkillType

class TestSkillTag:
    """
    Unit tests for the SkillTag class to ensure its correct behavior and data encapsulation.

    Tests:
    - Object creation with expected arguments.
    - Property access to confirm readable attributes.
    - Property immutability to ensure fields cannot be modified post-instantiation.

    Fixtures:
    - skill_tag: Returns a sample SkillTag instance for use in tests.
    - skill_props: Dynamically collects all public @property attributes of the SkillTag class.

    Note:
    These tests rely on the assumption that all important attributes of SkillTag
    are exposed via read-only @property methods and are named consistently.
    """

    # Prefix of all the private attributes
    private_attr_prefix: str = "_"

    @pytest.fixture
    def skill_tag(self):
        """
        Fixture that returns a default SkillTag instance.
        """
        return SkillTag("Python", SkillType.TECHNICAL, ImportanceLevel.HIGH, 2)

    @pytest.fixture
    def skill_props(self, skill_tag: SkillTag):
        """
        Fixture that returns a list of all @property attributes of the SkillTag
        object returned by the skill_tag fixture.
        """
        return [name for name, value in inspect.getmembers(skill_tag.__class__, lambda v: isinstance(v, property))]

    def test_create_skill_tag(self, skill_tag):
        """
        Check that a skill tag can be created sucessfully.
        """
        assert skill_tag
        assert SkillTag("C++", SkillType.TECHNICAL, ImportanceLevel.PIORITY)

    def test_raise_exception_at_skill_tag_creation(self):
        #
        pass


    def test_property_reading(self, skill_tag: SkillTag, skill_props):
        """
        Check that all skill tag properties are readable.
        """
        for prop in skill_props:
            getattr(skill_tag, prop)

    def test_property_name_setting(self, skill_tag: SkillTag):
        # Valid setting
        skill_tag.name = "Angular"
        assert skill_tag.name == "Angular"




class TestJob():
    pass
