import time

import snap7

from config import DataBlock, Status

PLC_IP = "192.168.0.1"
RACK = 0
SLOT = 1


plc = snap7.client.Client()

plc.connect(PLC_IP, RACK, SLOT)

plc.get_cpu_info()

plc.get_cpu_state()

DB_NUMBER = 4
START_OFFSET = 0
BIT_OFFSET = 2

start, size = Status.RANGE
plc_params = {
    "db_number": DataBlock.EQUIPMENT,
    "start": start,
    "size": size,
}

reading = plc.db_read(**plc_params)

print(list(reading))
new_number = 456
plc.db_write(
    4,
    start,
    new_number.to_bytes((new_number.bit_length() + 7) // 8),
)
