from dataclasses import dataclass, field
from typing import List


@dataclass
class Event:
    title: str
    st_date: str
    end_date: str


@dataclass
class Schedule:
    name: str
    events: List[Event] = field(default_factory=list)

