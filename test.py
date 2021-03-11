from state import State, Health
from fileio import load, gen
from alert import AlertHandle
from main import routine

import unittest


class NoWarTestCase(unittest.TestCase):
    def testNoWar(self):
        name = "nowar"
        expect = State.WAIT
        handler = AlertHandle(load(name))
        self.assertEqual(handler.state, expect)

if __name__ == "__main__":
    unittest.main()

