import random as r
import string

class Robot:
    robot_names = set()
    def __init__(self):
        self._name = None       
    @property
    def name(self):
        if self._name:
            return self._name
        while True:
            letters = ''.join(r.choices(string.ascii_uppercase, k=2))
            digits = ''.join(r.choices(string.digits, k=3))
            name = letters + digits
            if name not in Robot.robot_names:
                Robot.robot_names.add(name)
                self._name = name
                return self._name
    def reset(self):
        self._name = None