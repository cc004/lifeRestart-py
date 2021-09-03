from typing import Dict, List
from Talent import Talent

class PropertyManager:
    def __init__(self, base):
        self.base = base
        self.CHR = 0 # 颜值 charm CHR
        self.INT = 0 # 智力 intelligence INT
        self.STR = 0 # 体质 strength STR
        self.MNY = 0 # 家境 money MNY
        self.SPR = 5 # 快乐 spirit SPR

        self.AGE = -1
        self.LIF = 1 # hp
        
        self.total = 20
    
    @property
    def TLT(self) -> List[Talent]: # 天赋 talent TLT
        return self.base.talent.talents

    @property
    def EVT(self) -> List[Talent]:
        return self.base.talent.talents

    def apply(self, effect: Dict[str, int]):
        for key in effect:
            setattr(self, key, getattr(self, key) + effect[key])
