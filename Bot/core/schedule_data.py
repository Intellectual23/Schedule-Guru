from dataclasses import dataclass


@dataclass
class Event:
    title: str
    st_date: int
    end_date: int

