import random
import traceback
import msvcrt

from Life import Life

Life.load('data')

def genp(prop):
    if(prop < 1):
        return { 'CHR': 0, 'INT': 0, 'STR': 0, 'MNY': 0 }
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

life = Life()

def run():
    life.setErrorHandler(lambda e: traceback.print_exc())
    life.setTalentHandler(lambda ts: random.choice(ts).id)
    life.setPropertyhandler(genp)
    
    #from TalentManager import TalentManager
    #life.talent.talents.append(TalentManager.talentDict[1122])
    
    life.choose()
    
    print(f'\n【第{life.tally()}轮开始】获得以下天赋：')
    for t in life.talent.talents:
        print(t)
    print(life.property)

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
    print(f"\n\n【第{life.tally()}轮结束】你可以从本轮天赋中选择一项继承到下一轮：\n0 放弃继承")
    i = 1
    for t in life.talent.talents:
        print(f"{i}.{t}")
        i+=1
    c = input("请输入希望继承的天赋序号（默认选择1）：")
    if c == 0:
        print('没有继承任何天赋……')
        life.restart()
    inherit = 1
    try:
        inherit = int(c)
    except:
        pass
    print(f'你的选择是：{inherit}')
    life.restart(inherit)
