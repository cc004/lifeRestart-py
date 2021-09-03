from typing import Dict, List
import random

class Talent:
    def __init__(self, json):
        self.id: int = int(json['id'])
        self.name: str = json['name']
        self.desc: str = json['description']
        self.grade: int = int(json['id'])
        self._exclusive: List[int] = [int(x) for x in json['exclusive']] if'exclusive' in json else []
        self._effect: Dict[str, int] = json['effect'] if 'effect' in json else {}
    def isExclusiveWith(self, talent) -> bool:
        return talent.id in self._exclusive or self.id in talent._exclusive
    def apply(self) -> None:
        pass

class TalentManager:
    grade_count = 4
    grade_prob = [0.889, 0.1, 0.01, 0.001]
    def __init__(self, config, rnd=None):
        self._talents: Dict[int, List[Talent]] = dict([(i, []) for i in range(TalentManager.grade_count)])
        for k in config.keys():
            t = Talent(config[k])
            self._talents[t.grade].append(t)
        self.rnd = rnd or random.Random()

    def genGrades(self):
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
            counts[self.genGrades()] += 1
        result = []
        for grade in range(TalentManager.grade_count - 1, -1, -1):
            count = counts[grade]
            n = len(self._talents[grade])
            if count > n:
                counts[grade - 1] += count - n
                count = n
            result.extend(self.rnd.sample(self._talents[grade], k=count))
        return result
