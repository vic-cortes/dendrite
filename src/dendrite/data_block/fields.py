from dataclasses import dataclass


@dataclass
class Fields:
    name: str
    type: str
    byte: int
    bit: int
