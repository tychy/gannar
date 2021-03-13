from state import State, Health
from parser import checkState, checkHealth
from connect import sendLineNotify

class AlertHandle:

    def __init__(self, data):
        self.state = checkState(data)
        self.health= checkHealth(data)
        return

    def run_assert(self):
        if(self.state == State.WAIT):
            print("WAIT")
            return
        text = ""
        if(self.health == Health.FULL):
            text += "full health\n"
        sendLineNotify(text)

