from pathlib import Path
import pytest

from core.models.resume import Resume

resume_name = "CV1"
resume_path = Path("Company/Apple/FullStackDev/")


def test_should_create_resume():
    resume = Resume(resume_name, resume_path)
    assert resume.name == resume_name
    assert resume.path == resume_path


def test_should_throw_ValueError():
    # Missing name argument
    with pytest.raises(ValueError) as missing_name_exception:
        resume = Resume(None, resume_path)
    assert str(missing_name_exception.value) == "Missing required argument: 'name' for Resume"

    # Missing path argument
    with pytest.raises(ValueError) as missing_path_exception:
        resume = Resume(resume_name, None)
    assert str(missing_path_exception.value) == "Missing required argument: 'path' for Resume"


def test_should_throw_TypeError():
    # Wrong type for name argument
    with pytest.raises(TypeError) as wrong_type_for_name_exception:
        resume = Resume(resume_path, resume_path)
    assert str(wrong_type_for_name_exception.value) == "Wrong type for argument: 'name' fro Resume (should be a string object)"

    # Wrong type for path argument
    with pytest.raises(TypeError) as wrong_name_for_path_exception:
        resume = Resume(resume_name, "aStringAsThePath")
    assert str(wrong_name_for_path_exception.value) == "Wrong type for argument: 'path' fro Resume (should be a Path object)"


def test_should_retrieve_resume_id():
    resume = Resume(resume_name, resume_path)
    assert type(resume.id) == str


def test_should_not_update_resume_id():
    resume = Resume(resume_name, resume_path)
    with pytest.raises(AttributeError) as updating_resume_id_exception:
        resume.id = "newStrID"
