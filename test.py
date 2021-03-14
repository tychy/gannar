from state import State, Health
from fileio import load, gen
from alert import AlertHandle
from main import routine
from parser import checkOcc
import unittest


class NoWarTestCase(unittest.TestCase):
    def testNoWar(self):
        name = "nowar"
        expect = State.WAIT
        handler = AlertHandle(load(name))
        self.assertEqual(handler.state, expect)
    def testHealthOne(self):
        name = "health1"
        handler = AlertHandle(load(name))
        self.assertEqual(handler.state, State.RUN)
        self.assertEqual(handler.health, Health.NOFULL)
    def testOcc(self):
        name = "health1"
        checkOcc(load(name))



if __name__ == "__main__":
    unittest.main()

