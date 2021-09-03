from typing import Dict, List, Set
from Talent import Talent
import random

class AgeManager:
    @staticmethod
    def load(config):
        AgeManager._ages = config

    def __init__(self, base):
        self.base = base

    def _getnow(self):
        return AgeManager._ages[str(self.base.property.AGE)]
    
    def getEvents(self):
        now = self._getnow()
        if 'event' in now: return now['event']
        return []
    
    def getTalents(self):
        now = self._getnow()
        if 'talent' in now: return now['talent']
        return []
    
    def grow(self):
        self.base.property.AGE += 1