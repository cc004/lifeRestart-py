from typing import Dict, List
from Talent import Talent

class PropertyManager:
    def __init__(self, base):
        self.base = base
        self.CHR = 0
        self.INT = 0
        self.STR = 0
        self.MNY = 0
        self.SPR = 5

        self.AGE = -1
        self.LIF = 1 # hp
        
        self.total = 20
    
    @property
    def TLT(self) -> List[Talent]:
        return self.base.talent.talents

    def apply(self, effect: Dict[str, int]):
        for key in effect:
            setattr(self, key, getattr(self, key) + effect[key])
