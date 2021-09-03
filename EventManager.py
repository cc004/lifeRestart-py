from AgeManager import WeightedEvent
from typing import Dict, List, Set
from Event import Event

class EventManager:

    @staticmethod
    def load(config):
        EventManager._events: Dict[int, Event] = dict((int(k), Event(config[k]))for k in config)
        for k in EventManager._events:
            for b in EventManager._events[k].branch:
                b.evt = EventManager._events[b.id]

    def __init__(self, base, rnd):
        self.base = base
        self.triggered: Set[int] = set()
        self.rnd = rnd

    def randEvent(self, events: List[WeightedEvent]) -> int:
        if (self.base.property.AGE == 99):
            print(1)
        events_checked = []
        for ev in events:
            if EventManager._events[ev.evt].checkCondition(self.base.property):
                events_checked.append(ev)
        total = sum(e.weight for e in events_checked)
        rnd = self.rnd.random() * total
        for ev in events_checked:
            rnd -= ev.weight
            if rnd <= 0: return ev.evt
        return events[0].evt
    
    def runEvents(self, events: List[WeightedEvent]) -> List[str]:
        result = []
        ev = self.randEvent(events)
        self.triggered.add(ev)
        result.extend(EventManager._events[ev].runEvent(self.base.property))

        return result