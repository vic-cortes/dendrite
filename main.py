
import snap7

from config import DataBlock, Status, StatusDb

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
    status_db = StatusDb(connection=plc)

    print(status_db._create_bytes_dict())
