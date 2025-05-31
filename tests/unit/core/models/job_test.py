import pytest
import inspect

from core.models.job import Job, SkillTag
from core.enums import ImportanceLevel, SkillType
from utils import get_missing_error_message, get_wrong_type_error_message, get_not_in_range_error_message


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
        assert skill_tag # Creation with experience_years argument
        # Creation without experience_years argument
        new_tag = SkillTag("C++", SkillType.TECHNICAL, ImportanceLevel.PIORITY)
        assert new_tag
        assert new_tag.experience_years == None

    def test_raise_exception_at_skill_tag_creation(self):
        """
        Ensure exceptions are raised for invalid instantiation.
        """
        # None value for required argument
        with pytest.raises(ValueError) as missing_arg_exception:
            SkillTag( "Project Management", SkillType.TECHNICAL, None)
        assert str(missing_arg_exception.value) == get_missing_error_message("skill_level")

        # Bad arguments order
        with pytest.raises(TypeError) as wrong_type_error:
            SkillTag(ImportanceLevel.LOW, SkillType.TECHNICAL, "Project Management", 2)
        assert str(wrong_type_error.value) == get_wrong_type_error_message("skill_name", ImportanceLevel, str)

        # Years value can't be negative
        with pytest.raises(ValueError) as not_in_range_exception:
            SkillTag( "Project Management", SkillType.TECHNICAL, ImportanceLevel.MEDIUM, -10)
        assert str(not_in_range_exception.value) == get_not_in_range_error_message("experience_years", -10, (0, 20))


    def test_property_reading(self, skill_tag: SkillTag, skill_props):
        """
        Check that all skill tag properties are readable.
        """
        for prop in skill_props:
            getattr(skill_tag, prop)

    def test_property_name_setting(self, skill_tag: SkillTag):
        """
        Check that setting the name works correctly
        """
        # Valid setting
        skill_tag.name = "Angular"
        assert skill_tag.name == "Angular"

        # Mising string value
        with pytest.raises(ValueError) as missing_arg_exception:
            skill_tag.name = None
        assert str(missing_arg_exception.value) == get_missing_error_message("skill_name")

        # Wrong type
        with pytest.raises(TypeError) as wrong_type_exception:
            skill_tag.name = 12
        assert str(wrong_type_exception.value) == get_wrong_type_error_message("skill_name", int, str)

    def test_property_type_setting(self, skill_tag: SkillTag):
        """
        Check that setting the type works correctly
        """
        # Valid setting
        skill_tag.type = SkillType.SOFT
        assert skill_tag.type == SkillType.SOFT

        # Mising value
        with pytest.raises(ValueError) as missing_arg_exception:
            skill_tag.type = None
        assert str(missing_arg_exception.value) == get_missing_error_message("skill_type")

        # Wrong type
        with pytest.raises(TypeError) as wrong_type_exception:
            skill_tag.type = 12
        assert str(wrong_type_exception.value) == get_wrong_type_error_message("skill_type", int, SkillType)

    def test_property_level_setting(self, skill_tag: SkillTag):
            """
            Check that setting the level works correctly
            """
            # Valid setting
            skill_tag.level = ImportanceLevel.PIORITY
            assert skill_tag.level ==  ImportanceLevel.PIORITY

            # Mising value
            with pytest.raises(ValueError) as missing_arg_exception:
                skill_tag.level = None
            assert str(missing_arg_exception.value) == get_missing_error_message("skill_level")

            # Wrong type
            with pytest.raises(TypeError) as wrong_type_exception:
                skill_tag.level = 12
            assert str(wrong_type_exception.value) == get_wrong_type_error_message("skill_level", int, ImportanceLevel)

    def test_property_experience_setting(self, skill_tag: SkillTag):
            """
            Check that setting the experience years works correctly
            """
            # Valid setting
            skill_tag.experience_years = 2
            assert skill_tag.experience_years == 2

            # Valid setting (None is accepted)
            skill_tag.experience_years = None
            assert skill_tag.experience_years == None

            # Wrong type
            with pytest.raises(TypeError) as wrong_type_exception:
                skill_tag.experience_years = "12"
            assert str(wrong_type_exception.value) == get_wrong_type_error_message("experience_years", str, int)

            # Years value can't be negative
            with pytest.raises(ValueError) as not_in_range_exception:
                skill_tag.experience_years = -1
            assert str(not_in_range_exception.value) == get_not_in_range_error_message("experience_years", -1, (0, 20))

             # Value can't be higher than 20 years
            with pytest.raises(ValueError) as not_in_range_exception:
                skill_tag.experience_years = -1
            assert str(not_in_range_exception.value) == get_not_in_range_error_message("experience_years", -1, (0, 20))



class TestJob():
    pass
