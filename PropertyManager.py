from typing import Dict, Set

class PropertyManager:
    def __init__(self, base):
        self._base = base
        self.CHR = 0 # 颜值 charm CHR
        self.INT = 0 # 智力 intelligence INT
        self.STR = 0 # 体质 strength STR
        self.MNY = 0 # 家境 money MNY
        self.SPR = 5 # 快乐 spirit SPR

        self.AGE = -1
        self.LIF = 1 # hp
        
        self.total = 20

        self.TMS = 0
        self.AVT = []
    
    @property
    def TLT(self) -> Set[int]: # 天赋 talent TLT
        return self._base.talent.triggered

    @property
    def EVT(self) -> Set[int]:
        return self._base.event.triggered

    def apply(self, effect: Dict[str, int]):
        for key in effect:
            if key == "RDM":
                k = ['CHR','INT','STR','MNY','SPR'][id(key) % 5]
                setattr(self, k, getattr(self, k) + effect[key])
                continue
            setattr(self, key, getattr(self, key) + effect[key])
