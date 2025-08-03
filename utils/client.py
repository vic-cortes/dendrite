from snap7.client import Client as Snap7Client

from config import DataBlock, Status, StatusDb

PLC_IP = "127.0.0.1"
RACK = 0
SLOT = 1
TCP_PORT = 1102
DATA_BLOCK_NUMBER = 1


def connect_plc():
    client = Snap7Client()

    client.connect(PLC_IP, RACK, SLOT, TCP_PORT)
    client.get_cpu_info()
    client.get_cpu_state()

    plc_params = {
        "db_number": DATA_BLOCK_NUMBER,
        "start": 0,
        "size": 2,
    }
    reading = client.db_read(**plc_params)
    print(f"PLC reading: {reading}")


if __name__ == "__main__":
    connect_plc()
