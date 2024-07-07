import datetime
from dataclasses import dataclass, field
from typing import List


@dataclass
class Event:
    name: str
    time: datetime.time
    description: str


@dataclass
class Schedule:
    name: str
    events: List[Event] = field(default_factory=list)

