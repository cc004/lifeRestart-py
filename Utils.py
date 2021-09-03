import re
from typing import Callable


_regattr = re.compile('[A-Z]{3}')

def parseCondition(cond: str):
    cond = _regattr.sub(lambda m: f'getattr(x, "{m}")', cond).replace('?', ' in ').replace('![', ' not in [')
    return eval(f'lambda x: {cond}')