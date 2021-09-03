from typing import Dict, List, Set
from Talent import Talent

class TalentManager:
    grade_count = 4
    grade_prob = [0.889, 0.1, 0.01, 0.001]

    @staticmethod
    def load(config):
        TalentManager._talents: Dict[int, List[Talent]] = dict([(i, []) for i in range(TalentManager.grade_count)])
        for k in config.keys():
            t = Talent(config[k])
            TalentManager._talents[t.grade].append(t)

    def __init__(self, base, rnd):
        self._base = base
        self.talents: List[Talent] = []
        self.triggered: Set[int] = set()
        self._rnd = rnd

    def _genGrades(self):
        rnd = self._rnd.random()
        result = TalentManager.grade_count
        while rnd > 0:
            result -= 1
            rnd -= TalentManager.grade_prob[result]
        return result
    
    def genTalents(self, count: int) -> List[Talent]:
        # should not repeats
        counts = dict([(i, 0) for i in range(TalentManager.grade_count)])
        for _ in range(count):
            counts[self._genGrades()] += 1
        result = []
        for grade in range(TalentManager.grade_count - 1, -1, -1):
            count = counts[grade]
            n = len(TalentManager._talents[grade])
            if count > n:
                counts[grade - 1] += count - n
                count = n
            result.extend(self._rnd.sample(TalentManager._talents[grade], k=count))
        return result

    def updateTalentProp(self):
        self._base.property.total += sum(t.status for t in self.talents)

    def updateTalent(self) -> List[str]:
        result = []
        for t in self.talents:
            if t.id in self.triggered: continue
            r = t.runTalent(self._base.property)
            if r:
                self.triggered.add(t.id)
                result.extend(r)
        return result

    def addTalent(self, talent: Talent):
        for t in self.talents:
            if t.id == talent.id: return
        self.talents.append(talent)