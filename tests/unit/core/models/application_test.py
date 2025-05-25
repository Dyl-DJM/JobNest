from core.models import Application
from core.enums import ApplicationStatus

def test_should_create_application():
    assert Application()
