from enum import Enum

class Alert(Enum):
    ATTACK  = 6
    GAMMA = 5
    BETA = 4
    HOME = 3
    OCC = 2
    HEALTH = 1

class State(Enum):
    WAIT = 0
    RUN = 1

class Health(Enum):
    FULL = 1
    NOFULL = 1

    
