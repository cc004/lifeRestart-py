from Life import Life
import traceback

Life.load('data')

life = Life()
life.setErrorHandler(lambda e: traceback.print_exc())
life.setTalentHandler(lambda ts: ts[0].id)
def genp(prop):
    ps = []
    for _ in range(4):
        ps.append(min(prop, 10))
        prop -= ps[-1]
    return {
        'CHR': ps[0],
        'INT': ps[1],
        'STR': ps[2],
        'MNY': ps[3]
    }
life.setPropertyhandler(genp)

life.choose()

for t in life.talent.talents:
    print(t)

life.run()