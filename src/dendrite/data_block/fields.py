INTEGER_BYTE_SIZE = 2


class IntegerField:

    def __init__(self, *args, **kwargs):
        self._byte_size = INTEGER_BYTE_SIZE
        self._bit_enable = False
        self._name = kwargs.get("name")
        self._byte_number = kwargs.get("byte_number")
        self._db_number = kwargs.get("db_number")

    @property
    def value(self) -> int:
        print("Getting value")
        return 20

    @value.setter
    def value(self, new_value: int) -> None:
        # data = compute_integer_byte(_level)
        print(f"Setting new value {new_value}")
        # self._set_current_byte(byte=self.BytesMapping.LEVEL, data=data)


class BoolField:

    def __init__(self, *args, **kwargs):
        self._byte_size = INTEGER_BYTE_SIZE
        self._bit_enable = True
        self._name = kwargs.get("name")
        self._byte_number = kwargs.get("byte_number")
        self._bit_position = kwargs.get("bit_position")
        self._db_number = kwargs.get("db_number")

    @property
    def value(self) -> int:
        print("Getting value")
        return 20

    @value.setter
    def value(self, new_value: int) -> None:
        # data = compute_integer_byte(_level)
        print(f"Setting new value {new_value}")
        # self._set_current_byte(byte=self.BytesMapping.LEVEL, data=data)
