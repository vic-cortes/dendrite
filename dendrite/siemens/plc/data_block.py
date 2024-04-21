from weakref import WeakKeyDictionary

INTEGER_BYTE_SIZE = 2
MAX_ALLOWED_INTEGER = 65_536 - 1


class BoolField:

    def __init__(self, *, byte_number: int, bit_position: int, db_number: int) -> None:
        self._byte_number = byte_number
        self._bit_position = bit_position
        self._db_number = db_number

        # Keeping track of each instance
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        # TODO: Add logic for data retrival from byte
        return self._values.get(instance)

    def __set__(self, instance, value):
        if not (0 <= value <= MAX_ALLOWED_INTEGER):
            raise ValueError(f"Value must be between 0 and {MAX_ALLOWED_INTEGER}")
        # TODO: Add logic for sending data to PLC
        self._values[instance] = value


class IntegerField:

    def __init__(self, *, byte_number: int, db_number: int) -> None:
        self._byte_size = INTEGER_BYTE_SIZE
        self._byte_number = byte_number
        self._db_number = db_number

        # Keeping track of each instance
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        # TODO: Add logic for data retrival from byte
        return self._values.get(instance)

    def __set__(self, instance, value):
        if not (0 <= value <= MAX_ALLOWED_INTEGER):
            raise ValueError(f"Value must be between 0 and {MAX_ALLOWED_INTEGER}")
        # TODO: Add logic for sending data to PLC
        self._values[instance] = value


class StatusDataBlock:
    level = IntegerField(byte_number=0, db_number=4)
