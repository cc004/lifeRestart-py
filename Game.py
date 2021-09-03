from typing import Callable, Dict, List
from Talent import Talent, TalentManager
import os
import json

class Game:
    def __init__(self, datapath):
        self._talenthandler = None
        self._propertyhandler = None
        with open(os.path.join(datapath, 'talents.json')) as fp:
            self.talents = TalentManager(json.load(fp))

    def setTalentHandler(self, handler: Callable[[List[Talent]], List[int]]) -> None:
        '''
        handler recv randomized talents
        ret series of talent ids
        '''
        self._talenthandler = handler
    def setPropertyhandler(self, handler: Callable[[int], Dict[str, int]]) -> None:
        '''
        handler recv total props
        ret prop alloc
        '''
        self._propertyhandler = handler

    def run(self) -> List[str]:
        '''
        returns: information splited by day
        '''
