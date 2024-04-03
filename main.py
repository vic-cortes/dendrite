import time

import snap7

from config import DataBlock, Status, StatusDataBlock

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
reading = plc.db_read(4, 0, 2)

print(list(reading))
value = 100
byte_array_big = value.to_bytes(
    (value.bit_length() + 7) // 8,
)
byte_array_little = value.to_bytes((value.bit_length() + 7) // 8, "little")
# int.from_bytes(byte_array)


def compute_integer_byte(value: int, print_string: bool = True) -> bytearray:
    """
    Computes the number of required bytes and
    create the corresponding payload
    """
    MINIMUN_BYTES = 2
    MAX_BYTE_VALUE = 255
    BYTE_LENGTH = 8
    END_BYTES = 0
    MAX_ALLOWED_INTEGER = 65_536 - 1

    if value > MAX_ALLOWED_INTEGER:
        raise ValueError("You passed max supported integer value")

    if value > MAX_BYTE_VALUE:
        closest_byte = value.bit_length() + 7
        payload = value.to_bytes(closest_byte // BYTE_LENGTH)

    else:
        total_bytes = []
        total_value = value

        for _ in range(MINIMUN_BYTES):
            total_bytes.append(total_value)
            total_value = END_BYTES

        # Reverse for byte array
        payload = bytearray([el for el in reversed(total_bytes)])

    if print_string:
        binary_string = " | ".join(format(byte, "08b") for byte in payload)
        print(f"Binary representation: {binary_string}")

    return payload


# Convertir bytearray a cadena de 1s y 0s
binary_string_big = " | ".join(format(byte, "08b") for byte in byte_array_big * 2)
binary_string_little = " | ".join(format(byte, "08b") for byte in byte_array_little)
print(f"{binary_string_big = }")
print(f"{binary_string_little = }")

value1 = 255
value2 = 0

# Crear bytearray
byte_array = bytearray([value2, value1])

print(byte_array)  # Salida: bytearray(b'd\x00')

plc.db_write(4, 0, byte_array)


if __name__ == "__main__":
    status_db = StatusDataBlock(connection=plc)

    print(status_db._create_bytes_dict())
