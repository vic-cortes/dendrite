from dendrite.siemens.plc import data_block as siemens


class StatusDataBlock:
    DB_NUMBER = 4

    level = siemens.IntegerField(byte_number=0, db_number=DB_NUMBER)
    pump_running = siemens.BoolField(byte_number=2, bit_position=0, db_number=DB_NUMBER)


if __name__ == "__main__":
    status = StatusDataBlock()

    status.level
    status.level = 30
