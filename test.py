import random
import traceback
import msvcrt

from Talent import Talent
from Life import Life
from TalentManager import TalentManager

Life.load('data')

def genp(prop):
    ps = []
    for i in range(3):
        ps.append(id(i) % (int(prop * 2 / (4 - i)) + 1))
        if(10 < ps[-1]):
            ps[-1] = 10
        prop -= ps[-1]
    if(10 < prop):
        prop+=sum(ps)
        ps = [int(prop / 4)] * 3
        prop-=sum(ps)
    return {
        'CHR': ps[0],
        'INT': ps[1],
        'STR': ps[2],
        'MNY': prop
    }

def run():
    life = Life()
    life.setErrorHandler(lambda e: traceback.print_exc())
    life.setTalentHandler(lambda ts: random.choice(ts).id)
    life.setPropertyhandler(genp)

    life.choose()
    #life.property.INT = 10

    life.talent.talents.append(TalentManager.talentDict[1048])
    life.talent.talents.append(TalentManager.talentDict[1065])
    life.talent.talents.append(TalentManager.talentDict[1134])
    
    #life.event.triggered.add(40063)

    for t in life.talent.talents:
        print(t)

    return life.run()

while True:
    i = 0
    for x in run():
        print(f'\n{x[0]}{"——".join(x[1:])}',end='',flush=True)
        if(0 < i):
            i-=1
            continue
        if(msvcrt.getch() == b' '):
            i = 9
    print("\n\n[人生重开了]")
    msvcrt.getch()
