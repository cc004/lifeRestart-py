import random
import traceback
import pydoc
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
    while(10 < prop):
        prop -= 3
        ps = [x + 1 for x in ps]
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
    life.property.INT = 4

    life.talent.talents.append(TalentManager.talentDict[1001])
    life.talent.talents.append(TalentManager.talentDict[1002])
    life.talent.talents.append(TalentManager.talentDict[1004])
    life.talent.talents.append(TalentManager.talentDict[1005])
    life.talent.talents.append(TalentManager.talentDict[1016])
    life.talent.talents.append(TalentManager.talentDict[1017])
    life.talent.talents.append(TalentManager.talentDict[1022])
    life.talent.talents.append(TalentManager.talentDict[1048])
    life.talent.talents.append(TalentManager.talentDict[1060])
    life.talent.talents.append(TalentManager.talentDict[1065])
    life.talent.talents.append(TalentManager.talentDict[1072])
    life.talent.talents.append(TalentManager.talentDict[1104])
    life.talent.talents.append(TalentManager.talentDict[1114])
    life.talent.talents.append(TalentManager.talentDict[1118])
    life.talent.talents.append(TalentManager.talentDict[1129])
    life.talent.talents.append(TalentManager.talentDict[1131])
    life.talent.talents.append(TalentManager.talentDict[1134])
    life.talent.talents.append(TalentManager.talentDict[1135])
    #life.event.triggered.add(10007)

    for t in life.talent.talents:
        print(t)

    return life.run()

while True:
    result = []
    for x in run():
        result.append('——'.join(x))
    pydoc.pager('\n'.join(result))
    print("按任意键重新开始。。。")
    msvcrt.getch()
