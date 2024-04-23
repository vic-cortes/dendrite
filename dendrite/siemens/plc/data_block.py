from weakref import WeakKeyDictionary

INTEGER_BYTE_SIZE = 2
MAX_ALLOWED_INTEGER = 65_536 - 1
MAX_ALLOWED_DB_NUMBER = 20


class DataBlock:
    db_number = None

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        if cls.db_number is None:
            raise ValueError("'db_number' must be set")

        if not isinstance(cls.db_number, int):
            raise ValueError("'db_number' must be an integer")

        if not (0 <= cls.db_number <= MAX_ALLOWED_DB_NUMBER):
            raise ValueError("db_number must be between 0 and 20")


class BoolField:

    def __init__(self, *, byte_number: int, bit_position: int) -> None:
        self._byte_number = byte_number
        self._bit_position = bit_position

        # Keeping track of each instance
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        # TODO: Add logic for data retrieve from byte
        db_number = instance_type.db_number
        if instance is None:
            return self
        return self._values.get(instance)

    def __set__(self, instance, value):
        db_number = instance.db_number
        if not (0 <= value <= MAX_ALLOWED_INTEGER):
            raise ValueError(f"Value must be between 0 and {MAX_ALLOWED_INTEGER}")
        # TODO: Add logic for sending data to PLC
        self._values[instance] = value


class IntegerField:

    def __init__(self, *, byte_number: int) -> None:
        self._byte_size = INTEGER_BYTE_SIZE
        self._byte_number = byte_number

        # Keeping track of each instance
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type) -> None:
        #! Note: this variable is used to get the db_number from the instance
        #! is very important since with db_number we can get the data from the PLC
        db_number = instance_type.db_number
        if instance is None:
            return self
        # TODO: Add logic for data retrieve from byte
        return self._values.get(instance)

    def __set__(self, instance, value) -> None:
        # db_number = instance.db_number
        if not (0 <= value <= MAX_ALLOWED_INTEGER):
            raise ValueError(f"Value must be between 0 and {MAX_ALLOWED_INTEGER}")
        # TODO: Add logic for sending data to PLC
        self._values[instance] = value
