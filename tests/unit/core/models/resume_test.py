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


def test_should_retrieve_resume_id():
    resume = Resume(resume_name, resume_path)
    assert type(resume.id) == str

def test_should_not_update_resume_id():
    resume = Resume(resume_name, resume_path)
    with pytest.raises(AttributeError) as updating_resume_id_exception:
        resume.id = "newStrID"
