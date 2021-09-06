from Talent import Talent
from Life import Life
import traceback
import random
from TalentManager import TalentManager
Life.load('data')

def run():
    life = Life()
    life.setErrorHandler(lambda e: traceback.print_exc())
    life.setTalentHandler(lambda ts: random.choice(ts).id)
    def genp(prop):
        ps = []
        for _ in range(4):
            ps.append(min(prop, 8))
            prop -= ps[-1]
        return {
            'CHR': ps[0],
            'INT': ps[1],
            'STR': ps[2],
            'MNY': ps[3]
        }
    life.setPropertyhandler(genp)

    life.choose()
    life.property.INT = 1

    life.talent.talents.append(TalentManager.talentDict[1131])
    life.talent.talents.append(TalentManager.talentDict[1004])
    life.event.triggered.add(10007)

    for t in life.talent.talents:
        print(t)

    res = life.run()
    print('\n'.join('\n'.join(x) for x in res))

while True:
    run()