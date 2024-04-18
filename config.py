from abc import ABC, abstractmethod
from typing import Optional, TypedDict

import snap7

from utils import compute_integer_byte


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


class DataBlock(ABC):
    DB_NUMBER = None
    _plc = None

    class BytesMapping:
        pass

    def _get_current_byte(self, byte: int, size: int = 1) -> bytearray:
        """
        Get current value of a given byte
        """
        return self._plc.db_read(self.DB_NUMBER, start=byte, size=size)

    def _set_current_byte(self, byte: int, data: bytearray) -> bytearray:
        """
        Set current value of a given byte
        """
        return self._plc.db_write(self.DB_NUMBER, start=byte, data=data)

    def get_int_value(self, byte: int) -> int:
        """
        Reads data for integer field
        """
        INTEGER_SIZE = 2  # bytes
        reading = self._get_current_byte(byte=byte, size=INTEGER_SIZE)
        return int.from_bytes(reading)

    def _create_bytes_dict(self) -> None:
        bytes_dict = {}

        for key, value in self.BytesMapping.__dict__.items():
            if key.startswith("__"):
                continue

            current_values = bytes_dict.get(value) or []
            bytes_dict[value] = current_values.append(value)

        self.bytes_dict = bytes_dict
        return bytes_dict


class ByteConfig(TypedDict):
    type_of: str
    byte_number: int
    bit_position: int


class StatusDb(DataBlock):
    DB_NUMBER = 4

    class BytesMapping:
        LEVEL = 0.0
        IS_PUMP_RUNNING = 2.0
        IS_VALVE_OPEN = 2.1
        IS_FAULTED = 2.2
        IS_LOW_LEVEL = 2.3

    def __init__(self, connection: snap7.client.Client) -> None:
        self._plc = connection

    @property
    def level(self) -> int:
        return self.get_int_value(self.BytesMapping.LEVEL)

    @level.setter
    def level(self, _level: int) -> None:
        data = compute_integer_byte(_level)
        self._set_current_byte(byte=self.BytesMapping.LEVEL, data=data)

    @property
    def is_pump_running(self) -> bool:
        pass
