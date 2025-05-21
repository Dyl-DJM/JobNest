from enum import Enum

class ApplicationStatus(Enum):
    UNCOMPLETE = 0
    WAITING = 1
    REFUSAL = 2
    JOB_INTERVIEW = 3
    TECHNICAL_INTERVIEW = 4
    SIMPLE_CALL = 5

