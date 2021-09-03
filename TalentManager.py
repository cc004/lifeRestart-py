from typing import Dict, List, Set
from Talent import Talent
import random

class TalentManager:
    grade_count = 4
    grade_prob = [0.889, 0.1, 0.01, 0.001]

    @staticmethod
    def load(config):
        TalentManager._talents: Dict[int, List[Talent]] = dict([(i, []) for i in range(TalentManager.grade_count)])
        for k in config.keys():
            t = Talent(config[k])
            TalentManager._talents[t.grade].append(t)

    def __init__(self, base, rnd=None):
        self.base = base
        self.talents: List[Talent] = []
        self.triggered: Set[int] = set()
        self.rnd = rnd or random.Random()

    def _genGrades(self):
        rnd = self.rnd.random()
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
            result.extend(self.rnd.sample(TalentManager._talents[grade], k=count))
        return result

    def updateTalent(self) -> str:
        result = []
        for t in self.talents:
            if not t.id in self.triggered: continue
            r = t.runTalent(self.base.property)
            if r is not None:
                self.triggered.add(t.id)
                result.append(r)
        return result
