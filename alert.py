from state import *

class AlertHandle:
    health = Health.NOFULL

    def run_assert(self):
        text = ""
        if(self.health == Health.FULL):
            text += "full health\n"
        sendLineNotify(text)

