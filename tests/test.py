from dendrite.siemens.plc import data_block as siemens


class StatusDataBlock(siemens.DataBlock):

    level = siemens.IntegerField(byte_number=0, db_number=4)
    pump_running = siemens.BoolField(byte_number=2, bit_position=0, db_number=4)


if __name__ == "__main__":
    status = StatusDataBlock()

    status.level
    status.level = 30
