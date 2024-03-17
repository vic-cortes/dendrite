from dataclasses import dataclass


class Status:
    RANGE = (0, 2)

    I_LEVEL = 0
    X_PUMP_RUNNING = 2
    X_VALVE_OPEN = 2.1
    X_FAULTED = 2.2
    X_LOW_LEVEL = 2.3


class Supply:
    STATUS = Status()


class Equipment:
    SUPPLY = Supply()


class DataBlock:
    EQUIPMENT = 4


class BytesMapping:
    IlEVEL = 0
    PUMP_RUNNING = 2
    VALVE_OPEN = 2
    FAULTED = 2
    LOW_LEVEL = 2


@dataclass
class StatusDataBlock:
    i_level: int = 0
    x_pump_running: bool = False
    x_valve_open: bool = False
    x_faulted: bool = False
    x_low_level: bool = False

    def _current_byte_status(self, byte: int):
        """
        Get current value of a given byte
        """
        pass

    def set_level(self, level: int) -> None:
        pass
