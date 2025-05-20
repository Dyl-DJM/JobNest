from core.models import Application, storage

def test_should_add_application():
    job_app = Application()
    storage.addApplication(job_app)
    assert storage.applications.__len__() == 1


