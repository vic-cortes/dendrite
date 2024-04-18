from dendrite.data_block.fields import BoolField, IntegerField


class StatusDataBlock:
    DB_NUMBER = 4

    level = IntegerField(name="level", byte_number=0, db_number=DB_NUMBER)
    pump_running = BoolField(
        name="pump_running", byte_number=2, bit_position=0, db_number=DB_NUMBER
    )


if __name__ == "__main__":
    StatusDataBlock.level.value
    StatusDataBlock.level.value = 30
