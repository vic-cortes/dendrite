from dendrite.siemens.plc.data_block import BoolField, DataBlock, IntegerField


class StatusDataBlock(DataBlock):
    db_number = 20

    level = IntegerField(byte_number=5)
    level2 = IntegerField(byte_number=5)
    pump_running = BoolField(byte_number=2, bit_position=0)


# class ExampleDataBlock(siemens.DataBlock):
#     db_number = 4


if __name__ == "__main__":
    status = StatusDataBlock()
    status.to_dict()
    status.level
    status.level = 10
    status.to_dict()
    status.level

    status.level2
    # status.level = 20
    status.pump_running
    # print(status.level._by_size)
    # status.level = 30
