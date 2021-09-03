from typing import Dict, List
from Utils import parseCondition

class Talent:
    def __init__(self, json):
        self.id: int = int(json['id'])
        self.name: str = json['name']
        self.desc: str = json['description']
        self.grade: int = int(json['grade'])
        self._exclusive: List[int] = [int(x) for x in json['exclusive']] if'exclusive' in json else []
        self._effect: Dict[str, int] = json['effect'] if 'effect' in json else {}
        if 'status' in json:
            self._effect['status'] = int(json['status'])
        self.cond = parseCondition(json['condition']) if 'condition' in json else lambda _: True
    def isExclusiveWith(self, talent) -> bool:
        return talent.id in self._exclusive or self.id in talent._exclusive
    def apply(self, prop) -> None:
        prop.apply(self._effect)
    def __str__(self) -> str:
        return f'Talent(name={self.name})'
    def checkCondition(self, prop) -> bool:
        return self.cond(prop)
    def runTalent(self, prop) -> str:
        if not self.checkCondition(prop):
            self.apply(prop)
            return f'天赋【{self.name}】发动：{self.description}'
        return None