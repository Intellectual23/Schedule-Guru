from dataclasses import dataclass, field
from typing import List


@dataclass
class Event:
    title: str
    st_date: int
    end_date: int

