from pathlib import Path
import pytest
import re

from core.models.resume import Resume
from utils import get_missing_error_message, get_wrong_type_error_message

resume_name = "CV1"
resume_path = Path("Company/Apple/FullStackDev/")
wrong_type_path_message_pattern = r"Wrong type for argument: 'name' \('\w*Path' object\) should be 'str'"


def test_should_create_resume():
    resume = Resume(resume_name, resume_path)
    assert resume.name == resume_name
    assert resume.path == resume_path


def test_should_throw_ValueError():
    # Missing name argument
    with pytest.raises(ValueError) as missing_name_exception:
        resume = Resume(None, resume_path)
    assert str(missing_name_exception.value) == get_missing_error_message("name")

    # Missing path argument
    with pytest.raises(ValueError) as missing_path_exception:
        resume = Resume(resume_name, None)
    assert str(missing_path_exception.value) == get_missing_error_message("path")


def test_should_throw_TypeError():
    # Wrong type for name argument
    with pytest.raises(TypeError) as wrong_type_for_name_exception:
        resume = Resume(resume_path, resume_path)
    assert re.fullmatch(wrong_type_path_message_pattern, str(wrong_type_for_name_exception.value))

    # Wrong type for path argument
    with pytest.raises(TypeError) as wrong_name_for_path_exception:
        resume = Resume(resume_name, "aStringAsThePath")
    assert str(wrong_name_for_path_exception.value) == get_wrong_type_error_message("path", str, Path)


def test_should_retrieve_resume_id():
    resume = Resume(resume_name, resume_path)
    assert type(resume.id) == str


def test_should_not_update_resume_id():
    resume = Resume(resume_name, resume_path)
    with pytest.raises(AttributeError) as updating_resume_id_exception:
        resume.id = "newStrID"
