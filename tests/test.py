from dendrite.siemens.plc import data_block as siemens


class StatusDataBlock(siemens.DataBlock):
    db_number = 20

    level = siemens.IntegerField(byte_number=5)
    level2 = siemens.IntegerField(byte_number=5)
    pump_running = siemens.BoolField(byte_number=2, bit_position=0)


# class ExampleDataBlock(siemens.DataBlock):
#     db_number = 4


if __name__ == "__main__":
    status = StatusDataBlock()

    status.level
    status.level2
    # status.level = 20
    status.pump_running
    # print(status.level._by_size)
    # status.level = 30
